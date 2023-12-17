#! /bin/bash

age=30

if [ "$age" -gt 10 ] && [ "$age" -lt 40 ]
then
	echo "Age is correct"
else
	echo "Age is not correct"
fi

if [[ "$age" -gt 18 && "$age" -lt 40 ]]
then
	echo "Age is correct-2"
else
	echo "Age is incorrect-2"
fi
