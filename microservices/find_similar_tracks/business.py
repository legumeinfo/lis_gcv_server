from core.utils import cleanTrack, formatGene
from collections import defaultdict


# families - an ordered list of gene family ids representing the query context
# min_matched - the number of families that must match in each block
# max_intermediate - the max number of intermediate genes allowed between any two matched genes
async def searchMicroSyntenyTracks(r, rpc, families, min_matched, max_intermediate):
  # get all genes of the query families
  families = list(map(lambda f: 'family:' + f, families))
  params = {'families': families}
  family_gene_ids = await rpc.call('/family/get-family-genes', params)
  pipeline = r.pipeline()
  for gene_ids in family_gene_ids:
    for g in gene_ids:
      pipeline.hmget('gene:' + g, 'chromosome', 'number')
  genes = await pipeline.execute()
  # bin the gene numbers by chromosome
  chromosome_nums = defaultdict(list)
  for chromosome, number in genes:
    chromosome_nums[chromosome].append(int(number))
  # compute islands and gaps
  blocks = defaultdict(list)
  for c, nums in chromosome_nums.items():
    nums.sort()
    block = []
    for n in nums:
      if not block or n-block[-1] <= max_intermediate-1:
        block.append(n)
      else:
        if len(block) >= min_matched:
          blocks[c].append(block)
        block = []
    if len(block) >= min_matched:
      blocks[c].append(block)
  # fetch result tracks
  families = set()
  tracks = {'groups': []}
  for c, blocks in blocks.items():
    chromosome = await r.hgetall(c)
    genus, species = chromosome['organism'].split(':')[1:]
    for b in blocks:
      first = b[0]
      last = b[-1]
      gene_ids = await r.lrange(c + ':genes', first, last)
      pipeline = r.pipeline()
      for g in gene_ids:
        pipeline.hgetall(g)
      genes = await pipeline.execute()
      # format and return
      track = {
        'genus': genus,
        'species': species,
        'species_id': chromosome['organism'],
        'chromosome_name': chromosome['name'],
        'chromosome_id': c,
        'genes': list(map(lambda e: formatGene(*e), zip(gene_ids, genes)))
      }
      cleanTrack(track)
      families.update(map(lambda g: g['family'], track['genes']))
      tracks['groups'].append(track)
  families.discard('')
  tracks['families'] = list(map(lambda f: {'id': f, 'name': f}, families))
  return tracks