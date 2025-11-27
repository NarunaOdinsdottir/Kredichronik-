import datetime 
import random

#Klassen für den Einstieg

klassen = { "Planerin": { "Ausrüstung": ["Budgetliste", "Tageslichtlampe", "Kevin-Bot"], "Schwäche": "Perfektionismus" }, "Improvisatorin": { "Ausrüstung": ["Tupperdose Hoffnung", "2,50€ in Münzen"], "Schwäche": "Impulskäufe" }, "Rabatt-Vampirin": { "Ausrüstung": ["100 Coupons", "App-Flatrate"], "Schwäche": "Kaufsucht" }, "Budget-Zombie": { "Ausrüstung": ["Leeres Excel-Sheet", "Kaffee"], "Schwäche": "Aufschieberitis" } }

sprüche = [ "Trigger entdeckt: Aktivierung der Selbstmitgefühl-Routine...", "Dein Kontostand ist keine Wertung deiner Würde.", "Wenn du's schon gekauft hast – mach dir keinen Vorwurf. Mach dir 'ne Liste.", "Weniger ist mehr – außer bei Kaffee.", "Level Up: +1 Erkenntnis über alte Trigger." ]

ausgaben = [] trigger = []

def start(): print("\n📘 Willkommen in der KREDICHRONIK – Dein Fallout-Style Haushaltslogbuch") print("------------------------------------------------------------") name = input("Wähle deinen Namen für dieses Abenteuer: ")

print("\nHallo " + name + ", wähle deine Überlebensklasse im Ödland des Budgets:")
for idx, k in enumerate(klassen):
    print(f"{idx + 1}: {k} – Ausrüstung: {', '.join(klassen[k]['Ausrüstung'])} / Schwäche: {klassen[k]['Schwäche']}")
auswahl = int(input("\nDeine Wahl (1-4): "))
rolle = list(klassen.keys())[auswahl - 1]
print(f"\nDu bist jetzt: {rolle}! Möge dein Kontostand in Frieden ruhen.\n")

menu()

def menu(): while True: print("\n--- Hauptmenü ---") print("1. Neue Ausgabe eintragen") print("2. Trigger / Notiz eintragen") print("3. Gesamtausgaben & Trigger anzeigen") print("4. Motivation ausgeben") print("5. Programm beenden")

wahl = input("Deine Auswahl: ")

    if wahl == "1":
        neue_ausgabe()
    elif wahl == "2":
        neuer_trigger()
    elif wahl == "3":
        anzeigen()
    elif wahl == "4":
        motivation()
    elif wahl == "5":
        print("\n💾 Speicher abgeschlossen. Denk dran: Du bist mehr als deine Quittung.")
        break
    else:
        print("Ungültige Eingabe. Versuch's nochmal.")

def neue_ausgabe(): kategorie = input("Kategorie der Ausgabe (z. B. Lebensmittel, Therapie, Miete): ") betrag = float(input("Betrag in Euro: ")) datum = datetime.date.today() ausgaben.append((datum, kategorie, betrag)) print(f"✓ Ausgabe von {betrag:.2f}€ für '{kategorie}' gespeichert.")

def neuer_trigger(): notiz = input("Was hat dich heute getriggert oder beschäftigt? ") datum = datetime.date.today() trigger.append((datum, notiz)) print("✓ Notiz gespeichert. Analyse des Inneren Systems läuft...")

def anzeigen(): print("\n--- Ausgabenübersicht ---") gesamt = 0 for eintrag in ausgaben: print(f"{eintrag[0]} – {eintrag[1]}: {eintrag[2]:.2f}€") gesamt += eintrag[2] print(f"\nGesamtausgaben: {gesamt:.2f}€")

print("\n--- Trigger / Notizen ---")
for t in trigger:
    print(f"{t[0]} – {t[1]}")

def motivation(): print("\n💬 Motivationsmodul sagt:") print(random.choice(sprüche))

if name == "main": start()

