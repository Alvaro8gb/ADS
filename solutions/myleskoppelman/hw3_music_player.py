import sys
sys.path.append(".")

from ads_libs.io_parse import convert_file_to_commands
from collections import deque


class IPud:
    def __init__(self):
        self.songs = {} # O(1) for most operations
        self.playlist = deque() # O(1) except for search
        self.playlist_songs = set() # Used for search, for which its O(1)
        self.recents = deque() 
        self.total_time = 0
    
    def addSong(self, song: str, artist: str, duration: int): # O(1)
        if song in self.songs:
            raise ValueError
        self.songs[song]= {'artist': artist, 'duration': duration}
        return
        
    def addToPlaylist(self, song: str): # O(1)
        if song in self.playlist_songs:
            return
        if song not in self.songs:
            raise ValueError
        
        self.playlist.append(song)
        self.playlist_songs.add(song)
        self.total_time += self.songs[song]['duration']
        return
        
    def current(self): # O(1), len() is O(1)
        if len(self.playlist) == 0:
            raise ValueError
            
        return self.playlist[0]
        
    def play(self): # O(1)
        if len(self.playlist) == 0:
            return "No hay canciones en la lista"
        song = self.playlist.popleft() # O(1)
        if song not in self.playlist_songs:
            return "No hay canciones en la lista"
        self.playlist_songs.remove(song) # O(1)
        self.recents.append(song) # O(1)
        self.total_time -= self.songs[song]['duration']
        return f"Sonando {song}"
        
    def totalTime(self): # O(1)
        return self.total_time
    
    def recent(self, n: int): # O(n)
        if len(self.recents) == 0:
            return None
        if n < 1:
            raise ValueError
        songs = set()
        for i in range(1, n +1): #O(n)
            if i == len(self.recents) + 1: # Makes sure you dont deque more elements than in stack
                return songs
            song = self.recents[-i]
            if song in songs: # O(1)
                continue
            songs.add(song)
            i += 1

        return songs
        
    def deleteSong(self, song: str): # O(1)
        if song not in self.songs:
            return
        if song in self.playlist_songs:
            self.playlist_songs.remove(song)
            self.total_time -= self.songs[song]['duration']   
        del self.songs[song]
        return

        
        

def process_operations(operations):
    ipud = IPud()
    output = []
    
    for op in operations:
        parts = op.split()
        command = parts[0]

        try:
            if command == "addSong":
                output.append(ipud.addSong(parts[1], parts[2], int(parts[3])))
            elif command == "addToPlaylist":
                output.append(ipud.addToPlaylist(parts[1])) 
            elif command == "current":
                output.append(ipud.current()) 
            elif command == "play":
                output.append(ipud.play())
            elif command == "totalTime":
                time = ipud.totalTime()
                output.append(f"Tiempo total {time}")
            elif command == "recent":
                recents = ipud.recent(int(parts[1]))
                n = parts[1]
                if recents == None:
                    output.append("No hay canciones recients")
                else:
                    output.append(f"Las {n} mas recientes")
                    for song in recents:
                        output.append(f"    {song}")
            elif command == "deleteSong":
                ipud.deleteSong(parts[1])
            elif command == "FIN":
                output.append("---")
                break
            else:
                output.append("ERROR: Comando no valido\n")
        except ValueError:
            output.append(f"ERROR {command}")
            
    return [line for line in output if line is not None]
            
    


def main():
    if len(sys.argv) < 2:
       raise Exception("Usage: python script.py <input_file>")

    input_file = sys.argv[1]
    operations = convert_file_to_commands(input_file)
    
    test_case = []

    for line in operations:
        if line == "FIN":
            if test_case:
                print("\n".join(process_operations(test_case)))
                print("---")
                test_case = []
        else:
            test_case.append(line)


if __name__ == "__main__":
    main()