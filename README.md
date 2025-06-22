# ⭐ Star Wars 2D Shooter Game

A simple 2D Star Wars-themed space shooter game built using **Python** and **Pygame**. This game features classic arcade mechanics like player movement, shooting, enemies, scoring, levels, and a Game Over screen.

---

## 🌐 Demo

![screenshot](./screenshots/gameplay.png)

---

## 🎓 Features

* Player spaceship with left/right movement and shooting
* Enemy spaceship that shoots every second
* Collision detection for bullets
* Score and level tracking
* Background image for visual immersion
* Game Over screen with restart and exit options
* Level-based difficulty progression

---

## 📁 Project Structure

```bash
starwar_game/
├── assets/
│   ├── player.png
│   ├── enemy.png
│   └── background.png
├── src/
│   └── main.py
├── screenshots/
│   └── gameplay.png
├── README.md
```

---

## 📚 Requirements

* Python 3.7+
* pygame (install with `pip install pygame`)

---

## ⚙️ How to Run

1. Clone this repository:

```bash
git clone https://github.com/yourusername/starwar_game.git
cd starwar_game
```

2. Install dependencies:

```bash
pip install pygame
```

3. Run the game:

```bash
python src/main.py
```

---

## ⌚ Controls

* ← / → Arrow Keys: Move left/right
* Spacebar: Shoot bullet
* ENTER: Restart after Game Over
* ESC: Exit the game

---

## 🛠️ Game Logic

* Player starts with 3 lives
* Each enemy hit gives +1 point
* Every 5 points = new level (increases speed)
* Game Over when lives reach 0

---

## 🚀 Future Improvements

* Multiple enemies
* Sound effects and music
* Power-ups and special weapons
* High score tracking
* More level designs and backgrounds

---
