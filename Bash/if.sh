#!bin/bash

echo "Enter number :"
read VAR

if [[ $VAR -gt 100 ]] && [[ $VAR -lt 150 ]]
then 
    echo "$VAR is greater than 100 < 150"
elif [[ $VAR -lt 10 ]]
then  
    echo "$VAR is less than 10"
elif [[ $VAR -gt 50 ]]
then
    echo "$VAR is greater than 50"
elif [[ $VAR -lt 50 ]]
then
    echo "$VAR is less than 50"
else
    echo "$VAR not in test range"
fi

if [[ -z $VAR ]]
then
    echo "$VAR is empty"
fi    

if [[ "malayalam" = "malayalam" ]]; then
    echo "Malayalam is palindrome"
fi

#-n VAR - True if the length of VAR is greater than zero.
#-z VAR - True if the VAR is empty.
#STRING1 = STRING2 - True if STRING1 and STRING2 are equal.
#STRING1 != STRING2 - True if STRING1 and STRING2 are not equal.
#INTEGER1 -eq INTEGER2 - True if INTEGER1 and INTEGER2 are equal.
#INTEGER1 -gt INTEGER2 - True if INTEGER1 is greater than INTEGER2.
#INTEGER1 -lt INTEGER2 - True if INTEGER1 is less than INTEGER2.
#INTEGER1 -ge INTEGER2 - True if INTEGER1 is equal or greater than INTEGER2.
#INTEGER1 -le INTEGER2 - True if INTEGER1 is equal or less than INTEGER2.
#-h FILE - True if the FILE exists and is a symbolic link.
#-r FILE - True if the FILE exists and is readable.
#-w FILE - True if the FILE exists and is writable.
#-x FILE - True if the FILE exists and is executable.
#-d FILE - True if the FILE exists and is a directory.
#-e FILE - True if the FILE exists and is a file, regardless of type (node, directory, socket, etc.).
#-f FILE - True if the FILE exists and is a regular file (not a directory or device)