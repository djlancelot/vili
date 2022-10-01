import yaml
from .constants import input_key, output_key

def readFile(filePath: str):
    with open(filePath, "r") as file:
        content = file.read()
    return content

def readYaml(content: str):
    yaml.load(content)

def getOutputs(config: dict):
    config.get(output_key, dict())

def parse(file: str):
    content = readFile(file)
    config = readYaml(content)
    controllables = getOutputs(config)
