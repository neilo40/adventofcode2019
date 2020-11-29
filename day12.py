"""
<x=-9, y=-1, z=-1>
<x=2, y=9, z=5>
<x=10, y=18, z=-12>
<x=-6, y=15, z=-7>
"""
from itertools import combinations


class Moon():
    def __init__(self, position):
        super().__init__()
        self.position = position
        self.velocity = [0, 0, 0]

    def apply_gravity(self, other_moon):
        for i in range(3):
            if self.position[i] > other_moon.position[i]:
                self.velocity[i] -= 1
                other_moon.velocity[i] += 1
            elif self.position[i] < other_moon.position[i]:
                self.velocity[i] += 1
                other_moon.velocity[i] -= 1

    def apply_velocity(self):
        for i in range(3):
            self.position[i] += self.velocity[i]

    def calculate_energy(self):
        potential = sum([abs(x) for x in self.position])
        kinetic = sum([abs(x) for x in self.velocity])
        return potential * kinetic

    def __repr__(self):
        return "pos=<x={}, y={}, z={}>, vel=<x={}, y={}, z={}>".format(*self.position, *self.velocity)


def simulate(moons, moon_pairs):
    for moon_pair in moon_pairs:
        moon_pair[0].apply_gravity(moon_pair[1])

    for moon in moons:
        moon.apply_velocity()
        #print(moon)
        

def get_total_energy(moons):
    return sum([x.calculate_energy() for x in moons])


if __name__ == "__main__":
    moons = [Moon(x) for x in [[-9, -1, -1], [2, 9, 5], [10, 18, -12], [-6, 15, -7]]]
    #moons = tuple([Moon(x) for x in [[-1, 0, 2], [2, -10, -7], [4, -8, 8], [3, 5, -1]]])
    moon_pairs = tuple(combinations(moons, 2))

    for step in range(1000):
        #print("After {} steps".format(step + 1))
        simulate(moons, moon_pairs)

    print(get_total_energy(moons))


    

