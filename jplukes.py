# 1. Vytvořte pole, které bude mít 5 stringových hodnot.
pole = ["strom", "řeka", "hora", "jezero", "město"]
print("Základní list:", pole)

# 2. Přidejte pomocí metody append() jeden prvek. - "vítr"
pole.append("vítr")
print("Po Přidání 'vítr':", pole)

# 3. Odstraňte pomocí metody remove() druhý prvek z pole.
pole.remove(pole[1])  
print("Po Odstranění druhého stringu:", pole)

# 4. Zaměňte 5. hodnotu z pole za: "slunce"
pole[4] = "slunce"
print("Po Zaměnění pátého stringu za 'slunce':", pole)

# 5. Přidejte 2 stringové hodnoty pole pomocí metody extend().
pole.extend(["měsíc", "hvězda"])
print("Po Přidání 'měsíc' a 'hvězda':", pole)
