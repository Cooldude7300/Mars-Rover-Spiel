# World

# Holt die Python-Klasse random, um zufällige Objekte zu generieren
import random

# 4 Scroll-Methoden:
def scroll_left(grid):
    for i in range(len(grid)):
        for j in range(14, 0, -1):
            grid[i][j] = grid[i][j - 1]
    for i in range(len(grid)):
        grid[i][0] = "🟥"
    grid[2][8] = "🟥"

def scroll_right(grid):
    for i in range(len(grid)):
        for j in range(0, 14, 1):
            grid[i][j] = grid[i][j + 1]
    for i in range(len(grid)):
        grid[i][14] = "🟥"
    grid[2][6] = "🟥"

def scroll_up(grid):
    for i in range(4, 0, -1):
        for j in range(len(grid[i])):
            grid[i][j] = grid[i - 1][j]
    for i in range(len(grid[0])):
        grid[0][i] = "🟥"
    grid[3][7] = "🟥"

def scroll_down(grid):
    for i in range(0, 4):
        for j in range(len(grid[i])):
            grid[i][j] = grid[i + 1][j]
    for i in range(len(grid[0])):
        grid[4][i] = "🟥"
    grid[1][7] = "🟥"


# Generiert Batterien und Münzen
def gen_drops(maxim, difficulty):
    coin = -1
    battery = -1
    if random.randint(0, 7 - difficulty) == 0:
        battery = random.randint(0, maxim)
    if random.randint(0, 4 + difficulty) == 0:
        coin = random.randint(0, maxim)

    return coin, battery

# Haupt-Generierungsfunktion: nutzt die lokale Funktion gen_drops für Münzen und Batterien
def gen_world(move, difficulty):
    if move == "l":
        r1_x = 0
        r1_y = random.randint(0, 4)

        coin, battery = gen_drops(4, difficulty)
        return r1_x, r1_y, coin, battery

    elif move == "r":
        r1_x = 14
        r1_y = random.randint(0, 4)

        coin, battery = gen_drops(4, difficulty)
        return r1_x, r1_y, coin, battery

    elif move == "u":
        r1_x = random.randint(0, 14)
        r1_y = 0
        r2_x = random.randint(0, 14)
        r2_y = 0
        r3_x = random.randint(0, 14)
        r3_y = 0

    else:  # move == "d"
        r1_x = random.randint(0, 14)
        r1_y = 4
        r2_x = random.randint(0, 14)
        r2_y = 4
        r3_x = random.randint(0, 14)
        r3_y = 4

    coin, battery = gen_drops(14, difficulty)
    return r1_x, r1_y, r2_x, r2_y, r3_x, r3_y, coin, battery

def gen_quake(difficulty):
    quake = [-1, -1]
    if random.randint(1, 55 - difficulty * 5) == 1:
        quake[0] = random.randint(1, 3)
        quake[1] = random.randint(1, 10)
        if quake[1] >= 6:
            quake[1] += 3
    return quake[0], quake[1]

# Generiert Chancen für die extrem seltenen Eier
def gen_egg():
    chance = -1
    if random.randint(1,60) == 1:
        chance = random.randint(1,3)
    return chance


# Gibt dem Benutzer Informationen über das umliegende Gelände
def scan(emoji, direction):

    if direction == "2":
        print(" ->", end=" ")
    else:
        print("\n[Scanner]", direction, end=" -> ")
    match emoji:
        case "🟥":
            print("leeres Gelände", end=" ")
        case "🪙":
            print("Schatz", end=" ")
        case "🔋":
            print("Aufladestation gefunden", end=" ")
        case "🧱":
            print("⚠ Kritisch ⚠️ : Felsen", end=" ")
        case "⛈️":
            print("⚠ Kritisch ⚠️ : Blitzbeben", end=" ")


# Setzt das Raster auf das Standardgelände zurück
def set_grid():
    grid = [
        ['🟥', '🟥', '🟥', '🟥', '🟥', '🟥', '🟥', '🟥', '🟥', '🟥', '🟥', '🟥', '🟥', '🟥', '🟥'],
        ['🟥', '🟥', '🟥', '🟥', '🟥', '🟥', '🟥', '🟥', '🟥', '🟥', '🟥', '🟥', '🟥', '🟥', '🟥'],
        ['🟥', '🟥', '🟥', '🟥', '🟥', '🟥', '🟥', '🛸', '🟥', '🟥', '🟥', '🟥', '🟥', '🟥', '🟥'],
        ['🟥', '🟥', '🟥', '🟥', '🟥', '🟥', '🟥', '🟥', '🟥', '🟥', '🟥', '🟥', '🟥', '🟥', '🟥'],
        ['🟥', '🟥', '🟥', '🟥', '🟥', '🟥', '🟥', '🟥', '🟥', '🟥', '🟥', '🟥', '🟥', '🟥', '🟥']
    ]
    return grid

def border_check(pos_x, pos_y):
    if pos_x < -1700 or pos_x > 1700 or pos_y < -1700 or pos_y > 1700:
        print("Der Rover kann nicht über die Weltgrenze fliegen.")
        return False

    elif pos_x == 1700 or pos_x == -1700 or pos_y == 1700 or pos_y == -1700:
        if pos_x == -1700 or pos_x == 1700:
            print("⚠ ⚠ ⚠ Der Rover kann in diese Richtung nicht weiter entlang der X-Achse fliegen.")
        if pos_y == -1700 or pos_y == 1700:
            print("⚠ ⚠ ⚠ Der Rover kann in diese Richtung nicht weiter entlang der Y-Achse fliegen.")

    elif pos_y < -1650 or pos_y > 1650 or pos_x < -1650 or pos_x > 1650:
        if pos_y < -1650:
            print(f"Der Rover ist {1700 - abs(pos_y)} Einheiten von der Weltgrenze entfernt. Bitte wähle eine andere Richtung, sonst kannst du nicht weiter nach unten fliegen.")
        if pos_y > 1650:
            print(f"Der Rover ist {1700 - pos_y} Einheiten von der Weltgrenze entfernt. Bitte wähle eine andere Richtung, sonst kannst du nicht weiter nach oben fliegen.")
        if pos_x < -1650:
            print(f"Der Rover ist {1700 - abs(pos_x)} Einheiten von der Weltgrenze entfernt. Bitte wähle eine andere Richtung, sonst kannst du nicht weiter nach links fliegen.")
        if pos_x > 1650:
            print(f"Der Rover ist {1700 - pos_x} Einheiten von der Weltgrenze entfernt. Bitte wähle eine andere Richtung, sonst kannst du nicht weiter nach rechts fliegen.")
    return True