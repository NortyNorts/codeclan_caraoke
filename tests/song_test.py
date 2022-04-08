
import unittest

from classes.song import Song

class TestSong(unittest.TestCase):
    def setUp(self):
        self.song = Song("Song_1")

    # @unittest.skip("Delete this line to run the test")
    def test_check_song_name(self):
        self.assertEqual("Song_1", self.song.name)