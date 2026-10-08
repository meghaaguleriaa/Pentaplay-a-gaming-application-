About the Project

This is a simple Pac-Man style game made using Python and Pygame.


The main idea of the game is to control Pac-Man, collect all the dots, avoid the ghosts, and get the highest possible score. I made the game as a small college project to understand how game loops, keyboard controls, collision detection, images, and basic game logic work in Python.


Features
Pac-Man movement using arrow keys


Maze-based gameplay


Normal dots and power pellets


Score system


3 lives


Three ghosts:
Pink
Blue
Orange


Ghosts can be eaten after collecting a power pellet
Eaten ghosts come back after a short time


Game over screen
Victory screen


Restart option using the Space key


Ghosts and Pac-Man use image assets



Technologies Used

Python
Pygame
Python modules like copy and math


board.py contains the maze layout used by the game.



How to Run
1. Install Python
Make sure Python is installed on your computer.


2. Install Pygame
Open terminal or command prompt and run:
3 pip install pygame

4. Keep the project files together
Make sure main.py, board.py, and the assets folder are in the correct project folder.


5. Run the game
python main.py


Controls
Key
Action
↑ Move Up


↓ Move Down


← Move Left


→ Move Right


Space : Restart after Game Over/Victory


How the Game Works


At the start of the game, Pac-Man is placed inside the maze. The player uses the arrow keys to move around the maze and collect dots.
Normal dots increase the score. Power pellets give Pac-Man the ability to eat ghosts for a limited time.
When a ghost is eaten, it changes to the dead-ghost image. After some time, the ghost comes back into the maze and starts chasing Pac-Man again.
The player loses a life if Pac-Man touches an active ghost without having power mode active.
The game is won when all the dots and power pellets in the maze have been collected.


Scoring

Normal dot = 10 points
Power pellet = 50 points
Eaten ghost = 200 points


Game States

The game mainly has three possible states:

Playing
Pac-Man can move, collect dots, and interact with ghosts.

Game Over
The player loses all 3 lives.

Victory
All the dots and power pellets are collected.


This project helped me understand the basic concepts of making a game in Python. It is a simple implementation, but it combines many important programming concepts like loops, conditions, classes, functions, collision detection, and event handling.

