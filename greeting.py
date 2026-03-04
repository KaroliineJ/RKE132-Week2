last_name = input("Kirjuta oma perekonnanimi: ")
letter = input("Vali sugu M/N: ")
if letter == "M":
    print(f"Tere, härra {last_name}!")
elif letter == "N":
    print(f"Tere, Proua {last_name}!")
else:
    print(f"Tere tulemast, {last_name} (sugu ei olegi tähtis).") 