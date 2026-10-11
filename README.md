# PentaPlay: A Gaming Hub

**Five Games. One Hub. Endless Fun.**

## About the Project

PentaPlay is a Python-based desktop application that brings five different games together in one place. It provides a user-friendly graphical interface where users can select and launch their preferred game with a single click.

The project combines Python, Tkinter, and Pygame to create a convenient gaming hub.

## Games Included

1. **Fruity Match:** Match fruits and earn points.
2. **Space Invasion:** Defend your ship against enemy attacks.
3. **ZeroTH Second:** An action game that tests timing and reflexes.
4. **Turbo Rush:** Drive through traffic and avoid obstacles.
5. **Pacman:** Navigate the maze while avoiding ghosts.

## Technologies Used

* **Python:** Main programming language.
* **Pygame:** Runs the individual games.
* **Tkinter:** Creates the graphical launcher.
* **Subprocess:** Launches games independently from the main interface.
* **Git and GitHub:** Used for version control and project hosting.

## Key Features

* Five games accessible through a single launcher.
* Interactive graphical interface with individual game cards.
* Separate folders for each game's source code and assets.
* One-click game launching.
* Simple navigation through a dedicated gaming hub.

## Project Structure

```text
PentaPlay/
├── launcher.py
├── README.md
├── .gitignore
├── PentaPlay.code-workspace
├── Review_PPT.pptx
├── candycrush/
├── Space-Invasion-/
├── ZeroTH-Second-/
├── Turbo_Rush-a-car-game-/
└── pacman/
```

*Note: Replace `Review_PPT.pptx` with the actual filename of your presentation.*

## How to Run

### Prerequisites

* Python installed on your computer.
* Pygame and any additional dependencies required by the individual games.

### Steps

1. Extract the PentaPlay ZIP file.

2. Open the extracted project folder in VS Code or PowerShell.

3. Install Pygame if it is not already installed:

   ```bash
   python -m pip install pygame
   ```

4. Run the launcher:

   ```bash
   python launcher.py
   ```

5. Select any game by clicking its **PLAY** button.

Some games may require additional dependencies. Check their individual README files or requirements files if a game fails to start.

## How It Works

1. The launcher displays all five games using Tkinter.
2. Each game has its own Play button.
3. When a button is clicked, Python's `subprocess.Popen()` starts the corresponding game.
4. Each game runs independently using its own source code and assets.

## Lessons Learned

* Developing graphical interfaces using Tkinter.
* Running and integrating multiple Python applications.
* Managing project folders, files, and game assets.
* Debugging dependency and file-path issues.
* Using Git and GitHub for version control.
* Testing individual games and the integrated application.

## Future Enhancements

* Add more games to the hub.
* Introduce a unified leaderboard.
* Add user profiles and common settings.
* Improve the launcher with more animations and visual effects.

## Conclusion

PentaPlay demonstrates how multiple independent games can be organized and accessed through a single graphical interface. The project provided practical experience in Python programming, GUI development, game integration, debugging, and version control.

**PentaPlay makes gaming simple by bringing five games together in one place.**

## Project Repository

GitHub: https://github.com/meghaaguleriaa/Pentaplay-a-gaming-application-
