import logging
from .common import Controllable
import pyudmx

"""
UDMXLight will control UDMX compatible devices.
You can set multiple DMX channels to a value like the following:
        parameters:
        - ch: 0
          val: 255
        - ch: 1
          val: 255
"""
class UDMXLight(Controllable):
    id = "udmx"

    def __init__(self, parameters: dict) -> None:
        super().__init__()
        self.device = pyudmx.uDMXDevice()

    def do(self, parameters: dict):
        dev = self.device
        dev.open()
        for parameter in parameters:
            try:
                ch = parameter["ch"]
                val = parameter["val"]
                dev.send_single_value(ch, val)
            except Exception as e:
                logging.warn(e)
        dev.close()

