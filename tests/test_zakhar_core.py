import unittest
from zakhar_core import __version__
import zakhar_core

class Tests(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(sum([1, 2, 3]), 6, "Should be 6")

    def test_version(self):
        assert __version__ == '0.1.0'

    def test_reset(self):
        zakhar_core.devices.motors.dev.cmd(zakhar_core.devices.CMD_STOP)

if __name__ == "__main__":
    unittest.main()