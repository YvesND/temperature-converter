beenden = False

while True:
    einheit = str(input("Gibst du die Temperatur in Celsius oder Fahrenheit ein? (Schreibe C/F) "))
    einheit = einheit.upper()
    
    if einheit == "C":
        while True:
            try:
                temperatur = float(input("Bitte Temperatur eingeben: "))
                print(f"{temperatur} Grad Celsius entspricht {temperatur*1.8+32} Grad Fahrenheit.")
                break
            except ValueError:
                print("Du hast keine gültige Eingabe gemacht. Bitte nutze ausschliesslich Ziffern und einen Punkt als Komma.")
                
    elif einheit == "F":
        while True:
            try:
                temperatur = float(input("Bitte Temperatur eingeben: "))
                print(f"{temperatur} Grad Fahrenheit entspricht {(temperatur-32)/1.8} Grad Celsius.")
                break
            except ValueError:
                print("Du hast keine gültige Eingabe gemacht. Bitte nutze ausschliesslich Ziffern und einen Punkt als Komma.")
    else:
        print("Du hast keine gültige Eingabe gemacht. Bitte tippe C für Celsius oder F für Fahrenheit!")
    
    
    while True:    
        wiederholung = str(input("Willst du nochmal? (Schreibe J/N) "))
        wiederholung = wiederholung.upper()
        
        if wiederholung not in ("J", "N"):
            print("Du hast keine gültige Eingabe gemacht. Bitte tippe J für Ja oder N für Nein!")
        
        elif wiederholung == "J":
            break
        
        elif wiederholung == "N":
            print("Auf Wiedersehen!")
            beenden = True
            break 
    
    
    if beenden:
        break
