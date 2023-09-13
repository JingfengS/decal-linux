#!/usr/bin/python3


import sys
import os

PHONEBOOK_ENTRIES = "python_phonebook_entries"

class Duplicate_Map:

    def __init__(self):
        self.keys = []
        self.values = []
        self.size = 0

    def length(self):
        return self.size

    def add(self, key, value):
        self.keys.append(key)
        self.values.append(value)
        self.size += 1

    def remove(self, key):
        occurred_index = self.getIndex(key)
        if not occurred_index:
            print("There are no keys match!")
        else:
            j = 0
            for i in occurred_index:
                self.keys.pop(i-j)
                self.values.pop(i-j)
                self.size -= 1
                j += 1

    def getIndex(self, key):
        occurred_index = []
        for i in range(0, self.size):
            if self.keys[i] == key:
                occurred_index.append(i)
        return occurred_index
    
    def get(self, key):
        occurred_index = self.getIndex(key)
        values = []
        if not occurred_index:
            print("No key match!")
            return
        for index in occurred_index:
            values.append(self.values[index])
        return values

class PHONEBOOK:
    def __init__(self, path):
        self.name_to_number = Duplicate_Map()
        content = open(path, 'r')
        while (line := content.readline()):
            information = line.split()
            if len(information) == 3:
                self.name_to_number.add(information[0] + " " + information[1], information[2])
            elif len(information) == 2:
                self.name_to_number.add(information[0], information[1])
            #print(f"DEBUG: keys = {self.name_to_number.keys}" + 
            #       f" values = {self.name_to_number.values}")
        content.close()
        self.path = path

    def new(self, name, number):
        self.name_to_number.add(name, number)
        #print(f"DEBUG: keys = {self.name_to_number.keys}" + 
        #           f" values = {self.name_to_number.values}")
        

    def update(self):
        with open(self.path, 'w') as content:
            content.write('')
        with open(self.path, 'a') as content:
            for i in range(self.name_to_number.length()):
                content.write(f"{self.name_to_number.keys[i]} {self.name_to_number.values[i]}\n")

    def list(self):
        for name, number in zip(self.name_to_number.keys, self.name_to_number.values):
            print(f"{name} {number}")

    def remove(self, name):
        self.name_to_number.remove(name)

    def lookup(self, name):
        values = self.name_to_number.get(name)
        if not values:
            print("No name in the phonebook match!")
            return
        for value in values:
            print(value)

    def clear(self):
        self.name_to_number.keys = []
        self.name_to_number.values = []
        self.name_to_number.size = 0





def main():
    phonebook = PHONEBOOK(PHONEBOOK_ENTRIES)
    if len(sys.argv) < 2:
        exit(1)

    elif sys.argv[1] == "new":
        # YOUR CODE HERE #
        phonebook.new(sys.argv[2], sys.argv[3])
        

    elif sys.argv[1] == "list":
        if not os.path.isfile(PHONEBOOK_ENTRIES) or os.path.getsize(
                PHONEBOOK_ENTRIES) == 0:
            print("phonebook is empty")
        else:
            # YOUR CODE HERE #
            phonebook.list()
    
    elif sys.argv[1] == "lookup":
        # YOUR CODE HERE #
        phonebook.lookup(sys.argv[2])

    elif sys.argv[1] == "remove":
        name = " ".join(sys.argv[2:])
        # YOUR CODE HERE #
        phonebook.remove(sys.argv[2])

    elif sys.argv[1] == "clear":
        # YOUR CODE HERE #
        phonebook.clear()

    else:
        name = " ".join(sys.argv[1:])
        with open(PHONEBOOK_ENTRIES, 'r') as f:
            lookup = "".join(filter(lambda line: name in line, f.readlines()))
            # YOUR CODE HERE #
            pass
    phonebook.update()


if __name__ == "__main__":
    main()
