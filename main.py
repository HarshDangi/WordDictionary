import json

data = json.load(open("data.json"))

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    else:
        print("Word not found")

word = input("Enter the word: ")

print(translate(word))
