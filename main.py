import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    else:
        match = get_close_matches(word,data.keys())
        if len(match)>0:
            choice = input('Did you mean "%s" instead ? '%match[0]).lower()
            if choice == "y":
                return data[match[0]]
            elif choice == "n":
                return "XXX Word not found XXX"
            else:
                return "We didn't understand your query"
        else:
            return "XXX Word not found XXX"

word = input("Enter the word: ")

output = translate(word)

if type(output)!=str:
    for ix in output:
        print("\n--> %s"%ix,end="\n")
else:
    print("\n--> %s"%output)

print("")
