class PartyAnimal:
    def __init__(self, name=""):
        self.name = name
        self.x = 0

    def party(self):
        self.x += 1
        print(f"{self.name} party count: {self.x}")

    def load(self):
        pass

if __name__ == "__main__":
    jason = PartyAnimal()

    jason.party()

    jason.load()

    mary = PartyAnimal(name="mary")
    mary.party()

