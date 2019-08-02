import json
from difflib import get_close_matches
from typing import Tuple
collection = json.load(open("collection.json"))

class TrieNode(object):
    def __init__(self, char: str):
        self.char = char
        self.children = []
        self.word_finished = False
        self.counter = 1
    

def add(root, word: str):
    node = root
    for char in word:
        found_in_child = False
        for child in node.children:
            if child.char == char:
                child.counter += 1
                node = child
                found_in_child = True
                break
        if not found_in_child:
            new_node = TrieNode(char)
            node.children.append(new_node)
            node = new_node
    node.word_finished = True

def find_prefix(root, prefix: str) -> Tuple[bool, int]:
    node = root
    if not root.children:
        return False, 0
    for char in prefix:
        char_not_found = True
        for child in node.children:
            if child.char == char:
                char_not_found = False
                node = child
                break
        if char_not_found:
            return False, 0
    return True, node.counter
def lookup(word):
    word = word.lower()
    if word in collection:
        return collection[word]
    elif len(get_close_matches(word, collection.keys())) > 0:
        yn = input("Are you looking for the word %s ? Enter Y for Yes or N for No: " % get_close_matches(word, collection.keys())[0])
        if yn == "Y":
            return collection[get_close_matches(word, collection.keys())[0]]
        elif yn == "N":
            return "Word not found. Please try again."
        else:
            return "Please enter either Y or N"
    else:
        return "No word entered"
    

if __name__ == "__main__":
    root = TrieNode('*')
    for i in collection:
        add(root, i)
    '''print('\n***** WELCOME TO THE PYTHON ENGLISH DICTIONARY *****\n')
    word = input("Enter word: ")
    output = lookup(word)
    if type(output) == list:
        for item in output:
            print(item)
    else:
        print(output)'''
    print('\n***** WELCOME TO THE PYTHON ENGLISH DICTIONARY *****\n')
    word = input("Enter word: ")
    
    print(find_prefix(root, word))
    
        
