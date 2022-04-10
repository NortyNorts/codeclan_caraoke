
from classes.guest import Guest


class Room():
    def __init__(self,name, entry_fee):
        self.name = name
        self.guests_in_room = ["Mark", "Steve", "Emilie", "Jon", "Dan"]
        self.songs_in_room = ["song_1", "song_2", "song_3", "song_4","song_5"]
        self.entry_fee = entry_fee
        self.till = 0

    def number_of_guests_in_room(self):
        return len(self.guests_in_room)

    def add_guest_to_room(self, name):
        if len(self.guests_in_room) >= 10:
            print("Sorry Betty, the room is full")
        elif name.wallet < self.entry_fee:
            print("Do you have another way to pay?")
        else:
            self.guests_in_room.append(name)
            self.till += self.entry_fee
            name.wallet -= self.entry_fee
    
    def remove_guest_from_room(self, name):
        self.guests_in_room.remove(name)

    def number_of_songs_in_room(self):
        return len(self.songs_in_room)

    def add_song_to_room(self, song_name):
        self.songs_in_room.append(song_name)
    
    def remove_song_from_room(self, name):
        self.songs_in_room.remove(name)

    def favourite_song(self, name):
        if name.favourite_song == name:
            print("WooHoo!! This is my favourite song!")