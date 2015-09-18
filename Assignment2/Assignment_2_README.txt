For this program to work properly you will need to do the following:

Create world.txt

This file is your grid maze, and should look like this

0 0 0 0 1 0 1 1 0 0
0 2 1 1 0 0 2 0 2 0
0 0 0 0 0 0 2 0 0 0
2 0 2 2 0 0 0 0 2 0
0 0 2 0 0 2 1 0 1 0
0 0 2 0 0 2 0 0 2 0
0 0 2 0 1 2 0 1 2 2
0 0 0 0 0 0 0 0 0 0

The matrix positions are actually flipped (y,x) so the (0,0) is actually the top left corner.
The start posistion is the bottom left corner (0,7) and the goal position is  the top right corner(9,0).

Place the world.txt file in the working directory of the project.

To run in the terminal type python Nocella_Assignment2.py world.txt height width

So if we were to use the aformentioned matrix it would look like:
python Nocella_Assignment2.py world.txt 8 10