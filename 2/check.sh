#!usr/bin/zsh
./phonebook.py new "Linus Torvalds" 101-110-0111
./phonebook.py list
./phonebook.py new "Tux Penguin" 555-666-7777
./phonebook.py new "Linus Torvalds" 222-222-2222
./phonebook.py list
./phonebook.py lookup "Linus Torvalds"
./phonebook.py remove "Linus Torvalds"
./phonebook.py list
./phonebook.py lookup "Tux Penguin"
./phonebook.py new "Linus Torvalds" 101-110-0111
./phonebook.py lookup "Linus Torvalds"
./phonebook.py clear

