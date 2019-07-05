""" Looping through unique values in the dictionary after sorting them"""

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

print("The following languages have been mentioned:")
for language in sorted(set(favorite_languages.values())):
    print(language.title())
