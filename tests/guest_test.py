
import unittest

from classes.guest import Guest

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest = Guest("Guest_1")

    # @unittest.skip("Delete this line to run the test")
    def test_check_guest_name(self):
        self.assertEqual("Guest_1", self.guest.name)