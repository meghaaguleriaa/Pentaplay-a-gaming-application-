# 🚀 Space Invasion

### A 2D Arcade Space Shooter Game

**Space Invasion** is a 2D arcade-style space shooter developed using **Python and Pygame CE**. The player controls a spaceship, fights waves of alien enemies, avoids enemy attacks, and progresses through increasingly challenging formations.

The project was developed as a college engineering project with a focus on **Object-Oriented Programming, modular software design, game loops, event handling, collision detection, animations, audio, and progressive difficulty**.

---

## 🎮 Features

### Gameplay

* 🚀 Player spaceship movement
* 🔫 Player shooting
* 👾 Multiple enemy spaceship types
* 🛸 Multiple enemy formations
* 💥 Player and enemy bullet systems
* 🎯 Collision detection
* ⭐ Score system
* ❤️ Player health/lives system
* 🌊 Wave-based progression
* 📈 Progressive difficulty
* 💣 Enemy destruction and explosion effects
* 🎵 Background music
* 🔊 Gameplay sound effects
* 💀 Game Over state
* 🔄 Restart functionality
* 🏆 Win/progression system

### Enemy Formations

Different formations are introduced as the player progresses:

| Wave    | Formation           |
| ------- | ------------------- |
| Wave 1  | Grid                |
| Wave 2  | Triangle            |
| Wave 3  | Diamond             |
| Wave 4  | V Formation         |
| Wave 5+ | Advanced formations |

Advanced formations include patterns such as **Cross, Arrow and Hollow Rectangle**.

---

## 🕹️ Controls

| Key               | Action     |
| ----------------- | ---------- |
| `W` / `↑`         | Move Up    |
| `S` / `↓`         | Move Down  |
| `A` / `←`         | Move Left  |
| `D` / `→`         | Move Right |
| `SPACE`           | Shoot      |
| `ENTER` / `SPACE` | Start Game |
| `ESC`             | Quit       |

---

## 🧠 Engineering Concepts Used

The project applies several software and engineering principles:

### Object-Oriented Programming

Major game components are implemented as separate classes, including:

* `Game`
* `Player`
* `Enemy`
* `Bullet`
* `EnemyBullet`
* `Explosion`
* `HUD`
* `SpaceBackground`

This separates responsibilities and makes the project easier to maintain.

### Modular Design

The project is divided into separate modules for:

* Core game logic
* Game entities
* Visual effects
* Audio
* Background
* Enemy formations
* Difficulty
* HUD

### Event-Driven Programming

Pygame events are used to handle:

* Keyboard input
* Shooting
* Enemy shooting
* Game states
* Restart
* Quit events

### Collision Detection

Collision detection is used for interactions between:

* Player bullets and enemies
* Enemy bullets and player
* Enemies and player

### Game Loop

The game continuously processes:

```text
Input
  ↓
Game Logic
  ↓
Collision Detection
  ↓
Object Updates
  ↓
Rendering
  ↓
Repeat
```

---

## 🏗️ Project Structure

```text
Space Invasion/
│
├── main.py
├── settings.py
├── requirements.txt
├── README.md
│
├── assets/
│   ├── animations/
│   │   ├── fire00.png
│   │   ├── fire01.png
│   │   └── ...
│   │
│   ├── backgrounds/
│   │   └── space.png
│   │
│   ├── images/
│   │   ├── playerShip1_blue.png
│   │   ├── playerShip1_destroyed.png
│   │   ├── player_bullet.png
│   │   ├── enemyBlack3.png
│   │   ├── enemyBlue3.png
│   │   ├── enemyGreen3.png
│   │   ├── enemyRed3.png
│   │   └── enemy_bullet.png
│   │
│   ├── music/
│   │   └── background_music.mp3
│   │
│   └── sounds/
│       ├── player_shoot.wav
│       ├── player_destroy.wav
│       ├── enemy_shoot.wav
│       └── enemy_destroy.wav
│
└── src/
    │
    ├── core/
    │   ├── game.py
    │   ├── audio.py
    │   ├── background.py
    │   ├── difficulty.py
    │   ├── formation.py
    │   └── hud.py
    │
    ├── entities/
    │   ├── player.py
    │   ├── enemy.py
    │   ├── bullet.py
    │   ├── enemy_bullet.py
    │   └── explosion.py
    │
    └── effects/
        └── enemy_explosion.py
```

---

## ⚙️ Technologies Used

| Technology    | Purpose                           |
| ------------- | --------------------------------- |
| **Python**    | Main programming language         |
| **Pygame CE** | Game development framework        |
| **VS Code**   | Development environment           |
| **Git**       | Version control                   |
| **GitHub**    | Repository and project management |
| **PNG**       | Game graphics and sprites         |
| **WAV / OGG** | Sound effects                     |
| **MP3 / OGG** | Background music                  |

---

## 🎯 Gameplay System

### Player

The player controls a spaceship that can move around the game area and fire projectiles at enemies.

The player has a limited health/lives system. Enemy attacks reduce the player's available health, and the game ends when the player is destroyed.

### Enemies

Enemies are generated using predefined formation patterns. Different enemy sprites are used for different waves.

Enemies can:

* Move as formations
* Fire projectiles
* Collide with the player
* Be destroyed by player bullets

### Bullets

Two projectile systems are implemented:

**Player Bullets**

* Move upward.
* Interact with enemies.
* Destroy enemies on collision.

**Enemy Bullets**

* Move downward toward the player.
* Damage the player when a collision occurs.

---

## 🌊 Wave System

The game progresses through multiple waves.

### Wave 1

Grid formation using black enemies.

### Wave 2

Triangle formation using blue enemies.

### Wave 3

Diamond formation using green enemies.

### Wave 4

V formation using red enemies.

### Wave 5+

Advanced formations are selected from:

* Cross
* Arrow
* Hollow Rectangle

The difficulty system adjusts enemy behaviour as the player progresses.

---

## 💥 Explosion & Visual Effects

Enemy destruction produces an explosion effect.

The project contains animation frames for explosion effects and dedicated explosion/effect classes.

Visual elements include:

* Animated space background
* Stars
* Shooting stars
* Spaceship sprites
* Enemy sprites
* Projectile sprites
* Explosion effects
* HUD elements

---

## 🔊 Audio System

The game includes event-based audio feedback.

### Sounds

* **Player Shoot** — played when the player fires.
* **Enemy Shoot** — played when an enemy fires.
* **Enemy Destroy** — played when an enemy is destroyed.
* **Player Destroy** — played when the player is destroyed.
* **Background Music** — provides continuous gameplay music.

---

## 📊 HUD

The game HUD provides important gameplay information such as:

* Score
* Player health/lives
* Current wave
* Game status

The interface uses a futuristic mission-control style to match the space theme.

---

## 🧪 Testing

Major gameplay systems were tested during development:

* Player movement
* Player shooting
* Enemy movement
* Enemy shooting
* Bullet movement
* Collision detection
* Enemy destruction
* Score updates
* Health/lives
* Wave progression
* Difficulty progression
* Explosion effects
* Audio events
* Game Over
* Restart
* Win/progression states

---

## 📚 Learning Outcomes

Through this project, the following concepts were applied:

* Python programming
* Object-Oriented Programming
* Pygame development
* Game loops
* Event handling
* Keyboard input
* Collision detection
* Animation and rendering
* Object interaction
* Modular programming
* Game-state management
* Difficulty progression
* Git and GitHub

---

## 🔮 Future Scope

Possible future improvements include:

* 👑 Advanced boss battles
* ⚡ Power-ups and shields
* 🔫 Special weapons
* 👾 Additional enemy types
* ⏸️ Pause system
* ⚙️ Settings menu
* 🏆 High-score system
* 💾 Save system
* ✨ More particle effects
* 🧠 More complex enemy behaviour
* 🌊 More advanced boss waves
* 🌐 Improved web deployment

---

## 🚀 Installation & Setup

### 1. Clone the repository

```bash
git clone <YOUR-GITHUB-REPOSITORY-URL>
cd "Space Invasion"
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the virtual environment

**Windows:**

```powershell
.\venv\Scripts\Activate.ps1
```

**macOS / Linux:**

```bash
source venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the game

```bash
python main.py
```

---

## 🧑‍💻 Development

The project follows a modular architecture so individual systems can be modified without changing the entire game.

For example:

```text
game.py
    ↓
Controls overall gameplay

player.py
    ↓
Controls player behaviour

enemy.py
    ↓
Controls enemy behaviour

formation.py
    ↓
Creates enemy formations

difficulty.py
    ↓
Controls difficulty progression

audio.py
    ↓
Controls music and sound effects
```

This structure makes the project easier to **understand, debug, maintain and extend**.

---

## 👨‍💻 Project Information

**Project:** Space Invasion
**Type:** 2D Arcade Space Shooter
**Language:** Python
**Framework:** Pygame CE
**Developer:** Pratham Srivastava

---

## 📜 License

This project was developed as an academic/educational project.

Game assets used in the project should be treated according to their respective original licenses and sources.

---

# 🚀 Space Invasion

### Defend. Survive. Conquer.
