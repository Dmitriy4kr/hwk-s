class BeeElephant:
    def __init__(self, part_bee, part_elephant):
        self.part_bee = part_bee
        self.part_elephant = part_elephant

    def fly(self):
        return self.part_bee >= self.part_elephant

    def trumpet(self):
        return "tu-tu-doo-doo" if self.part_elephant >= self.part_bee else "wzzzz"

    def eat(self, meal, value):
        if meal == "nectar":
            self.part_elephant = self.part_elephant - value if self.part_elephant - value >= 0 else 0
            self.part_bee = self.part_bee + value if self.part_bee + value <= 100 else 100
        elif meal == "grass":
            self.part_bee = self.part_bee - value if self.part_bee - value >= 0 else 0
            self.part_elephant = self.part_elephant + value if self.part_elephant + value <= 100 else 100

    def __str__(self):
        return f"BeeElephant(bee={self.part_bee}, elephant={self.part_elephant})"


be_el = BeeElephant(40, 25)
print(be_el.fly())
print(be_el.trumpet())

be_el.eat("nectar", 40)
print(be_el)
be_el.eat("grass", 35)
print(be_el)