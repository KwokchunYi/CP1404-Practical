from prac_09.taxi import Taxi


class SilverServiceTaxi(Taxi):
    flagfall = 4.50

    def __init__(self, name, fuel, fanciness):
        super().__init__(name, fuel)
        self.price_per_km *= fanciness

    def __str__(self):
        return f"{super().__str__()}plus flagfall of ${self.flagfall:.2f}"

    def get_fare(self):
        return f"{super(SilverServiceTaxi, self).get_fare() + self.flagfall:.2f}"