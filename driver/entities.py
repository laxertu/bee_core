import abc
from typing import List, Dict
from abc import ABC


class PortRequest(ABC):
    ...


class PortResponse(ABC):
    ...


class PortHandler(ABC):
    @abc.abstractmethod
    def handle(self, cmd: str, request: PortRequest) -> PortResponse:
        ...

    @abc.abstractmethod
    def validate(self, request: PortRequest):
        ...
