class Song:
    def __init__(self, a, b):
        self.title = a
        self.duration = b
    def info(self):
        return f"{self.title} ({self.duration} мин)"
class Playlist:
    def __init__(self, n):
        self.name = n
        self.songs = []  
    def add(self, s):
        self.songs.append(s)  
    def show(self):
        print(f"Плейлист: {self.name}")
        for s in self.songs:
            print(f"  - {s.info()}")
s1 = Song("Трек1", 3.5)
s2 = Song("Трек2", 4.0)
p = Playlist("Мой плейлист")
p.add(s1)  
p.add(s2)  
p.show() 