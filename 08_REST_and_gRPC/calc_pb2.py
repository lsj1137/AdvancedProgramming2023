# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: calc.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\ncalc.proto\"\x1c\n\x0cHelloRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"\x1d\n\nHelloReply\x12\x0f\n\x07message\x18\x01 \x01(\t\".\n\x08Operands\x12\n\n\x02x1\x18\x01 \x01(\x02\x12\n\n\x02x2\x18\x02 \x01(\x02\x12\n\n\x02op\x18\x03 \x01(\t\"\x1c\n\nCalcResult\x12\x0e\n\x06result\x18\x01 \x01(\x02\x32T\n\nCalculator\x12&\n\x08SayHello\x12\r.HelloRequest\x1a\x0b.HelloReply\x12\x1e\n\x04\x43\x61lc\x12\t.Operands\x1a\x0b.CalcResultb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'calc_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_HELLOREQUEST']._serialized_start=14
  _globals['_HELLOREQUEST']._serialized_end=42
  _globals['_HELLOREPLY']._serialized_start=44
  _globals['_HELLOREPLY']._serialized_end=73
  _globals['_OPERANDS']._serialized_start=75
  _globals['_OPERANDS']._serialized_end=121
  _globals['_CALCRESULT']._serialized_start=123
  _globals['_CALCRESULT']._serialized_end=151
  _globals['_CALCULATOR']._serialized_start=153
  _globals['_CALCULATOR']._serialized_end=237
# @@protoc_insertion_point(module_scope)
