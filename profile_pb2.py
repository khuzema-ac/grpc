# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: profile.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rprofile.proto\x12\x07profile\"T\n\x07Profile\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07\x63ompany\x18\x02 \x01(\t\x12\x0b\n\x03ssn\x18\x03 \x01(\t\x12\x0f\n\x07\x61\x64\x64ress\x18\x04 \x01(\t\x12\x0c\n\x04mail\x18\x05 \x01(\t\";\n\x06Status\x12!\n\x07profile\x18\x01 \x01(\x0b\x32\x10.profile.Profile\x12\x0e\n\x06status\x18\x02 \x01(\t2I\n\x0eProfileService\x12\x37\n\x0csaveProfiles\x12\x10.profile.Profile\x1a\x0f.profile.Status\"\x00(\x01\x30\x01\x62\x06proto3')



_PROFILE = DESCRIPTOR.message_types_by_name['Profile']
_STATUS = DESCRIPTOR.message_types_by_name['Status']
Profile = _reflection.GeneratedProtocolMessageType('Profile', (_message.Message,), {
  'DESCRIPTOR' : _PROFILE,
  '__module__' : 'profile_pb2'
  # @@protoc_insertion_point(class_scope:profile.Profile)
  })
_sym_db.RegisterMessage(Profile)

Status = _reflection.GeneratedProtocolMessageType('Status', (_message.Message,), {
  'DESCRIPTOR' : _STATUS,
  '__module__' : 'profile_pb2'
  # @@protoc_insertion_point(class_scope:profile.Status)
  })
_sym_db.RegisterMessage(Status)

_PROFILESERVICE = DESCRIPTOR.services_by_name['ProfileService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _PROFILE._serialized_start=26
  _PROFILE._serialized_end=110
  _STATUS._serialized_start=112
  _STATUS._serialized_end=171
  _PROFILESERVICE._serialized_start=173
  _PROFILESERVICE._serialized_end=246
# @@protoc_insertion_point(module_scope)
