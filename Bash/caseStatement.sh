#! /bin/bash

read -p "Are you 21 or Over? Y/N " ANSWER
case "$ANSWER" in 
	[yY] | [yY][eE][sS])
		echo "You can have a beer"
		;;
	[nN] | [nN][oO])
		echo "Sorry, you can't drink"
		;;
	*)
		echo "Please enter y/yes or n/no"
		;;
esac