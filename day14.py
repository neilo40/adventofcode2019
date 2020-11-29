import math


class Chemical():
    def __init__(self, qty, name):
        super().__init__()
        self.name = name
        self.qty = int(qty)

    def __repr__(self):
        return "{} ({})".format(self.name, self.qty)


class Reaction():
    def __init__(self, formula):
        super().__init__()
        reagents, product = formula.strip().split("=>")
        
        self.product = Chemical(*product.strip().split())
        self.reagents = [Chemical(*x.strip().split()) for x in reagents.split(',')]

    def __repr__(self):
        return "{} from {}".format(self.product, self.reagents)


def get_ore_needed(product, reaction_map, scaling_factor):
    reaction = reaction_map[product.name]
    ore_needed = 0
    for reagent in reaction.reagents:
        total_reagents_needed = reagent.qty * scaling_factor
        if reagent.name == "ORE":
            return total_reagents_needed
        else:
            reagent_producer = reaction_map[reagent.name]
            print("Need {} {}.  Reaction for {} produces {}".format(total_reagents_needed, reagent.name, reagent.name, reagent_producer.product.qty))
            multiple_needed = math.ceil(total_reagents_needed / reagent_producer.product.qty)
            print("  Scaling reaction for {} by {} to produce {}".format(reagent.name, multiple_needed, reagent_producer.product.qty*multiple_needed))
            ore_needed += get_ore_needed(reagent, reaction_map, multiple_needed)
    return ore_needed

            
if __name__ == "__main__":
    with open("inputs/day14.txt", 'r') as fh:
        formulae = fh.readlines()

    reaction_map = {}

    for formula in formulae:
        reaction = Reaction(formula)
        reaction_map[reaction.product.name] = reaction

    print(get_ore_needed(reaction_map["FUEL"].product, reaction_map, 1))