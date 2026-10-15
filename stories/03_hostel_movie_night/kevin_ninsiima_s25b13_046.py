from story import (
    FeaturedMovie,
    MusicSession,
    MovieNight,
    StorytellingCircle,
    StreamedMovie,
    available,
)


options = [
    StreamedMovie("Full movie"),
    MusicSession("Music"),
    FeaturedMovie("Server movie"),
    StorytellingCircle(),
]

night = MovieNight("Kevin Ninsiima", 500)
before = (night.bundle.remaining, night.activities)

print("Expected titles: Music, Saver movie, Storytelling circle")
print("Actual titles:", [item.title for item in available(options, 350)])
print("Expected empty list; actual:", available(options, -1))
print("State unchange:", before == (night.bundle.remaining, night.activities))


#hi
