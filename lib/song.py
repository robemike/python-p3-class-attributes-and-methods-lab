class Song:

    count = 0

    genres = list()

    artists = list()

    genre_count = {}

    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist 
        self.genre = genre

        Song.add_song_to_count()
        Song.add_to_genre(self.genre)
        Song.add_to_artist(self.artist)
        Song.add_to_genre_count(self.genre)
        Song.add_to_artist_count(self.artist)

    @classmethod
    def add_to_genre(cls, genre):
        if genre not in cls.genres:
            cls.genres.append(genre)

    @classmethod 
    def add_song_to_count(cls, increment = 1):
        cls.count += increment

    @classmethod
    def add_to_artist(cls, artist):
        if artist not in cls.artists:
            cls.artists.append(artist)
    @classmethod
    def add_to_genre_count(cls, genre, increment = 1):
        if genre in cls.genre_count:
            cls.genre_count[genre] += increment
        else:
            cls.genre_count[genre] = increment

    @classmethod
    def add_to_artist_count(cls, artist, increment = 1):
        if artist in cls.artist_count:
            cls.artist_count[artist] += increment
        else:
            cls.artist_count[artist] = increment
    
    pass