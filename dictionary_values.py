""" Looping through values in the dictionary"""

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

print("The following languages have been mentioned:")
for person in favorite_languages.values():
    print(person.title())
