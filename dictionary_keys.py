""" Looping through people's names i.e. Keys in the dictionary"""

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

print("The following people have been mentioned:")
for person in favorite_languages.keys():
    print(person.title())
