import logging
from regex import W
from .common import Controllable, UDMXLight, WemoLight

outputs = {
    'udmx': UDMXLight,
    'wemo': WemoLight
}

inputs = {
    'wyze' : None
}

def initOutput(ctype: str, cparams: dict) -> Controllable:
    return initClass(outputs, ctype, cparams)

def initInput(ctype: str, cparams: dict) -> Controllable:
    return initClass(inputs, ctype, cparams)

def initClass(deices: dict, ctype: str, cparams: dict):
    try:
        myclass = outputs[ctype]
        myclass(cparams)
    except KeyError:
        logging.error(f"Output module does not exist for {ctype}.")
    except Exception as e:
        logging.error(f"Unknown error initializing {ctype}.")
        logging.debug(e)

