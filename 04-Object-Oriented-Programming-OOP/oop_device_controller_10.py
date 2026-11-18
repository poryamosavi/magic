class BaseHardwareUnit_10:
    def __init__(self, unit_id: str, voltage: float = 3.3):
        self.unit_id = unit_id
        self.voltage = voltage
        self.active = False

    def activate(self) -> dict:
        self.active = True
        return {'unit': self.unit_id, 'status': 'ONLINE', 'voltage': self.voltage}

class SensorController_10(BaseHardwareUnit_10):
    def __init__(self, unit_id: str, gain: float = 2.0):
        super().__init__(unit_id)
        self.gain = gain

    def read_calibrated(self, raw: float) -> dict:
        return {'unit': self.unit_id, 'calibrated_value': round(raw * self.gain, 3)}

if __name__ == '__main__':
    ctrl = SensorController_10('NODE_10')
    print(ctrl.activate(), ctrl.read_calibrated(12.4))
