#!/usr/bin/bash
FILES=$(ls)
# want to make new copies of existing files with "new" prepended to names and contents
for FILE in $FILES
do 
	echo "new" > "new_$FILE"
	cat $FILE >> "new_$FILE"
done
