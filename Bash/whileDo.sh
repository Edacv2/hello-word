#! /bin/bash

number=1
while [ $number -lt 10 ]
do
	echo "$number"
	number=$(( number+1 ))
done

################################

count=10
if [ $count -eq 10 ]
then
	echo "the condition is true"
fi

################################

echo "Enter a Number"
read  num

case $num in 
1)
echo "This is 1 with case";;
2)
echo "This is 2 with case";;
*)#<-- wild card any value
echo "Not valid"
esac


'
https://www.youtube.com/watch?v=e7BufAVwDiM
Next topic 
45:29 Script input (STDIN)
'
