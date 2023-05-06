import abc
from abc import ABC
from dataclasses import dataclass

@dataclass
class Dto:
    ...

@dataclass
class PortRequest(ABC):
    cmd: str
    payload: Dto


@dataclass
class PortResponse(ABC):
    payload: Dto


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
