# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: service_msg.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import common_pb2 as common__pb2
import schema_pb2 as schema__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='service_msg.proto',
  package='milvus.proto.service',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x11service_msg.proto\x12\x14milvus.proto.service\x1a\x0c\x63ommon.proto\x1a\x0cschema.proto\")\n\x0e\x43ollectionName\x12\x17\n\x0f\x63ollection_name\x18\x01 \x01(\t\"5\n\rPartitionName\x12\x17\n\x0f\x63ollection_name\x18\x01 \x01(\t\x12\x0b\n\x03tag\x18\x02 \x01(\t\"|\n\x08RowBatch\x12\x17\n\x0f\x63ollection_name\x18\x01 \x01(\t\x12\x15\n\rpartition_tag\x18\x02 \x01(\t\x12+\n\x08row_data\x18\x03 \x03(\x0b\x32\x19.milvus.proto.common.Blob\x12\x13\n\x0bhash_values\x18\x04 \x03(\x05\"I\n\x10PlaceholderValue\x12\x0b\n\x03tag\x18\x01 \x01(\t\x12(\n\x05value\x18\x02 \x01(\x0b\x32\x19.milvus.proto.common.Blob\"\x83\x01\n\x05Query\x12\x17\n\x0f\x63ollection_name\x18\x01 \x01(\t\x12\x16\n\x0epartition_tags\x18\x02 \x03(\t\x12\x0b\n\x03\x64sl\x18\x03 \x01(\t\x12<\n\x0cplaceholders\x18\x04 \x03(\x0b\x32&.milvus.proto.service.PlaceholderValue\"L\n\x0eStringResponse\x12+\n\x06status\x18\x01 \x01(\x0b\x32\x1b.milvus.proto.common.Status\x12\r\n\x05value\x18\x02 \x01(\t\"J\n\x0c\x42oolResponse\x12+\n\x06status\x18\x01 \x01(\x0b\x32\x1b.milvus.proto.common.Status\x12\r\n\x05value\x18\x02 \x01(\x08\"Q\n\x12StringListResponse\x12+\n\x06status\x18\x01 \x01(\x0b\x32\x1b.milvus.proto.common.Status\x12\x0e\n\x06values\x18\x02 \x03(\t\"R\n\x13IntegerListResponse\x12+\n\x06status\x18\x01 \x01(\x0b\x32\x1b.milvus.proto.common.Status\x12\x0e\n\x06values\x18\x02 \x03(\x03\"_\n\x14IntegerRangeResponse\x12+\n\x06status\x18\x01 \x01(\x0b\x32\x1b.milvus.proto.common.Status\x12\r\n\x05\x62\x65gin\x18\x02 \x03(\x03\x12\x0b\n\x03\x65nd\x18\x03 \x03(\x03\"\xb2\x01\n\x15\x43ollectionDescription\x12+\n\x06status\x18\x01 \x01(\x0b\x32\x1b.milvus.proto.common.Status\x12\x35\n\x06schema\x18\x02 \x01(\x0b\x32%.milvus.proto.schema.CollectionSchema\x12\x35\n\nstatistics\x18\x03 \x03(\x0b\x32!.milvus.proto.common.KeyValuePair\"\xad\x01\n\x14PartitionDescription\x12+\n\x06status\x18\x01 \x01(\x0b\x32\x1b.milvus.proto.common.Status\x12\x31\n\x04name\x18\x02 \x01(\x0b\x32#.milvus.proto.service.PartitionName\x12\x35\n\nstatistics\x18\x03 \x03(\x0b\x32!.milvus.proto.common.KeyValuePair\"$\n\x05Score\x12\x0b\n\x03tag\x18\x01 \x01(\t\x12\x0e\n\x06values\x18\x02 \x03(\x02\"m\n\x04Hits\x12\x0b\n\x03ids\x18\x01 \x03(\x03\x12+\n\x08row_data\x18\x02 \x03(\x0b\x32\x19.milvus.proto.common.Blob\x12+\n\x06scores\x18\x03 \x03(\x0b\x32\x1b.milvus.proto.service.Score\"d\n\x0bQueryResult\x12+\n\x06status\x18\x01 \x01(\x0b\x32\x1b.milvus.proto.common.Status\x12(\n\x04hits\x18\x02 \x03(\x0b\x32\x1a.milvus.proto.service.Hitsb\x06proto3'
  ,
  dependencies=[common__pb2.DESCRIPTOR,schema__pb2.DESCRIPTOR,])




_COLLECTIONNAME = _descriptor.Descriptor(
  name='CollectionName',
  full_name='milvus.proto.service.CollectionName',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='collection_name', full_name='milvus.proto.service.CollectionName.collection_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=71,
  serialized_end=112,
)


_PARTITIONNAME = _descriptor.Descriptor(
  name='PartitionName',
  full_name='milvus.proto.service.PartitionName',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='collection_name', full_name='milvus.proto.service.PartitionName.collection_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='tag', full_name='milvus.proto.service.PartitionName.tag', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=114,
  serialized_end=167,
)


_ROWBATCH = _descriptor.Descriptor(
  name='RowBatch',
  full_name='milvus.proto.service.RowBatch',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='collection_name', full_name='milvus.proto.service.RowBatch.collection_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='partition_tag', full_name='milvus.proto.service.RowBatch.partition_tag', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='row_data', full_name='milvus.proto.service.RowBatch.row_data', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='hash_values', full_name='milvus.proto.service.RowBatch.hash_values', index=3,
      number=4, type=5, cpp_type=1, label=3,
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
  serialized_start=169,
  serialized_end=293,
)


_PLACEHOLDERVALUE = _descriptor.Descriptor(
  name='PlaceholderValue',
  full_name='milvus.proto.service.PlaceholderValue',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='tag', full_name='milvus.proto.service.PlaceholderValue.tag', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='milvus.proto.service.PlaceholderValue.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=295,
  serialized_end=368,
)


_QUERY = _descriptor.Descriptor(
  name='Query',
  full_name='milvus.proto.service.Query',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='collection_name', full_name='milvus.proto.service.Query.collection_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='partition_tags', full_name='milvus.proto.service.Query.partition_tags', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='dsl', full_name='milvus.proto.service.Query.dsl', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='placeholders', full_name='milvus.proto.service.Query.placeholders', index=3,
      number=4, type=11, cpp_type=10, label=3,
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
  serialized_start=371,
  serialized_end=502,
)


_STRINGRESPONSE = _descriptor.Descriptor(
  name='StringResponse',
  full_name='milvus.proto.service.StringResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='milvus.proto.service.StringResponse.status', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='milvus.proto.service.StringResponse.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=504,
  serialized_end=580,
)


_BOOLRESPONSE = _descriptor.Descriptor(
  name='BoolResponse',
  full_name='milvus.proto.service.BoolResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='milvus.proto.service.BoolResponse.status', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='milvus.proto.service.BoolResponse.value', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=582,
  serialized_end=656,
)


_STRINGLISTRESPONSE = _descriptor.Descriptor(
  name='StringListResponse',
  full_name='milvus.proto.service.StringListResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='milvus.proto.service.StringListResponse.status', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='values', full_name='milvus.proto.service.StringListResponse.values', index=1,
      number=2, type=9, cpp_type=9, label=3,
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
  serialized_start=658,
  serialized_end=739,
)


_INTEGERLISTRESPONSE = _descriptor.Descriptor(
  name='IntegerListResponse',
  full_name='milvus.proto.service.IntegerListResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='milvus.proto.service.IntegerListResponse.status', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='values', full_name='milvus.proto.service.IntegerListResponse.values', index=1,
      number=2, type=3, cpp_type=2, label=3,
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
  serialized_start=741,
  serialized_end=823,
)


_INTEGERRANGERESPONSE = _descriptor.Descriptor(
  name='IntegerRangeResponse',
  full_name='milvus.proto.service.IntegerRangeResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='milvus.proto.service.IntegerRangeResponse.status', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='begin', full_name='milvus.proto.service.IntegerRangeResponse.begin', index=1,
      number=2, type=3, cpp_type=2, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='end', full_name='milvus.proto.service.IntegerRangeResponse.end', index=2,
      number=3, type=3, cpp_type=2, label=3,
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
  serialized_start=825,
  serialized_end=920,
)


_COLLECTIONDESCRIPTION = _descriptor.Descriptor(
  name='CollectionDescription',
  full_name='milvus.proto.service.CollectionDescription',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='milvus.proto.service.CollectionDescription.status', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='schema', full_name='milvus.proto.service.CollectionDescription.schema', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='statistics', full_name='milvus.proto.service.CollectionDescription.statistics', index=2,
      number=3, type=11, cpp_type=10, label=3,
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
  serialized_start=923,
  serialized_end=1101,
)


_PARTITIONDESCRIPTION = _descriptor.Descriptor(
  name='PartitionDescription',
  full_name='milvus.proto.service.PartitionDescription',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='milvus.proto.service.PartitionDescription.status', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='milvus.proto.service.PartitionDescription.name', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='statistics', full_name='milvus.proto.service.PartitionDescription.statistics', index=2,
      number=3, type=11, cpp_type=10, label=3,
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
  serialized_start=1104,
  serialized_end=1277,
)


_SCORE = _descriptor.Descriptor(
  name='Score',
  full_name='milvus.proto.service.Score',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='tag', full_name='milvus.proto.service.Score.tag', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='values', full_name='milvus.proto.service.Score.values', index=1,
      number=2, type=2, cpp_type=6, label=3,
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
  serialized_start=1279,
  serialized_end=1315,
)


_HITS = _descriptor.Descriptor(
  name='Hits',
  full_name='milvus.proto.service.Hits',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='ids', full_name='milvus.proto.service.Hits.ids', index=0,
      number=1, type=3, cpp_type=2, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='row_data', full_name='milvus.proto.service.Hits.row_data', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='scores', full_name='milvus.proto.service.Hits.scores', index=2,
      number=3, type=11, cpp_type=10, label=3,
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
  serialized_start=1317,
  serialized_end=1426,
)


_QUERYRESULT = _descriptor.Descriptor(
  name='QueryResult',
  full_name='milvus.proto.service.QueryResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='milvus.proto.service.QueryResult.status', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='hits', full_name='milvus.proto.service.QueryResult.hits', index=1,
      number=2, type=11, cpp_type=10, label=3,
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
  serialized_start=1428,
  serialized_end=1528,
)

_ROWBATCH.fields_by_name['row_data'].message_type = common__pb2._BLOB
_PLACEHOLDERVALUE.fields_by_name['value'].message_type = common__pb2._BLOB
_QUERY.fields_by_name['placeholders'].message_type = _PLACEHOLDERVALUE
_STRINGRESPONSE.fields_by_name['status'].message_type = common__pb2._STATUS
_BOOLRESPONSE.fields_by_name['status'].message_type = common__pb2._STATUS
_STRINGLISTRESPONSE.fields_by_name['status'].message_type = common__pb2._STATUS
_INTEGERLISTRESPONSE.fields_by_name['status'].message_type = common__pb2._STATUS
_INTEGERRANGERESPONSE.fields_by_name['status'].message_type = common__pb2._STATUS
_COLLECTIONDESCRIPTION.fields_by_name['status'].message_type = common__pb2._STATUS
_COLLECTIONDESCRIPTION.fields_by_name['schema'].message_type = schema__pb2._COLLECTIONSCHEMA
_COLLECTIONDESCRIPTION.fields_by_name['statistics'].message_type = common__pb2._KEYVALUEPAIR
_PARTITIONDESCRIPTION.fields_by_name['status'].message_type = common__pb2._STATUS
_PARTITIONDESCRIPTION.fields_by_name['name'].message_type = _PARTITIONNAME
_PARTITIONDESCRIPTION.fields_by_name['statistics'].message_type = common__pb2._KEYVALUEPAIR
_HITS.fields_by_name['row_data'].message_type = common__pb2._BLOB
_HITS.fields_by_name['scores'].message_type = _SCORE
_QUERYRESULT.fields_by_name['status'].message_type = common__pb2._STATUS
_QUERYRESULT.fields_by_name['hits'].message_type = _HITS
DESCRIPTOR.message_types_by_name['CollectionName'] = _COLLECTIONNAME
DESCRIPTOR.message_types_by_name['PartitionName'] = _PARTITIONNAME
DESCRIPTOR.message_types_by_name['RowBatch'] = _ROWBATCH
DESCRIPTOR.message_types_by_name['PlaceholderValue'] = _PLACEHOLDERVALUE
DESCRIPTOR.message_types_by_name['Query'] = _QUERY
DESCRIPTOR.message_types_by_name['StringResponse'] = _STRINGRESPONSE
DESCRIPTOR.message_types_by_name['BoolResponse'] = _BOOLRESPONSE
DESCRIPTOR.message_types_by_name['StringListResponse'] = _STRINGLISTRESPONSE
DESCRIPTOR.message_types_by_name['IntegerListResponse'] = _INTEGERLISTRESPONSE
DESCRIPTOR.message_types_by_name['IntegerRangeResponse'] = _INTEGERRANGERESPONSE
DESCRIPTOR.message_types_by_name['CollectionDescription'] = _COLLECTIONDESCRIPTION
DESCRIPTOR.message_types_by_name['PartitionDescription'] = _PARTITIONDESCRIPTION
DESCRIPTOR.message_types_by_name['Score'] = _SCORE
DESCRIPTOR.message_types_by_name['Hits'] = _HITS
DESCRIPTOR.message_types_by_name['QueryResult'] = _QUERYRESULT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CollectionName = _reflection.GeneratedProtocolMessageType('CollectionName', (_message.Message,), {
  'DESCRIPTOR' : _COLLECTIONNAME,
  '__module__' : 'service_msg_pb2'
  # @@protoc_insertion_point(class_scope:milvus.proto.service.CollectionName)
  })
_sym_db.RegisterMessage(CollectionName)

PartitionName = _reflection.GeneratedProtocolMessageType('PartitionName', (_message.Message,), {
  'DESCRIPTOR' : _PARTITIONNAME,
  '__module__' : 'service_msg_pb2'
  # @@protoc_insertion_point(class_scope:milvus.proto.service.PartitionName)
  })
_sym_db.RegisterMessage(PartitionName)

RowBatch = _reflection.GeneratedProtocolMessageType('RowBatch', (_message.Message,), {
  'DESCRIPTOR' : _ROWBATCH,
  '__module__' : 'service_msg_pb2'
  # @@protoc_insertion_point(class_scope:milvus.proto.service.RowBatch)
  })
_sym_db.RegisterMessage(RowBatch)

PlaceholderValue = _reflection.GeneratedProtocolMessageType('PlaceholderValue', (_message.Message,), {
  'DESCRIPTOR' : _PLACEHOLDERVALUE,
  '__module__' : 'service_msg_pb2'
  # @@protoc_insertion_point(class_scope:milvus.proto.service.PlaceholderValue)
  })
_sym_db.RegisterMessage(PlaceholderValue)

Query = _reflection.GeneratedProtocolMessageType('Query', (_message.Message,), {
  'DESCRIPTOR' : _QUERY,
  '__module__' : 'service_msg_pb2'
  # @@protoc_insertion_point(class_scope:milvus.proto.service.Query)
  })
_sym_db.RegisterMessage(Query)

StringResponse = _reflection.GeneratedProtocolMessageType('StringResponse', (_message.Message,), {
  'DESCRIPTOR' : _STRINGRESPONSE,
  '__module__' : 'service_msg_pb2'
  # @@protoc_insertion_point(class_scope:milvus.proto.service.StringResponse)
  })
_sym_db.RegisterMessage(StringResponse)

BoolResponse = _reflection.GeneratedProtocolMessageType('BoolResponse', (_message.Message,), {
  'DESCRIPTOR' : _BOOLRESPONSE,
  '__module__' : 'service_msg_pb2'
  # @@protoc_insertion_point(class_scope:milvus.proto.service.BoolResponse)
  })
_sym_db.RegisterMessage(BoolResponse)

StringListResponse = _reflection.GeneratedProtocolMessageType('StringListResponse', (_message.Message,), {
  'DESCRIPTOR' : _STRINGLISTRESPONSE,
  '__module__' : 'service_msg_pb2'
  # @@protoc_insertion_point(class_scope:milvus.proto.service.StringListResponse)
  })
_sym_db.RegisterMessage(StringListResponse)

IntegerListResponse = _reflection.GeneratedProtocolMessageType('IntegerListResponse', (_message.Message,), {
  'DESCRIPTOR' : _INTEGERLISTRESPONSE,
  '__module__' : 'service_msg_pb2'
  # @@protoc_insertion_point(class_scope:milvus.proto.service.IntegerListResponse)
  })
_sym_db.RegisterMessage(IntegerListResponse)

IntegerRangeResponse = _reflection.GeneratedProtocolMessageType('IntegerRangeResponse', (_message.Message,), {
  'DESCRIPTOR' : _INTEGERRANGERESPONSE,
  '__module__' : 'service_msg_pb2'
  # @@protoc_insertion_point(class_scope:milvus.proto.service.IntegerRangeResponse)
  })
_sym_db.RegisterMessage(IntegerRangeResponse)

CollectionDescription = _reflection.GeneratedProtocolMessageType('CollectionDescription', (_message.Message,), {
  'DESCRIPTOR' : _COLLECTIONDESCRIPTION,
  '__module__' : 'service_msg_pb2'
  # @@protoc_insertion_point(class_scope:milvus.proto.service.CollectionDescription)
  })
_sym_db.RegisterMessage(CollectionDescription)

PartitionDescription = _reflection.GeneratedProtocolMessageType('PartitionDescription', (_message.Message,), {
  'DESCRIPTOR' : _PARTITIONDESCRIPTION,
  '__module__' : 'service_msg_pb2'
  # @@protoc_insertion_point(class_scope:milvus.proto.service.PartitionDescription)
  })
_sym_db.RegisterMessage(PartitionDescription)

Score = _reflection.GeneratedProtocolMessageType('Score', (_message.Message,), {
  'DESCRIPTOR' : _SCORE,
  '__module__' : 'service_msg_pb2'
  # @@protoc_insertion_point(class_scope:milvus.proto.service.Score)
  })
_sym_db.RegisterMessage(Score)

Hits = _reflection.GeneratedProtocolMessageType('Hits', (_message.Message,), {
  'DESCRIPTOR' : _HITS,
  '__module__' : 'service_msg_pb2'
  # @@protoc_insertion_point(class_scope:milvus.proto.service.Hits)
  })
_sym_db.RegisterMessage(Hits)

QueryResult = _reflection.GeneratedProtocolMessageType('QueryResult', (_message.Message,), {
  'DESCRIPTOR' : _QUERYRESULT,
  '__module__' : 'service_msg_pb2'
  # @@protoc_insertion_point(class_scope:milvus.proto.service.QueryResult)
  })
_sym_db.RegisterMessage(QueryResult)


# @@protoc_insertion_point(module_scope)