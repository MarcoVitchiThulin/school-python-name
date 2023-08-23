q = input("Vad är ditt namn? ")
q = int(input(f"Hej, välkommen {q}! Hur gammal är du? "))
if q < 16:
    print("Meh, du kan bli äldre.")
elif q > 16:
    print("Oj, du måste vara erfaren!")
else:
    print("Du har en perfekt ålder!")