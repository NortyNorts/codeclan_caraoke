
class Room():
    def __init__(self,name):
        self.name = name
        self.guests_in_room = ["Mark", "Steve", "Emilie", "Jon", "Dan"]
        self.songs_in_room = ["song_1", "song_2", "song_3", "song_4","song_5"]

    def number_of_guests_in_room(self):
        return len(self.guests_in_room)

    def add_guest_to_room(self, name):
        self.guests_in_room.append(name)
    
    def remove_guest_from_room(self, name):
        self.guests_in_room.remove(name)

    def number_of_songs_in_room(self):
        return len(self.songs_in_room)

    def add_song_to_room(self, name):
        self.songs_in_room.append(name)
    
    def remove_song_from_room(self, name):
        self.songs_in_room.remove(name)