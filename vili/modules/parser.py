import logging
import yaml

from vili.interfaces.registry import initOutput
from .constants import \
    input_key, \
    output_key, \
    sequence_key, \
    device_type, \
    device_params

def readFile(filePath: str):
    with open(filePath, "r") as file:
        content = file.read()
    return content

def readYaml(content: str):
    return yaml.load(content, Loader=yaml.CSafeLoader)

def getOutputs(config: dict):
    outputs = dict()
    out_conf = config.get(output_key, dict())
    for key, value in out_conf.items():
        try:
            controllable = initOutput(value[device_type], value[device_params])
            outputs[key] = controllable
        except KeyError as e:
            logging.error(f"{device_type} or {device_params} sections are malformed or missing.")
    return outputs

def getInputs(config: dict):
    config.get(input_key, dict())

def getSequence(config: dict):
    config.get(sequence_key, dict())

def parse(file: str):
    content = readFile(file)
    config = readYaml(content)
    controllables = getOutputs(config)
    triggers = getInputs(config)
    sequence = getSequence(config)
    return {
        "controllables": controllables,
        "triggers": triggers,
        "sequence": sequence,
        "config": config
    }