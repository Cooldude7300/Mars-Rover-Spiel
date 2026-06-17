# Main

# Holt die Python-Klasse time, um Verzögerungen zu verursachen
import time
# Holt die Python-Klasse platform, um zu prüfen, ob die Plattform Windows ist
import platform
# Holt die Python-Klasse os, um Dateien zu schreiben
import os
# Nutzt unsere eigenen Dateien für die erforderlichen Funktionen
from world import set_grid, scroll_up, scroll_down, scroll_left, scroll_right, gen_world, gen_quake, gen_egg, scan, border_check
from panels import open_manual, open_shop


def validate_int(prompt, retry, min=None, max=None):
    while True:
        try:
            vari = int(input(prompt))
            if (min is not None and vari < min) or (max is not None and vari > max):
                print(f"Bitte wähle eine Zahl zwischen {min} und {max}.")
                continue
            break
        except ValueError:
            print(retry)
    return vari


def gen_file():
    filename = f"Game{file_num}.txt"
    file = open(filename, "w", encoding="utf-8")
    file.write("================ MARS-ROVER BERICHT ================\n\n")
    return file


def delete(f_num):
    for i in range(f_num):
        f_name = f"Game{i + 1}.txt"
        if os.path.exists(f_name):
            os.remove(f_name)


def beep(sound):
    if not SOUND_ENABLED:
        return
    if sound == "Claim_c":
        winsound.Beep(1200, 150)
    elif sound == "Claim_e":
        winsound.Beep(700, 300)
    else:
        winsound.Beep(400, 500)
        winsound.Beep(300, 500)


def dramatise(phrase, time1, time2):
    print(f"{phrase}.", end="")
    time.sleep(time1)
    print(f"\r{phrase}..", end="")
    time.sleep(time1)
    print(f"\r{phrase}...", end="")
    time.sleep(time2)


def main():
    # Variablen deklarieren
    steps = 0
    balance = 0
    lifetime = 0
    alive = True
    level = 1
    bonus = 0
    eggs = 0
    n_level = level

    grid = set_grid()
    print()
    while True:
        difficulty = validate_int("Wähle den Schwierigkeitsgrad (1-5): ", "Bitte gib eine gültige ganze Zahl ein.", 1, 5)

        if not 1 <= difficulty <= 5:
            print("Bitte wähle eine Zahl zwischen 1 und 5.")
            continue
        break

    energy = 150 - (difficulty * 5)

    print()

    # Begrüßt den Spieler
    print(f"Hallo Kommandant {username}, willkommen am Startplatz der Rakete!")
    if input("Drücke Enter, um den Mars-Rover zu starten, oder tippe 'instruct', um die Anleitung zu öffnen: ").lower() == "instruct":
        open_manual()
    print("\n")
    file = gen_file()

    while True:
        rover = input("Wähle einen coolen Namen für deinen Rover: ")
        if rover == "" or rover == " ":
            print("Dein Raumschiff muss einen Namen haben.")
        else:
            break

    print("An welchen Koordinaten möchtest du den Rover landen?")

    pos_x = validate_int("X: ", "Bitte gib eine gültige ganze Zahl ein.", -1500, 1500)
    pos_y = validate_int("Y: ", "Bitte gib eine gültige ganze Zahl ein.", -1500, 1500)

    print("\n")
    dramatise("Rover landet auf dem Mars", 0.5, 1)
    print()
    dramatise("Sensordaten werden abgerufen", 0.5, 1)
    print("\n")

    print(f"Willkommen in Level {level}")
    print("Deine Mission ist es, ein höheres Level zu erreichen. Öffne den Shop, um ein Upgrade zu kaufen.\n\n")

    last_moves = ["", "", ""]
    old_pos = [pos_x, pos_y]

    while alive:
        for i in last_moves:
            if i != "":
                print(i)

        scan(grid[2][6], "Links")
        scan(grid[2][5], "2")

        scan(grid[2][8], "Rechts")
        scan(grid[2][9], "2")

        scan(grid[1][7], "Oben")
        scan(grid[0][7], "2")

        scan(grid[3][7], "Unten")
        scan(grid[4][7], "2")

        scan(grid[1][6], "Diagonal Links-Oben")
        scan(grid[1][8], "Diagonal Rechts-Oben")
        scan(grid[3][6], "Diagonal Links-Unten")
        scan(grid[3][8], "Diagonal Rechts-Unten")

        # Zeigt Details an
        print(f"Alte Position    : x = {old_pos[0]}  y = {old_pos[1]}")
        print("-------------------------------------------")
        print(f"Kommandanten Name:  {username}")
        print(f"Rover-Name       :  {rover}")
        print(f"Gemachte Schritte:  {steps}")
        print(f"Energie          :  {energy}")
        print(f"Position         :  x = {pos_x}  y = {pos_y}")
        print(f"Gesammelte Münzen:  {lifetime} 🪙")
        print(f"Guthaben         :  {balance} 🪙")
        print("-------------------------------------------")

        # Zeigt Zug-Optionen an
        print("""
        Steuerung:
        l - nach links
        r - nach rechts
        u - nach oben
        d - nach unten
        Du kannst auch eine Kombination dieser Buchstaben eingeben, um Züge auf einmal auszuführen!
        Oder tippe 'instruct', um die Anleitung zu öffnen

        Möchtest du einen Bonus? - tippe 'shop', um den Shop zu öffnen
        """)

        move = input("Gib deinen Zug/deine Züge ein: ").lower()

        if move == "instruct":
            open_manual()
            continue
        if move == "shop":
            bonus, balance, n_level, eggs, file = open_shop(balance, level, bonus, eggs, file)
            continue

        if n_level > level:
            level = n_level
            print("Herzlichen Glückwunsch! Mission erfolgreich")
            print(f"Du fährst nun mit Mission {level} fort")
            grid = set_grid()
            energy = 150 - (difficulty * 5)
            continue

        moves = tuple(move)

        old_pos = [pos_x, pos_y]

        data = ""

        for i in range(len(moves)):

            match moves[i]:
                case "l": # Scrollt nach links
                    pos_x -= 1
                    scroll_left(grid)
                    data = "nach links"
                case "r": # Scrollt nach rechts
                    pos_x += 1
                    scroll_right(grid)
                    data = "nach rechts"
                case "u": # Scrollt nach oben
                    pos_y += 1
                    scroll_up(grid)
                    data = "nach oben"
                case "d": # Scrollt nach unten
                    pos_y -= 1
                    scroll_down(grid)
                    data = "nach unten"
                case _ : # Zeigt Fehlermeldung
                    print("Rover konnte den Befehl nicht erkennen. Bitte gib 'l', 'r', 'u' oder 'd' ein.")
                    print(f"Habe {i} von {len(moves)} Zügen ausgeführt.")
                    break

            if not border_check(pos_x, pos_y):
                match data:
                    case "nach links":
                        pos_x += 1
                        scroll_right(grid)
                    case "nach rechts":
                        pos_x -= 1
                        scroll_left(grid)
                    case "nach unten":
                        pos_y += 1
                        scroll_up(grid)
                    case "nach oben":
                        pos_y -= 1
                        scroll_down(grid)
                break

            steps += 1
            energy -= 5
            if bonus > 0:
                bonus -= 1

            file.write(f"[SCHRITT {steps}] Rover suchte {data}")
            last_moves[0] = last_moves[1]
            last_moves[1] = last_moves[2]

            # Beendet Mission beim Zusammenstoß mit Felsen
            if grid[2][7] == "🧱":
                alive = False
                print("*******************************************************************")
                print("Mission fehlgeschlagen. Der Rover ist gegen einen Felsen gekracht.")
                file.write("\nMission fehlgeschlagen. Der Rover ist gegen einen Felsen gekracht.\n")
                break

            elif grid[2][7] == "⛈️":
                alive = False
                print("*******************************************************************")
                print("Mission fehlgeschlagen. Der Rover wurde durch ein Blitzbeben zerstört.")
                break

            # Fügt Münzen hinzu
            elif grid[2][7] == "🪙":
                if bonus > 0:
                    lifetime += 2
                    balance += 2
                    file.write(" und fand Schatzmünzen im Bonus!\n")
                else:
                    lifetime += 1
                    balance += 1
                    file.write(" und fand eine Schatzmünze\n")
                beep("Claim_c")
                grid[2][7] = "🛸"
                last_moves[2] = f"[SCHRITT {steps}] Rover suchte {data} und fand eine Schatzmünze."

            # Fügt Energie hinzu
            elif grid[2][7] == "🔋":
                energy += 40
                beep("Claim_e")
                if energy > 500:
                    energy = 500
                grid[2][7] = "🛸"
                file.write(" und fand eine Aufladestation\n")
                last_moves[2] = f"[SCHRITT {steps}] Rover suchte {data} und fand eine Aufladestation."

            else:
                grid[2][7] = "🛸"
                file.write("\n")
                last_moves[2] = f"[SCHRITT {steps}] Rover suchte {data}."

            if energy <= 0:
                alive = False
                beep("Out_e")
                print("Mission fehlgeschlagen. Dem Rover ist die Energie ausgegangen.")
                file.write("Mission fehlgeschlagen. Dem Rover ist die Energie ausgegangen.\n")
                break

            if moves[i] in ("l", "r"):
                r1_x, r1_y, coin, battery = gen_world(moves[i], difficulty)
                grid[r1_y][r1_x] = "🧱"
                if coin != -1:
                    grid[coin][r1_x] = "🪙"
                if battery != -1:
                    grid[battery][r1_x] = "🔋"

            elif moves[i] in ("u", "d"):
                r1_x, r1_y, r2_x, r2_y, r3_x, r3_y, coin, battery = gen_world(moves[i], difficulty)
                grid[r1_y][r1_x] = "🧱"
                grid[r2_y][r2_x] = "🧱"
                grid[r3_y][r3_x] = "🧱"
                if coin != -1:
                    grid[r1_y][coin] = "🪙"
                if battery != -1:
                    grid[r1_y][battery] = "🔋"

            quake_y, quake_x = gen_quake(difficulty)
            egg = gen_egg()

            if egg != -1:
                eggs += egg
                print(f"Hurra, du hast {egg} Ei(er) durch eine seltene Xenologische Begegnung erhalten!!!")
                print("Öffne den Shop, um es zu verkaufen!")
                file.write(f" und fand {egg} Xenologische Eier\n")
                
            if quake_y != -1:
                for j in range(-1, 2):
                    for k in range(-1, 2):
                        grid[quake_y + j][quake_x + k] = "⛈️"
                print(
                    f"Ein Blitzbeben in der Nähe hat kurzzeitig die Verbindung zum Rover unterbrochen. {i + 1} von {len(moves)} Zügen wurden ausgeführt.")
                break


    return steps, energy, lifetime, balance, pos_x, pos_y, rover, difficulty, file


# ---------------------------------------------------------
# Hier startet das Programm
# ---------------------------------------------------------
global SOUND_ENABLED
global file_num
global username

if platform.system() == "Windows":
    # Holt die Python-Klasse winsound, um unter Windows Sounds abzuspielen
    import winsound

    SOUND_ENABLED = True
else:
    SOUND_ENABLED = False

file_num = 0

print("***************************************")
print("Willkommen beim Mars-Rover-Spiel!")
print("***************************************")

while True:
    username = input(
        "Wähle einen coolen Benutzernamen, um dich mit dem Rover zu verbinden, oder tippe 'instruct', um die Anleitung zu öffnen: ")
    if username == "instruct":
        open_manual()
    elif username == "" or username == " ":
        print("Du musst einen Benutzernamen eingeben, um Kommandant zu werden.")
    else:
        break

while True:
    file_num += 1
    steps, energy, lifetime, balance, pos_x, pos_y, rover, difficulty, file = main()

    dramatise("Missionszusammenfassung wird abgerufen", 0.8, 1)
    print()

    file.write("\n================ ABSCHLUSSBERICHT ================\n")
    file.write(f"Kommandant: {username}\n")
    file.write(f"Name des Rovers: {rover}\n")
    file.write(f"Schwierigkeitsgrad: {difficulty}\n")
    file.write(f"Gemachte Schritte: {steps}\n")
    file.write(f"Verbleibende Energie: {energy} \n")
    file.write(f"Gesammelte Münzen: {lifetime} \n")
    file.write(f"Guthaben: {balance} \n")
    file.write(f"Endgültige Position: x = {pos_x} y = {pos_y}\n")
    file.close()

    file = open(f"Game{file_num}.txt", "r", encoding="utf-8")
    content = file.read()
    print(content)
    file.close()

    again = input("Nochmal spielen? (j/n): ").lower()
    if again not in ("j", "ja", "y", "yes"):
        break

delete(file_num)

print("Danke fürs Spielen!")
