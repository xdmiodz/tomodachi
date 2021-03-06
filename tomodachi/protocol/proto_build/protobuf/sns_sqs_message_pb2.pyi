# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
    FileDescriptor as google___protobuf___descriptor___FileDescriptor,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from typing import (
    Optional as typing___Optional,
    Text as typing___Text,
    Union as typing___Union,
)

from typing_extensions import (
    Literal as typing_extensions___Literal,
)


builtin___bool = bool
builtin___bytes = bytes
builtin___float = float
builtin___int = int
if sys.version_info < (3,):
    builtin___buffer = buffer
    builtin___unicode = unicode


DESCRIPTOR: google___protobuf___descriptor___FileDescriptor = ...

class Service(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    name: typing___Text = ...
    uuid: typing___Text = ...

    def __init__(self,
        *,
        name : typing___Optional[typing___Text] = None,
        uuid : typing___Optional[typing___Text] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> Service: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> Service: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"name",b"name",u"uuid",b"uuid"]) -> None: ...
type___Service = Service

class Metadata(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    message_uuid: typing___Text = ...
    protocol_version: typing___Text = ...
    timestamp: builtin___float = ...
    topic: typing___Text = ...
    data_encoding: typing___Text = ...

    def __init__(self,
        *,
        message_uuid : typing___Optional[typing___Text] = None,
        protocol_version : typing___Optional[typing___Text] = None,
        timestamp : typing___Optional[builtin___float] = None,
        topic : typing___Optional[typing___Text] = None,
        data_encoding : typing___Optional[typing___Text] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> Metadata: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> Metadata: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"data_encoding",b"data_encoding",u"message_uuid",b"message_uuid",u"protocol_version",b"protocol_version",u"timestamp",b"timestamp",u"topic",b"topic"]) -> None: ...
type___Metadata = Metadata

class SNSSQSMessage(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    data: builtin___bytes = ...

    @property
    def service(self) -> type___Service: ...

    @property
    def metadata(self) -> type___Metadata: ...

    def __init__(self,
        *,
        service : typing___Optional[type___Service] = None,
        metadata : typing___Optional[type___Metadata] = None,
        data : typing___Optional[builtin___bytes] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> SNSSQSMessage: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> SNSSQSMessage: ...
    def HasField(self, field_name: typing_extensions___Literal[u"metadata",b"metadata",u"service",b"service"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"data",b"data",u"metadata",b"metadata",u"service",b"service"]) -> None: ...
type___SNSSQSMessage = SNSSQSMessage
