from .mower import Mower
from .sensor import Sensor
from .water_control import WaterControl
from .smart_irrigation_control import SmartIrrigationControl


class DeviceFactory:
    @staticmethod
    def build(self, smart_system, device_map):
        if "MOWER" in device_map:
            return Mower(smart_system, device_map)
        elif "SENSOR" in device_map:
            return Sensor(smart_system, device_map)
        elif "POWER_SOCKET" in device_map:
            pass
        elif "VALVE" in device_map:
            if len(device_map["VALVE"]) > 1:
                return SmartIrrigationControl(
                    smart_system, device_map
                )  # Smart irrigation control
            else:
                return WaterControl(smart_system, device_map)
