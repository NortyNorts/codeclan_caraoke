
import unittest

from classes.room import *
from classes.guest import *
from classes.song import*

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room_1 = Room("Main room", 10)
        self.room_2 = Room("VIP room", 20)
        self.guest_1 = Guest("Garry", "song_6", 20)
        self.guest_2 = Guest("Helen", "Song_7", 20)
        self.guest_3 = Guest("Bob", "Song_8", 10)
        self.guest_4 = Guest("Bill", "Song_9", 10)
        self.guest_5 = Guest("Dave", "Song_10", 20)
        self.guest_6 = Guest("Betty", "Song_11", 0)
        self.guest_in_room_1 = Guest("Mark", "song_1", 20)
        self.guest_in_room_2 = Guest("Steve", "song_2", 20)
        self.song_1 = Song("song_6")
        self.song_2 = Song("song_7")
        self.song_3 = Song("song_8")
        self.song_4 = Song("song_9")
        self.song_5 = Song("song_10")
        self.song_in_room_1 = Song("song_1")
        self.song_in_room_2 = Song("song_2")

    # @unittest.skip("Delete this line to run the test")
    def test_check_room_name(self):
        self.assertEqual("Main room", self.room_1.name)
    
    # @unittest.skip("Delete this line to run the test")
    def test_check_no_guests_in_room(self):
        self.assertEqual(5, self.room_1.number_of_guests_in_room())
    
    # @unittest.skip("Delete this line to run the test")
    def test_check_one_guest_in_room(self):
        self.room_1.add_guest_to_room(self.guest_1)
        self.assertEqual(6, self.room_1.number_of_guests_in_room()) 

    # @unittest.skip("Delete this line to run the test")
    def test_check_five_guests_added_to_room(self):
        self.room_1.add_guest_to_room(self.guest_1)
        self.room_1.add_guest_to_room(self.guest_2)
        self.room_1.add_guest_to_room(self.guest_3)
        self.room_1.add_guest_to_room(self.guest_4)
        self.room_1.add_guest_to_room(self.guest_5)
        self.room_1.add_guest_to_room(self.guest_6)
        
        self.assertEqual(10, self.room_1.number_of_guests_in_room())

    # @unittest.skip("Delete this line to run the test")
    def test_check_remove_one_guest_from_room(self):
        self.room_1.remove_guest_from_room(self.guest_in_room_1.name)
        self.room_1.remove_guest_from_room(self.guest_in_room_2.name)
        self.assertEqual(3, self.room_1.number_of_guests_in_room())

    # @unittest.skip("Delete this line to run the test")
    def test_check_no_songs_in_room(self):
        self.assertEqual(5, self.room_1.number_of_songs_in_room())
    
    # @unittest.skip("Delete this line to run the test")
    def test_add_one_song_to_room(self):
        self.room_1.add_song_to_room(self.song_1)
        self.assertEqual(6, self.room_1.number_of_songs_in_room()) 

    # @unittest.skip("Delete this line to run the test")
    def test_check_five_songs_added_to_room(self):
        self.room_1.add_song_to_room(self.guest_1.favourite_song)
        self.room_1.add_song_to_room(self.guest_2.favourite_song)
        self.room_1.add_song_to_room(self.guest_3.favourite_song)
        self.room_1.add_song_to_room(self.guest_4.favourite_song)
        self.room_1.add_song_to_room(self.guest_5.favourite_song)
        self.assertEqual(10, self.room_1.number_of_songs_in_room())

    # @unittest.skip("Delete this line to run the test")
    def test_check_remove_two_songs_from_room(self):
        self.room_1.remove_song_from_room(self.song_in_room_1.name)
        self.room_1.remove_song_from_room(self.song_in_room_2.name)
        self.assertEqual(3, self.room_1.number_of_songs_in_room())

    # @unittest.skip("Delete this line to run the test")
    def test_check_till_value(self):
        self.assertEqual(0, self.room_1.till)

    def test_check_in_and_charge(self):
        self.room_1.add_guest_to_room(self.guest_1)
        self.assertEqual(10, self.room_1.till)
        self.assertEqual(10, self.guest_1.wallet)

    def test_guest_cannot_afford_entry(self):
        self.room_2.add_guest_to_room(self.guest_3)

    def test_guest_favourite_song(self):
        self.room_1.add_song_to_room(self.song_1)
        self.room_1.favourite_song(self.guest_1)

