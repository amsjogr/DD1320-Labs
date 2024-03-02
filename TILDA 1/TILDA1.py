def csv_experiment_funktion(filename):
    import csv
    with open(filename) as file:
        csvreader = csv.reader(file)
        rows = []
        for row in csvreader:
            rows.append(row)
    return rows


class Pokemons:
    def __init__(self, data):
     self.Number = int(data[0])
     self.Name = data[1]
     self.TypeOne = data[2]
     self.TypeTwo = data[3]
     self.Total = int(data[4])
     self.HP = int(data[5])
     self.Attack = int(data[6])
     self.Defense = int(data[7])
     self.SpAttack = int(data[8])
     self.SpDef = int(data[9])
     self.Speed = int(data[10])
     self.Generation = int(data[11])
     self.Legendary = data[12]

    def __repr__(self):
        return "Pokemon number " + str(self.Number) + " is " + self.Name
    def __lt__(self, other):
        if self.HP == other.HP:
            return self.Number < other.Number
        else:
            return self.HP < other.HP


class Pokedex:
    def __init__(self, filepath):
        self.iterering(filepath)

    def iterering(self, filepath):
        data = csv_experiment_funktion(filepath)
        lista = []
        for i in range(1, len(data)):
            lista.append(Pokemons(data[i]))
        self.lista = lista

    def whosthatID(self, number):
        for item in self.lista:
            if item.Number == number:
                return item

    def whosthatname(self, Name):
        for item in self.lista:
            if item.Name == Name:
                return item

fil = 'pokemon.csv'
pokedex = Pokedex(fil)
bulbis = (pokedex.whosthatID(1))
cater = (pokedex.whosthatID(14))
print(bulbis < cater)

rader = []
with open(filnamn) as landfil:
    for rad in landfil:
        rader.insert(0,rad.strip())

rader = []
with open(filnamn) as landfil:
    rad = landfil.readline()
    while rad:
        rader.append(rad.strip())
        rad = landfil.readline()
rader.reverse()




