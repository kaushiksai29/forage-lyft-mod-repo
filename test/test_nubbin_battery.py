import unittest
from datetime import date

from battery.nubbin_battery import NubbinBattery

class TestNubbinBattery(unittest.TestCase):
    def test_needs_service_true(self):
        current_date = date.fromisoformat("2022-09-15")
        last_service_date = date.fromisoformat("2018-05-04")
        battery = NubbinBattery(last_service_date, current_date)
        self.assertTrue(battery.needs_service())

    def test_needs_service_false(self):
        current_date = date.fromisoformat("2022-09-15")
        last_service_date = date.fromisoformat("2021-07-23")
        battery = NubbinBattery(last_service_date, current_date)
        self.assertTrue(battery.needs_service())