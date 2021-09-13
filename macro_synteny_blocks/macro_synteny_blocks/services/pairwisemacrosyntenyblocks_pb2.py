# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: services/pairwisemacrosyntenyblocks.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from macro_synteny_blocks.structures import block_pb2 as structures_dot_block__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='services/pairwisemacrosyntenyblocks.proto',
  package='gcv.services',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n)services/pairwisemacrosyntenyblocks.proto\x12\x0cgcv.services\x1a\x16structures/block.proto\"\xaa\x01\n(PairwiseMacroSyntenyBlocksComputeRequest\x12\x12\n\nchromosome\x18\x01 \x03(\t\x12\x0e\n\x06target\x18\x02 \x01(\t\x12\x0f\n\x07matched\x18\x03 \x01(\r\x12\x14\n\x0cintermediate\x18\x04 \x01(\r\x12\x11\n\x04mask\x18\x05 \x01(\rH\x00\x88\x01\x01\x12\x17\n\x0foptionalMetrics\x18\x06 \x03(\tB\x07\n\x05_mask\"O\n&PairwiseMacroSyntenyBlocksComputeReply\x12%\n\x06\x62locks\x18\x01 \x03(\x0b\x32\x15.gcv.structures.Block2\x97\x01\n\x1aPairwiseMacroSyntenyBlocks\x12y\n\x07\x43ompute\x12\x36.gcv.services.PairwiseMacroSyntenyBlocksComputeRequest\x1a\x34.gcv.services.PairwiseMacroSyntenyBlocksComputeReply\"\x00\x62\x06proto3'
  ,
  dependencies=[structures_dot_block__pb2.DESCRIPTOR,])




_PAIRWISEMACROSYNTENYBLOCKSCOMPUTEREQUEST = _descriptor.Descriptor(
  name='PairwiseMacroSyntenyBlocksComputeRequest',
  full_name='gcv.services.PairwiseMacroSyntenyBlocksComputeRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='chromosome', full_name='gcv.services.PairwiseMacroSyntenyBlocksComputeRequest.chromosome', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='target', full_name='gcv.services.PairwiseMacroSyntenyBlocksComputeRequest.target', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='matched', full_name='gcv.services.PairwiseMacroSyntenyBlocksComputeRequest.matched', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='intermediate', full_name='gcv.services.PairwiseMacroSyntenyBlocksComputeRequest.intermediate', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='mask', full_name='gcv.services.PairwiseMacroSyntenyBlocksComputeRequest.mask', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='optionalMetrics', full_name='gcv.services.PairwiseMacroSyntenyBlocksComputeRequest.optionalMetrics', index=5,
      number=6, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='_mask', full_name='gcv.services.PairwiseMacroSyntenyBlocksComputeRequest._mask',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=84,
  serialized_end=254,
)


_PAIRWISEMACROSYNTENYBLOCKSCOMPUTEREPLY = _descriptor.Descriptor(
  name='PairwiseMacroSyntenyBlocksComputeReply',
  full_name='gcv.services.PairwiseMacroSyntenyBlocksComputeReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='blocks', full_name='gcv.services.PairwiseMacroSyntenyBlocksComputeReply.blocks', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=256,
  serialized_end=335,
)

_PAIRWISEMACROSYNTENYBLOCKSCOMPUTEREQUEST.oneofs_by_name['_mask'].fields.append(
  _PAIRWISEMACROSYNTENYBLOCKSCOMPUTEREQUEST.fields_by_name['mask'])
_PAIRWISEMACROSYNTENYBLOCKSCOMPUTEREQUEST.fields_by_name['mask'].containing_oneof = _PAIRWISEMACROSYNTENYBLOCKSCOMPUTEREQUEST.oneofs_by_name['_mask']
_PAIRWISEMACROSYNTENYBLOCKSCOMPUTEREPLY.fields_by_name['blocks'].message_type = structures_dot_block__pb2._BLOCK
DESCRIPTOR.message_types_by_name['PairwiseMacroSyntenyBlocksComputeRequest'] = _PAIRWISEMACROSYNTENYBLOCKSCOMPUTEREQUEST
DESCRIPTOR.message_types_by_name['PairwiseMacroSyntenyBlocksComputeReply'] = _PAIRWISEMACROSYNTENYBLOCKSCOMPUTEREPLY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PairwiseMacroSyntenyBlocksComputeRequest = _reflection.GeneratedProtocolMessageType('PairwiseMacroSyntenyBlocksComputeRequest', (_message.Message,), {
  'DESCRIPTOR' : _PAIRWISEMACROSYNTENYBLOCKSCOMPUTEREQUEST,
  '__module__' : 'services.pairwisemacrosyntenyblocks_pb2'
  # @@protoc_insertion_point(class_scope:gcv.services.PairwiseMacroSyntenyBlocksComputeRequest)
  })
_sym_db.RegisterMessage(PairwiseMacroSyntenyBlocksComputeRequest)

PairwiseMacroSyntenyBlocksComputeReply = _reflection.GeneratedProtocolMessageType('PairwiseMacroSyntenyBlocksComputeReply', (_message.Message,), {
  'DESCRIPTOR' : _PAIRWISEMACROSYNTENYBLOCKSCOMPUTEREPLY,
  '__module__' : 'services.pairwisemacrosyntenyblocks_pb2'
  # @@protoc_insertion_point(class_scope:gcv.services.PairwiseMacroSyntenyBlocksComputeReply)
  })
_sym_db.RegisterMessage(PairwiseMacroSyntenyBlocksComputeReply)



_PAIRWISEMACROSYNTENYBLOCKS = _descriptor.ServiceDescriptor(
  name='PairwiseMacroSyntenyBlocks',
  full_name='gcv.services.PairwiseMacroSyntenyBlocks',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=338,
  serialized_end=489,
  methods=[
  _descriptor.MethodDescriptor(
    name='Compute',
    full_name='gcv.services.PairwiseMacroSyntenyBlocks.Compute',
    index=0,
    containing_service=None,
    input_type=_PAIRWISEMACROSYNTENYBLOCKSCOMPUTEREQUEST,
    output_type=_PAIRWISEMACROSYNTENYBLOCKSCOMPUTEREPLY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_PAIRWISEMACROSYNTENYBLOCKS)

DESCRIPTOR.services_by_name['PairwiseMacroSyntenyBlocks'] = _PAIRWISEMACROSYNTENYBLOCKS

# @@protoc_insertion_point(module_scope)