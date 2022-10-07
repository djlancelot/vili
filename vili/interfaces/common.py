import logging
from sqlite3 import Timestamp
import string
from typing import AnyStr, List

class Registerable:
    _id: string

class Controllable(Registerable):

    def do(self, parameters: dict):
        raise RuntimeError("TODO")
        
class WemoLight(Controllable):
    _id = "wemo"

class UDMXLight(Controllable):
    _id = "udmx"

class DummyControllable(Controllable):
    _id = "dummy"
    
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
    _id = "timer"

class WyzeTrigger(Trigger):
    _id = "wyze"

class DummyTrigger(Trigger):
    _id = "dummy"

    def __init__(self, parameters):
        self.parameters = parameters
