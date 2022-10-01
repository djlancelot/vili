from os import device_encoding
from sqlite3 import Timestamp
import string
from typing import AnyStr, List


class Controllable:
    id: string
    actions: dict

class WemoLight(Controllable):
    device

class UDMXLight(Controllable):
    device


class Action:
    controllable: Controllable
    parameters: dict

class Step:
    start_time: int
    action: Action

class Sequence:
    steps: List[Step]

class Trigger:
    id: AnyStr
    def listen():
        pass


