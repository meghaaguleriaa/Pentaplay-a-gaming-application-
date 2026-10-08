import tkinter as tk
import subprocess
import sys
import os


# -----------------------------
# Open Game
# -----------------------------
def open_game(folder_name, file_name):
    base_folder = os.path.dirname(os.path.abspath(__file__))
    game_folder = os.path.join(base_folder, folder_name)
    game_file = os.path.join(game_folder, file_name)

    subprocess.Popen(
        [sys.executable, game_file],
        cwd=game_folder
    )


def exit_launcher():
    root.destroy()


# -----------------------------
# Window
# -----------------------------
root = tk.Tk()
root.title("PentaPlay")
root.geometry("900x800")
root.resizable(False, False)
root.configure(bg="#0b0f19")


# -----------------------------
# Colors
# -----------------------------
BG = "#0b0f19"
CARD = "#151b2b"
CARD_HOVER = "#202a40"
WHITE = "#ffffff"
GREY = "#9aa4b2"

COLORS = [
    "#ff4d6d",
    "#4dabf7",
    "#a78bfa",
    "#f59f00",
    "#22c55e"
]


# -----------------------------
# Header
# -----------------------------
header = tk.Frame(root, bg=BG)
header.pack(pady=(35, 20))

tk.Label(
    header,
    text="PENTAPLAY",
    font=("Arial", 42, "bold"),
    fg=WHITE,
    bg=BG
).pack()

tk.Label(
    header,
    text="5 GAMES  •  1 HUB  •  PICK YOUR CHALLENGE",
    font=("Arial", 12, "bold"),
    fg=GREY,
    bg=BG
).pack(pady=(5, 0))


# -----------------------------
# Games
# -----------------------------
games = [
    ("01", "FRUITY MATCH", "Match fruits. Build your score.",
     "candycrush", "main.py"),

    ("02", "SPACE INVASION", "Defend your ship. Survive the invasion.",
     "Space-Invasion-", "main.py"),

    ("03", "ZEROTH SECOND", "Test your timing and reflexes.",
     "ZeroTH-Second-", "main.py"),

    ("04", "TURBO RUSH", "Drive fast. Dodge traffic. Go further.",
     "Turbo_Rush-a-car-game-", "main.py"),

    ("05", "PACMAN", "Navigate the maze. Avoid the ghosts.",
     "pacman", "pacman_prototype_2.py")
]


# -----------------------------
# Card Hover
# -----------------------------
def on_enter(card, title_label, color):
    card.configure(bg=CARD_HOVER)
    title_label.configure(fg=color)


def on_leave(card, title_label):
    card.configure(bg=CARD)
    title_label.configure(fg=WHITE)


# -----------------------------
# Game Grid
# -----------------------------
game_frame = tk.Frame(root, bg=BG)
game_frame.pack(padx=35, fill="x")

for index, (number, name, description, folder, file) in enumerate(games):

    row = index // 2
    column = index % 2

    card = tk.Frame(
        game_frame,
        bg=CARD,
        width=390,
        height=170
    )

    card.grid(
        row=row,
        column=column,
        padx=10,
        pady=10
    )

    card.grid_propagate(False)

    color = COLORS[index]

    # Number
    number_label = tk.Label(
        card,
        text=number,
        font=("Arial", 11, "bold"),
        fg=color,
        bg=CARD
    )
    number_label.place(x=20, y=18)

    # Title
    title_label = tk.Label(
        card,
        text=name,
        font=("Arial", 20, "bold"),
        fg=WHITE,
        bg=CARD
    )
    title_label.place(x=20, y=48)

    # Description
    description_label = tk.Label(
        card,
        text=description,
        font=("Arial", 10),
        fg=GREY,
        bg=CARD,
        anchor="w"
    )
    description_label.place(x=20, y=82)

    # Play button
    play_button = tk.Button(
        card,
        text="PLAY  →",
        font=("Arial", 10, "bold"),
        fg=WHITE,
        bg=color,
        activebackground=color,
        activeforeground=WHITE,
        relief="flat",
        bd=0,
        padx=12,
        pady=5,
        cursor="hand2",
        command=lambda f=folder, p=file: open_game(f, p)
    )

    play_button.place(x=20, y=115)

    # Hover
    card.bind(
        "<Enter>",
        lambda e, c=card, t=title_label, col=color:
        on_enter(c, t, col)
    )

    card.bind(
        "<Leave>",
        lambda e, c=card, t=title_label:
        on_leave(c, t)
    )


# -----------------------------
# Exit Button
# -----------------------------
exit_button = tk.Button(
    root,
    text="EXIT GAME HUB",
    font=("Arial", 11, "bold"),
    fg=GREY,
    bg=BG,
    activeforeground=WHITE,
    activebackground=BG,
    relief="flat",
    bd=0,
    cursor="hand2",
    command=exit_launcher
)

exit_button.pack(pady=22)


# -----------------------------
# Start
# -----------------------------
root.mainloop()