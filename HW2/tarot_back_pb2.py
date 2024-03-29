# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tarot_back.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x10tarot_back.proto\"\x1c\n\nprocResult\x12\x0e\n\x06result\x18\x01 \x01(\t\"\x17\n\tidRequest\x12\n\n\x02id\x18\x01 \x01(\t\"&\n\x0cloginRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12\n\n\x02pw\x18\x02 \x01(\t\"5\n\rchngPwRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0b\n\x03pw1\x18\x02 \x01(\t\x12\x0b\n\x03pw2\x18\x03 \x01(\t\"R\n\x08infoData\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0e\n\x06gender\x18\x02 \x01(\t\x12\x0b\n\x03\x61ge\x18\x03 \x01(\x05\x12\x0b\n\x03job\x18\x04 \x01(\t\x12\x10\n\x08relation\x18\x05 \x01(\t\"1\n\x0b\x63\x61rdRequest\x12\n\n\x02n1\x18\x01 \x01(\x05\x12\n\n\x02n2\x18\x02 \x01(\x05\x12\n\n\x02n3\x18\x03 \x01(\x05\"M\n\x04\x63\x61rd\x12\t\n\x01n\x18\x01 \x01(\x05\x12\x0b\n\x03\x65ng\x18\x02 \x01(\t\x12\x0b\n\x03kor\x18\x03 \x01(\t\x12\x0f\n\x07meaning\x18\x04 \x01(\t\x12\x0f\n\x07reverse\x18\x05 \x01(\x05\"G\n\x0c\x63\x61rdResponse\x12\x11\n\x02\x63\x31\x18\x01 \x01(\x0b\x32\x05.card\x12\x11\n\x02\x63\x32\x18\x02 \x01(\x0b\x32\x05.card\x12\x11\n\x02\x63\x33\x18\x03 \x01(\x0b\x32\x05.card\"*\n\x0bsaveRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0f\n\x07\x63ontent\x18\x02 \x01(\t\"\'\n\x06record\x12\x0c\n\x04\x64\x61te\x18\x01 \x01(\t\x12\x0f\n\x07\x63ontent\x18\x02 \x01(\t\"(\n\x0ctarotRecords\x12\x18\n\x07records\x18\x01 \x03(\x0b\x32\x07.record2\x92\x02\n\x0binfoManager\x12\"\n\x07\x43hkInfo\x12\n.idRequest\x1a\x0b.procResult\x12!\n\x07SetInfo\x12\t.infoData\x1a\x0b.procResult\x12 \n\x07GetInfo\x12\n.idRequest\x1a\t.infoData\x12$\n\x06SignUp\x12\r.loginRequest\x1a\x0b.procResult\x12#\n\x05LogIn\x12\r.loginRequest\x1a\x0b.procResult\x12%\n\x06\x43hngPw\x12\x0e.chngPwRequest\x1a\x0b.procResult\x12(\n\nDelAccount\x12\r.loginRequest\x1a\x0b.procResult2\x86\x01\n\x0bTarotPlayer\x12\'\n\x08GetCards\x12\x0c.cardRequest\x1a\r.cardResponse\x12&\n\tSaveTarot\x12\x0c.saveRequest\x1a\x0b.procResult\x12&\n\tLoadTarot\x12\n.idRequest\x1a\r.tarotRecordsb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'tarot_back_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_PROCRESULT']._serialized_start=20
  _globals['_PROCRESULT']._serialized_end=48
  _globals['_IDREQUEST']._serialized_start=50
  _globals['_IDREQUEST']._serialized_end=73
  _globals['_LOGINREQUEST']._serialized_start=75
  _globals['_LOGINREQUEST']._serialized_end=113
  _globals['_CHNGPWREQUEST']._serialized_start=115
  _globals['_CHNGPWREQUEST']._serialized_end=168
  _globals['_INFODATA']._serialized_start=170
  _globals['_INFODATA']._serialized_end=252
  _globals['_CARDREQUEST']._serialized_start=254
  _globals['_CARDREQUEST']._serialized_end=303
  _globals['_CARD']._serialized_start=305
  _globals['_CARD']._serialized_end=382
  _globals['_CARDRESPONSE']._serialized_start=384
  _globals['_CARDRESPONSE']._serialized_end=455
  _globals['_SAVEREQUEST']._serialized_start=457
  _globals['_SAVEREQUEST']._serialized_end=499
  _globals['_RECORD']._serialized_start=501
  _globals['_RECORD']._serialized_end=540
  _globals['_TAROTRECORDS']._serialized_start=542
  _globals['_TAROTRECORDS']._serialized_end=582
  _globals['_INFOMANAGER']._serialized_start=585
  _globals['_INFOMANAGER']._serialized_end=859
  _globals['_TAROTPLAYER']._serialized_start=862
  _globals['_TAROTPLAYER']._serialized_end=996
# @@protoc_insertion_point(module_scope)
