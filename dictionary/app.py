r"""
This is a scriot that gets meaning of words
"""
import json

from difflib import get_close_matches 


#loading the words in a file

data=json.load(open("data.json"));

#A function that returns the meaning of the word

def meaning(w):
    #changing to lower case for case sensitivity
    w=w.lower()
    if w in data:
        return data[w];
    elif w.title() in data:
        return data[w.title()]
    elif w.upper() in data:
        return data[w.upper()]
    elif(len(get_close_matches(w,data.keys()))>0):
        yn=input("Did you mean %s ? Enter Y for yes, and N for no: " % get_close_matches(w,data.keys())[0]);
        if yn=='Y':
            return data[get_close_matches(w,data.keys())[0]];
        elif yn=='N':
            return "We couldn't find the word you are looking for.";
        else:
            return "Wrong Input";
    else:
        return "The word doesn't exist, Please Double check"

#collects inputs
word=input("What word are you looking for ? ");

output=meaning(word);

if (type(output) == list):
    for item in output:
        print(item)
else:
    print(output)