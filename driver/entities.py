import abc
from abc import ABC
from dataclasses import dataclass


@dataclass
class PortRequest(ABC):
    cmd: str
    payload: object


@dataclass
class PortResponse(ABC):
    payload: object


class PortResponseError(PortResponse):
    code: int
    msg: str = None


class PortHandler(ABC):
    @abc.abstractmethod
    def handle(self, request: PortRequest) -> PortResponse:
        ...

    @abc.abstractmethod
    def validate(self, request: PortRequest):
        ...
