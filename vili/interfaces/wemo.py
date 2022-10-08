import logging
import pywemo
from .common import Controllable

"""
WemoLight controller

The module discovers all devices. 
You can turn on and off devices by either specifying their 
user friendly name or the device order in the list (it may change)

parameters:
 - name: Living room
   action: on
 - id: 0
   action: off
"""
class WemoLight(Controllable):
    id = "wemo"

    def __init__(self, parameters: dict) -> None:
        super().__init__()
        self.devices = pywemo.discover_devices()

    def _get_device_by_name(self, name: str):
        try:
            result = [device for device in self.devices if device.name == name][0]
        except IndexError:
            names = ",".join([device.name for device in self.devices])
            logging.warn(f"'{name}' can't be found in devices: {names} .")

    def _execute(self, device, action):
        if action == "on":
            device.on()
        elif action == "off":
            device.off()
        elif action == "toggle":
            device.toggle()

    
    def do(self, parameters: dict):
        for parameter in parameters:
            try:
                action = parameter["action"]
            except KeyError:
                logging.warn(f"No action specified in paramaters: {parameter}")
            if "name" in parameter:
                device = self._get_device_by_name(parameter["name"])
            elif "id" in parameter:
                try:
                    device = self.devices[int(parameter["id"])]
                except (TypeError, KeyError, IndexError):
                    logging.warn(f"{parameter['id']} should be a number in range {len(self.devices)}.")
            else:
                logging.warn("Device id or name not specified.")
                break
            self._execute(device, action)
        


    
