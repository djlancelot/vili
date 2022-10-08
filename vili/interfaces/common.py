import logging
from sqlite3 import Timestamp
import string
from typing import AnyStr, List

class Registerable:
    id: string

class Controllable(Registerable):

    def do(self, parameters: dict):
        raise RuntimeError("TODO")

class DummyControllable(Controllable):
    id = "dummy"
    
    def __init__(self, parameters: dict):
        self.parameters = parameters

    def do(self, parameters: dict):
        print(parameters)

class Action:
    controllable: Controllable
    parameters: dict

class Step:
    start_time: int
    action: Action

class Sequence:
    steps: List[Step]

class Trigger(Registerable):
    def listen():
        pass

class TimeTrigger(Trigger):
    id = "timer"

class WyzeTrigger(Trigger):
    id = "wyze"

class DummyTrigger(Trigger):
    id = "dummy"

    def __init__(self, parameters):
        self.parameters = parameters
