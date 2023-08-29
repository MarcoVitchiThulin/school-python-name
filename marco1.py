name = input("Vad är ditt namn? ")
print(f"Hej {name}!")
age = int(input("Hur gammal är du? "))
if age > 16:
    print("Du måste vara erfaren")
else:
    print("Du kan bli äldre") if age < 16 else print("Du har en perfekt ålder")