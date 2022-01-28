class ChargingBrick:
    def __init__(self, volts: float, amps: float):
        self._volts = volts # type: float
        self._amps = amps # type: float

    def __lt__(self, other: "ChargingBrick") -> bool:
        return self._volts * self._amps < other._volts * other._amps

    def __gt__(self, other: "ChargingBrick") -> bool:
        return self._volts * self._amps > other._volts * other._amps

    def __eq__(self, other: "ChargingBrick") -> bool:
        return not self > other and not self < other
