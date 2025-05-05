import sys

class iPod:
    def __init__(self):
        self.songs = {}  
        self.playlist = []  
        self.recently_played = []  
        self.total_play_time = 0  

    def addSong(self, S, A, D):
        # Time Complexity: O(1) - Dictionary lookup and insertion are O(1)
        if S in self.songs:
            
            return "ERROR addSong"
        else:
            self.songs[S] = (A, int(D))  
            return None  

    def addToPlaylist(self, S):
        # Time Complexity: O(n) - Checking if song exists in playlist takes O(n) where n is the size of the playlist
        if S not in self.songs:
            
            return "ERROR addToPlaylist"
        if S not in self.playlist:
            self.playlist.append(S) 
            self.total_play_time += self.songs[S][1]  
        return None  

    def current(self):
        # Time Complexity: O(1) - Accessing first element of the playlist is O(1)
        if not self.playlist:
           
            print("ERROR current")
        else:
            
            print(self.playlist[0])

    def play(self):
        # Time Complexity: O(n) - Removing the first song (pop(0)) is O(n) because it shifts the elements in the list
        if not self.playlist:
            
            print("No hay canciones en la lista")
            return
        song = self.playlist.pop(0)  
        self.total_play_time -= self.songs[song][1]  
        self.recently_played.insert(0, song)  
        print(f"Sonando {song}")
    def totalTime(self):
        # Time Complexity: O(1) - Accessing an integer value and printing is O(1)
        print(f"Tiempo total {self.total_play_time}")

    def recent(self, N):
        # Time Complexity: O(n)
        if not self.recently_played:
            print("No hay canciones recientes")
        else:
            R = min(N, len(self.recently_played))  
            print(f"Las {R} mas recientes")
            for song in self.recently_played[:R]: 
                print(f"    {song}")

    def deleteSong(self, S):
        # Time Complexity: O(1) - Dictionary removal is O(1), list removal is O(n) in worst case
        if S in self.songs:
            del self.songs[S]  

            if S in self.playlist:
                self.playlist.remove(S)  
                self.total_play_time -= self.songs[S][1]  
            
            if S in self.recently_played:
                self.recently_played.remove(S)  

def process_operations(operations):
    school = iPod()  
    output = []  

    for op in operations:
        parts = op.strip().split()
        if not parts:
            continue

        cmd = parts[0]
        current_output = []

        if cmd == "FIN":
            break  

        try:
            if cmd == "addSong":
                S, A, D = parts[1], parts[2], int(parts[3])
                school.addSong(S, A, D)  
            elif cmd == "addToPlaylist":
                S = parts[1]
                school.addToPlaylist(S) 
            elif cmd == "play":
                school.play()  
            elif cmd == "totalTime":
                school.totalTime()  
            elif cmd == "deleteSong":
                S = parts[1]
                school.deleteSong(S)  
            elif cmd == "recent":
                N = int(parts[1])
                school.recent(N)  
            elif cmd == "current":
                school.current()  
        except Exception:
            current_output = ["ERROR"]  
        
        output.extend(current_output) 

    return output

def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py input_file")
        sys.exit(1)

    with open(sys.argv[1], 'r') as f:
        current_case = []
        for line in f:
            cleaned = line.strip()
            if cleaned == "FIN":
                if current_case:
                    results = process_operations(current_case)  
                    print('\n'.join(results))
                    print("---")
                    current_case = []  
            else:
                current_case.append(cleaned)  
        
        if current_case:
            results = process_operations(current_case)  
            print('\n'.join(results))
            print("---")

if __name__ == "__main__":
    main()

