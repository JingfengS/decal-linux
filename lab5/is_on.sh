#!/bin/zsh

# To check if the basic connection is established
ping -c 1 $1 > connection.log & PID=$!
wait $PID
ReturnValue=$?
if [ $ReturnValue -eq 0 ];
then
    echo "OK, we are good!"
else 
    echo "Oops! Host is not reachable"
fi
\
