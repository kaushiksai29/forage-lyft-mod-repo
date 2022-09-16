import unittest
from datetime import date

from battery.spindler_battery import SpindlerBattery

class TestSpindlerBattery(unittest.TestCase):
    def test_needs_service_true(self):
        current_date = date.fromisoformat("2022-09-15")
        last_service_date = date.fromisoformat("2019-03-24")
        battery = SpindlerBattery(last_service_date, current_date)
        self.assertTrue(battery.needs_service())

    def test_needs_service_false(self):
        current_date = date.fromisoformat("2022-09-15")
        last_service_date = date.fromisoformat("2021-09-22")
        battery = SpindlerBattery(last_service_date, current_date)
        self.assertTrue(battery.needs_service())