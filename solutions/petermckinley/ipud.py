from collections import deque, OrderedDict
import sys

class iPud:
    def __init__(self):
        self.trackList = {}  # {song_name: (artist, duration)}
        self.songQueue = deque()  # Queue for playback
        self.historyDict = OrderedDict()  # OrderedDict to preserve playback history order
        self.totalDuration = 0  # total duration of playlist

    # O(1) dictionary insertion
    def addSong(self, title, musician, length):
        if title in self.trackList:
            return "ERROR addSong"
        self.trackList[title] = (musician, int(length))
        return None

    # O(1) appends if not present in playlist
    def addToPlaylist(self, track):
        if track not in self.trackList:
            return "ERROR addToPlaylist"
        if track not in self.songQueue:
            self.songQueue.append(track)
            self.totalDuration += self.trackList[track][1]
        return None

    # O(1) returns first element in playlist
    def currentSong(self):
        if not self.songQueue:
            return "ERROR current"
        return self.songQueue[0]

    # O(1) removes and plays the first song
    def play(self):
        if not self.songQueue:
            return "No hay canciones en la lista"
        song = self.songQueue.popleft()
        self.totalDuration -= self.trackList[song][1]
        if song in self.historyDict:
            del self.historyDict[song]
        self.historyDict[song] = None  # Preserve order in history
        return f"Sonando {song}"

    # O(1) returns stored total duration of playlist
    def total_time(self):
        return f"Tiempo total {self.totalDuration}"

    # O(N) - Slices list up to N to get recent songs
    def recentSongs(self, count):
        recent_songs = list(self.historyDict.keys())[-count:][::-1]
        if not recent_songs:
            return "No hay canciones recientes"
        output = [f"Las {len(recent_songs)} mas recientes"]
        output.extend(f"    {song}" for song in recent_songs)
        return output

    # O(1) removes song from track list, playlist, and history
    def delete_song(self, title):
        if title in self.trackList:
            del self.trackList[title]
        if title in self.songQueue:
            self.songQueue.remove(title)
            self.totalDuration -= self.trackList[title][1]
        if title in self.historyDict:
            del self.historyDict[title]
        return None

# Reads input file and returns list of stripped command lines
def convert_file_to_commands(filename):
    # Time: O(n) where n is number of lines
    with open(filename, "r", encoding="utf-8") as f:
        return [line.strip() for line in f.readlines() if line.strip()]

# Executes a sequence of commands, returns result lines
def process_operations(operations):
    ipudPlayer = iPud()
    outputLog = []

    for op in operations:  # Time: O(m), m = number of commands
        parts = op.split()
        if not parts:
            continue
        command = parts[0]

        try:
            if command == "addSong":
                response = ipudPlayer.addSong(parts[1], parts[2], parts[3])
                if response:
                    outputLog.append(response)
            elif command == "addToPlaylist":
                response = ipudPlayer.addToPlaylist(parts[1])
                if response:
                    outputLog.append(response)
            elif command == "current":
                response = ipudPlayer.currentSong()
                if response:
                    outputLog.append(response)
            elif command == "play":
                outputLog.append(ipudPlayer.play())
            elif command == "totalTime":
                outputLog.append(ipudPlayer.total_time())
            elif command == "recent":
                response = ipudPlayer.recentSongs(int(parts[1]))
                if isinstance(response, list):
                    outputLog.extend(response)
                else:
                    outputLog.append(response)
            elif command == "deleteSong":
                ipudPlayer.delete_song(parts[1])
            elif command == "FIN":
                outputLog.append("---")
                break
            else:
                outputLog.append("ERROR: Comando no valido\n")
        except Exception:
            outputLog.append("ERROR")

    return [line for line in outputLog if line is not None]

# Main script entry — supports batch input file
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
