# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pairwisemacrosyntenyblocks.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pairwisemacrosyntenyblocks.proto',
  package='pairwisemacrosyntenyblocks',
  syntax='proto3',
  serialized_options=b'\n\"lis.gcv.pairwisemacrosyntenyblocksB\037PairwiseMacroSyntenyBlocksProtoP\001\242\002\002GS',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n pairwisemacrosyntenyblocks.proto\x12\x1apairwisemacrosyntenyblocks\"w\n\x0e\x43omputeRequest\x12\x12\n\nchromosome\x18\x01 \x03(\t\x12\x0e\n\x06target\x18\x02 \x01(\t\x12\x0f\n\x07matched\x18\x03 \x01(\r\x12\x14\n\x0cintermediate\x18\x04 \x01(\r\x12\x11\n\x04mask\x18\x05 \x01(\rH\x00\x88\x01\x01\x42\x07\n\x05_mask\"A\n\x0c\x43omputeReply\x12\x31\n\x06\x62locks\x18\x01 \x03(\x0b\x32!.pairwisemacrosyntenyblocks.Block\"N\n\x05\x42lock\x12\t\n\x01i\x18\x01 \x01(\r\x12\t\n\x01j\x18\x02 \x01(\r\x12\x0c\n\x04\x66min\x18\x03 \x01(\r\x12\x0c\n\x04\x66max\x18\x04 \x01(\r\x12\x13\n\x0borientation\x18\x05 \x01(\t2\x7f\n\x1aPairwiseMacroSyntenyBlocks\x12\x61\n\x07\x43ompute\x12*.pairwisemacrosyntenyblocks.ComputeRequest\x1a(.pairwisemacrosyntenyblocks.ComputeReply\"\x00\x42L\n\"lis.gcv.pairwisemacrosyntenyblocksB\x1fPairwiseMacroSyntenyBlocksProtoP\x01\xa2\x02\x02GSb\x06proto3'
)




_COMPUTEREQUEST = _descriptor.Descriptor(
  name='ComputeRequest',
  full_name='pairwisemacrosyntenyblocks.ComputeRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='chromosome', full_name='pairwisemacrosyntenyblocks.ComputeRequest.chromosome', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='target', full_name='pairwisemacrosyntenyblocks.ComputeRequest.target', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='matched', full_name='pairwisemacrosyntenyblocks.ComputeRequest.matched', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='intermediate', full_name='pairwisemacrosyntenyblocks.ComputeRequest.intermediate', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='mask', full_name='pairwisemacrosyntenyblocks.ComputeRequest.mask', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
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
      name='_mask', full_name='pairwisemacrosyntenyblocks.ComputeRequest._mask',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=64,
  serialized_end=183,
)


_COMPUTEREPLY = _descriptor.Descriptor(
  name='ComputeReply',
  full_name='pairwisemacrosyntenyblocks.ComputeReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='blocks', full_name='pairwisemacrosyntenyblocks.ComputeReply.blocks', index=0,
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
  serialized_start=185,
  serialized_end=250,
)


_BLOCK = _descriptor.Descriptor(
  name='Block',
  full_name='pairwisemacrosyntenyblocks.Block',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='i', full_name='pairwisemacrosyntenyblocks.Block.i', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='j', full_name='pairwisemacrosyntenyblocks.Block.j', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='fmin', full_name='pairwisemacrosyntenyblocks.Block.fmin', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='fmax', full_name='pairwisemacrosyntenyblocks.Block.fmax', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='orientation', full_name='pairwisemacrosyntenyblocks.Block.orientation', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=252,
  serialized_end=330,
)

_COMPUTEREQUEST.oneofs_by_name['_mask'].fields.append(
  _COMPUTEREQUEST.fields_by_name['mask'])
_COMPUTEREQUEST.fields_by_name['mask'].containing_oneof = _COMPUTEREQUEST.oneofs_by_name['_mask']
_COMPUTEREPLY.fields_by_name['blocks'].message_type = _BLOCK
DESCRIPTOR.message_types_by_name['ComputeRequest'] = _COMPUTEREQUEST
DESCRIPTOR.message_types_by_name['ComputeReply'] = _COMPUTEREPLY
DESCRIPTOR.message_types_by_name['Block'] = _BLOCK
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ComputeRequest = _reflection.GeneratedProtocolMessageType('ComputeRequest', (_message.Message,), {
  'DESCRIPTOR' : _COMPUTEREQUEST,
  '__module__' : 'pairwisemacrosyntenyblocks_pb2'
  # @@protoc_insertion_point(class_scope:pairwisemacrosyntenyblocks.ComputeRequest)
  })
_sym_db.RegisterMessage(ComputeRequest)

ComputeReply = _reflection.GeneratedProtocolMessageType('ComputeReply', (_message.Message,), {
  'DESCRIPTOR' : _COMPUTEREPLY,
  '__module__' : 'pairwisemacrosyntenyblocks_pb2'
  # @@protoc_insertion_point(class_scope:pairwisemacrosyntenyblocks.ComputeReply)
  })
_sym_db.RegisterMessage(ComputeReply)

Block = _reflection.GeneratedProtocolMessageType('Block', (_message.Message,), {
  'DESCRIPTOR' : _BLOCK,
  '__module__' : 'pairwisemacrosyntenyblocks_pb2'
  # @@protoc_insertion_point(class_scope:pairwisemacrosyntenyblocks.Block)
  })
_sym_db.RegisterMessage(Block)


DESCRIPTOR._options = None

_PAIRWISEMACROSYNTENYBLOCKS = _descriptor.ServiceDescriptor(
  name='PairwiseMacroSyntenyBlocks',
  full_name='pairwisemacrosyntenyblocks.PairwiseMacroSyntenyBlocks',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=332,
  serialized_end=459,
  methods=[
  _descriptor.MethodDescriptor(
    name='Compute',
    full_name='pairwisemacrosyntenyblocks.PairwiseMacroSyntenyBlocks.Compute',
    index=0,
    containing_service=None,
    input_type=_COMPUTEREQUEST,
    output_type=_COMPUTEREPLY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_PAIRWISEMACROSYNTENYBLOCKS)

DESCRIPTOR.services_by_name['PairwiseMacroSyntenyBlocks'] = _PAIRWISEMACROSYNTENYBLOCKS

# @@protoc_insertion_point(module_scope)
