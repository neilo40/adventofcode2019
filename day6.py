with open("inputs/day6.txt", 'r') as orbit_fh:
    orbits = orbit_fh.readlines()
orbits = [x.strip() for x in orbits]


class Lump:
    def __init__(self, name):
        self.name = name
        self.distance = 0
        self.is_orbiting = []
        self.is_orbited_by = []
        self.ancestry = []

    def __repr__(self):
        return self.name

com = Lump("COM")
all_lumps = {"COM": com}

for orbit in orbits:
    lump, orbiting_lump = orbit.split(')')
    if not lump in all_lumps:
        all_lumps[lump] = Lump(lump)
    if not orbiting_lump in all_lumps:
        all_lumps[orbiting_lump] = Lump(orbiting_lump)

    all_lumps[lump].is_orbited_by.append(all_lumps[orbiting_lump])
    all_lumps[orbiting_lump].is_orbiting.append(all_lumps[lump])


def set_distances(distance_so_far, lump):
    lump.distance = distance_so_far
    for l in lump.is_orbited_by:
        l.ancestry = list(lump.ancestry)
        l.ancestry.append(lump)
        set_distances(distance_so_far + 1, l)

set_distances(0, all_lumps["COM"])

total_orbits = 0
for lump in all_lumps.values():
    total_orbits += lump.distance

print(total_orbits)

for ancestor in reversed(all_lumps["SAN"].ancestry):
    if ancestor in all_lumps["YOU"].ancestry:
        transfers_needed = (all_lumps["YOU"].distance - ancestor.distance - 1) + (all_lumps["SAN"].distance - ancestor.distance - 1)
        print(transfers_needed)
        break