import json
from difflib import get_close_matches as match

## Converting json to a list
data = json.load(open("data.json"))


## Function that asks for a word and finds the correct answer
def dictionary(word):
    word = word.lower()
    if(word in data.keys()):
        return data[word]
    elif(len(match(word, data.keys(), cutoff=.8)) > 0):
        answer = input("Did you mean '%s' ? Y/N: " % match(word, data.keys())[0])
        if(answer=="Y"):
            return data[match(word, data.keys())[0]]
        elif(answer=="N"):
            return "The word does not exist!"
        else:
            return "Error!"
    else:
        return "The word does not exist!"

word = input("Enter word: ").lower()
output = dictionary(word)

## This conditional state indicates good-looking output in case the output is a list

if(type(output)==list):
    for i in output:
        print(i)
else:
    print(output)

