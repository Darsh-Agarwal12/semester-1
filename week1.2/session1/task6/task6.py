# Week 1.2, Session 1: Task 6

from pprint import pprint

# Create music database, as a dictionary of strings mapped to lists
# (keys are artist names, values are lists of album names)
music={
    "Pink Floyd": ["The Dark Side of the Moon", "The Wall", "Wish You Were Here"],
    "Daft Punk": ["Homework", "Discovery", "Random Access Memories"],
    "Billie Eilish": ["When We All Fall Asleep, Where Do We Go?", "Happier Than Ever", "Hit Me Hard and Soft"],
    "The Weeknd": ["House of Balloons", "After Hours", "Dawn FM"]
}
# Pretty-print the data structure
pprint(music)
# Display details of one album recorded by a specific artist
print(f"Printing first album by The Weeknd: {music['The Weeknd'][0]}")