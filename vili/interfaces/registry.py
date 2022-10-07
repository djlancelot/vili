import logging
from typing import Set
from .common import Controllable, DummyControllable, DummyTrigger, Registerable, TimeTrigger, UDMXLight, WemoLight, WyzeTrigger

outputs = None
inputs = None

input_set = { WyzeTrigger, DummyTrigger, TimeTrigger }
output_set = { UDMXLight, WemoLight, DummyControllable }

def cache(things: Set[Registerable]):
    return { thing._id: thing for thing in things }

def getOutput(output: str):
    global outputs
    if outputs is None:
        outputs = cache(output_set)
    try:
        result = outputs[output]
    except KeyError:
        logging.error(f"{output} controllable is not registered.")
    return result

def getInput(input: str):
    global inputs
    if inputs is None:
        inputs = cache(input_set)
    try:
        result = inputs[input]
    except KeyError:
        logging.error(f"{input} trigger is not registered.")
    return result

def initInput(ctype: str, cparams: dict) -> Controllable:
    try:
        myclass = getInput(ctype)
        return myclass(cparams)
    except KeyError:
        logging.error(f"Input module does not exist for {ctype}.")
    except Exception as e:
        logging.error(f"Unknown error initializing {ctype} trigger.")
        logging.error(e)
    return myclass

def initOutput(ctype: str, cparams: dict) -> Controllable:
    try:
        myclass = getOutput(ctype)
        return myclass(cparams)
    except KeyError:
        logging.error(f"Output module does not exist for {ctype}.")
    except Exception as e:
        logging.error(f"Unknown error initializing {ctype} controllable.")
        logging.error(e)

