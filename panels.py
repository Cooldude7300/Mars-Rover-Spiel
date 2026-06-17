# Panels

def open_manual():
    print("""
        Willkommen beim Mars-Rover-Spiel!
        Erkunde eine unendliche generierte Marslandschaft, sammle Münzen, lade Energie auf und überlebe so lange wie möglich.

        Steuerung:
        l - nach links bewegen
        r - nach rechts bewegen
        u - nach oben bewegen
        d - nach unten bewegen
        Oder eine Kombination dieser Buchstaben, um mehrere Züge auf einmal auszuführen
        Oder 'instruct', um die Anleitung zu öffnen

        Symbole:
        🛸 = Rover
        🟥 = Leeres Gelände
        🧱 = Felsenhindernis
        🪙 = Münze
        🔋 = Aufladestation

        Jeder Zug kostet Energie. Ein Zusammenstoß mit einem Felsen oder das Ausgehen der Energie beendet die Mission.

        Hinweis:
        Die Welt wird zufällig generiert. Sobald Objekte von der sichtbaren Karte verschwinden, tauchen sie möglicherweise nicht wieder auf, selbst wenn du zu vorherigen Koordinaten zurückkehrst.

        """)
    input("Drücke Enter, um fortzufahren... ")
    print()


global items
items = [
    ["2x Münzbeutel - 10 Züge", "Kaufen", 15],
    ["2x Münzbeutel - 20 Züge", "Kaufen", 25],
    ["Alien-Eier", "Verkaufen", -50]
    # Rover-Upgrade wird später basierend auf dem Level angehängt
]


def open_shop(balance, level, bonus, eggs, file):
    shop_items = items.copy()
    shop_items.append(["Rover-Upgrade", "Kaufen", 20 + (level - 1) * 10])
    mis = f"Bitte wähle eine gültige Option (1 - {len(shop_items)})"
    print(f"""
        Willkommen im Shop!
        Hier kannst du Rover-Ressourcen und 2x Münz-Boni erwerben...
        Oder sogar Alien-Eier verkaufen!

        Um das nächste Level zu erreichen, musst du Rover-Upgrades kaufen...

        """)
    while True:
        print(f"Dein Guthaben beträgt derzeit {balance} Münzen.")

        print("Du kannst:")
        for i in range(len(shop_items)):
            print(f"Option {i + 1}: {shop_items[i][1]} {shop_items[i][0]} für {abs(shop_items[i][2])} Münzen")

        option = input("Was möchtest du tun?: (Optionsnummer oder 'exit' zum Verlassen): ")
        if option == "exit":
            break

        try:
            option = int(option) - 1
        except ValueError:
            print(mis)
            continue

        if option >= len(shop_items) or option < 0:
            print(f"{mis}\n\n")
            continue
        elif balance < shop_items[option][2]:
            print("Du hast nicht genug Guthaben, um diesen Artikel zu kaufen.\n\n")
            continue
        elif input(
                f"\n\nDrücke Enter, um deinen Kauf zu bestätigen, oder 'c' zum Abbrechen: {shop_items[option][0]}").lower() == "c":
            continue

        if option == 0:
            bonus += 10
            file.write(f"[Shop Exchange] {shop_items[0][1]} von {shop_items[0][0]} für {abs(shop_items[0][2])}\n")
        elif option == 1:
            bonus += 20
            file.write(f"[Shop Exchange] {shop_items[1][1]} von {shop_items[1][0]} für {abs(shop_items[1][2])}\n")
        elif option == 2:
            if eggs >= 1:
                eggs -= 1
                file.write(f"[Shop Exchange] {shop_items[2][1]} von {shop_items[2][0]} für {abs(shop_items[2][2])}\n")
            else:
                print("Du hast keine Alien-Eier zum Verkaufen!\n")
                continue
        elif option == 3:
            level += 1

        balance -= shop_items[option][2]

    return bonus, balance, level, eggs, file
