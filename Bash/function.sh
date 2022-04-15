#!bin/bash

my_function()  {
    echo "Good Morinign $1!"
    sleep 1
    echo "You're looking good today $1"
    sleep 1
    echo "You have the best ideas ever $1"
}

my_add(){
    local val=$(($1 + $2))
    printf "Sum of numbers: %d" $val
}

echo -n "Enter a name: "
read INPUT

my_function $INPUT

my_add 2 4