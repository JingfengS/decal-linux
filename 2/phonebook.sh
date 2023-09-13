#!/bin/bash

PHONEBOOK_ENTRIES="bash_phonebook_entries"


if [ "$#" -lt 1 ]; then
    exit 1

elif [ "$1" = "new" ]; then
    # YOUR CODE HERE #
    echo "$2 $3" >> bash_phonebook_entries

elif [ "$1" = "list" ]; then
    if [ ! -e $PHONEBOOK_ENTRIES ] || [ ! -s $PHONEBOOK_ENTRIES ]; then
        echo "phonebook is empty"
    else
        # YOUR CODE HERE #
	cat bash_phonebook_entries | sd '(?P<name>\w+)\s\d.*' '$name'
    fi

elif [ "$1" = "lookup" ]; then
    # YOUR CODE HERE #
    cat bash_phonebook_entries | sd "$2\s(?P<number>\d+-\d+-\d+)" '$number' | sd '^\D.*' ''

elif [ "$1" = "remove" ]; then
    # YOUR CODE HERE #
    cat bash_phonebook_entries | sd "$2\s\d.*" '' > helper_bash_phonebook
    cat helper_bash_phonebook > bash_phonebook_entries

elif [ "$1" = "clear" ]; then
    # YOUR CODE HERE #
    echo '' > bash_phonebook_entries

else
     # YOUR CODE HERE #
     echo "TODO"
fi
