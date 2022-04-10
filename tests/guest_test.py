
import unittest

from classes.guest import *

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest = Guest("Guest_1", "song_1", 10)

    # @unittest.skip("Delete this line to run the test")
    def test_check_guest_name(self):
        self.assertEqual("Guest_1", self.guest.name)

    def test_check_song_name(self):
        self.assertEqual("song_1", self.guest.favourite_song)

    def test_check_wallet(self):
        self.assertEqual(10, self.guest.wallet)
