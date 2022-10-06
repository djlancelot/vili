import logging
from msilib.schema import Control
from os import device_encoding
from sqlite3 import Timestamp
import string
from typing import AnyStr, List


class Controllable:
    id: string
    actions: dict

    def do(self, action: string, parameters: dict):
        try:
            self.actions[action](parameters)
        except KeyError:
            logging.error(f"{action} action is not supported by {self.__name__}")

    def register(self, action: str, function: function):
        self.actions[action] = function

class WemoLight(Controllable):
    pass

class UDMXLight(Controllable):
    pass

class DummyControllable(Controllable):
    
    def __init__(self, parameters: dict):
        self.parameters = parameters
        self.actions["print"]=print



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

class TimeTrigger(Trigger):
    pass

class WyzeTrigger(Trigger):
    pass