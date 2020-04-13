from AbstractPowerCalculator import AbstractPowerCalculator


class MinouraB60Level3Calculator(AbstractPowerCalculator):
    def __init__(self):
        super(MinouraB60Level3Calculator, self).__init__()
	# default value - can be overridden in config.py; Continental Trainer Tire - 2.122
	# 700 x 23C - 2.097
	# 700 x 25C - 2.105
        self.wheel_circumference = 2.105

    A = 0.000480
    B = 0.050536
    C = 7.613403
    D = 3.233333

    # Derived Minoura Power Curve from http://www.powercurvesensor.com/cycling-trainer-power-curves/
    # This is a 3rd order polynomial, where
    # Power = A * v ^ 3 + B * v ^ 2 + C * v + d
    # where v is speed in km/hour and constants A, B, C & D are as defined above.
    def power_from_speed(self, revs_per_sec):
        if self._DEBUG: print "power_from_speed"

        km_per_rev = self.wheel_circumference 
        kph = revs_per_sec * 3600 * km_per_rev
        power = self.correction_factor * (self.A * kph * kph * kph +
                                          self.B * kph * kph +
                                          self.C * kph +
                                          self.D)
        return power

    def set_wheel_circumference(self, circumference):
        self.wheel_circumference = circumference