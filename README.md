# 🚀 Mars-Rover-Expedition
Ein textbasiertes Python-Spiel, das die Expedition eines Rovers durch eine unendlich generierte, zweidimensionale Marslandschaft simuliert. In dieser Simulation schlüpfst du in die Rolle eines Kommandanten und steuerst einen Mars-Rover. Ziel ist es, den Rover sicher durch das Gelände zu navigieren, Ressourcen (Energie) zu verwalten, Schätze (Münzen) zu sammeln und unvorhersehbare Zufallsereignisse zu überstehen. 

Jeder Schritt wird detailliert im Terminal protokolliert, und am Ende der Mission wird ein vollständiger Expeditionsbericht erstellt. Das Programm läuft vollständig im Terminal, benötigt keine grafische Benutzeroberfläche und läuft ab Python-Version 3.11.

## 📋 Startanleitung

1. Lade alle Projektdateien (main.py, world.py, panels.py) in denselben Ordner herunter.
2. Lass dem main.py im Terminal (Command Prompt) oder ein IDE laufen
3. Das Spiel wird dich beim Start nach deinen Startparametern fragen (Schwierigkeitsgrad, Name des Kommandanten, Rover-Name und Start-Koordinaten).

## 🎮 Steuerung

* l – nach links bewegen
* r – nach rechts bewegen
* u – nach oben bewegen
* d – nach unten bewegen

Pro-Tipp: Befehle lassen sich kombinieren (z. B. 'uur' für zwei Schritte nach oben und einen nach rechts), um mehrere Bewegungen durch den Autopiloten nacheinander auszuführen!

### Spezielle Befehle:
shop – öffnet das Shop-Menü für Upgrades und Gegenstände.
instruct – öffnet das Handbuch mit einer Erklärung aller Funktionen.

## 🌍 Elemente der Welt

* 🛸 Rover: Dein Fahrzeug.
* 🟥 Leeres Gelände: Sicherer Boden.
* 🧱 Fels (Hindernis): Eine Kollision führt zum sofortigen Scheitern der Mission.
* 🪙 Schatz/Münze: Erhöht dein Guthaben. Münzen können im Shop für Upgrades verwendet werden.
* 🔋 Ladestation: Füllt die Energie wieder auf.

Hinweis: Jeder Schritt kostet den Rover 5 Energieeinheiten. Die maximale Energie ist auf 500 begrenzt. Sinkt die Energie auf 0, scheitert die Mission.

## 🎲 Zufällige Ereignisse

Blitzbeben (⛈️): Ein plötzliches Wetterereignis, das die Verbindung zum Rover unterbricht, laufende Bewegungsabfolgen stoppt und umliegende Felder gefährlich macht. Ein direkter Treffer zerstört den Rover.
Xenologische Begegnungen (👽 Alien-Eier): Sehr seltene Funde auf der Karte, die im Shop für eine große Anzahl an Münzen verkauft werden können.

## 🏁 Spielende

Erfolg: Du kaufst ein Rover-Upgrade im Shop und erreichst das nächste Level.
Misserfolg (Kollision): Der Rover prallt gegen einen Felsen oder gerät in ein Blitzbeben.
Misserfolg (Energie): Dem Rover geht die Energie aus.
