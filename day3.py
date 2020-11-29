with open("inputs/day3.txt", 'r') as fh:
    wire1 = fh.readline().strip().split(',')
    wire2 = fh.readline().strip().split(',')

instruction_set = {"L": (-1, 0), "U": (0, 1), "R": (1, 0), "D": (0, -1)}

def get_visited(wire, wire_num, visited):
    pos = (0, 0)
    steps = 0
    for instruction in wire:
        opcode = instruction[0]
        transform = instruction_set[opcode]
        distance = int(instruction[1:])
        for i in range(1, distance + 1):
            visited_x = pos[0] + transform[0] * i
            visited_y = pos[1] + transform[1] * i
            newpos = (visited_x, visited_y)
            steps += 1
            if visited.get(newpos) is not None and wire_num not in visited.get(newpos)["visited_by"]:
                visited[newpos]["visited_by"].append(wire_num) # crossing
                visited[newpos]["steps"] += steps
            else:
                visited[newpos] = {"visited_by": [wire_num], "steps": steps}
        pos = newpos
    return visited


crossings = []
print("getting visited locations for wire1")
wire1_visited = get_visited(wire1, 1, {})
print("getting visited locations for wire2")
wire2_visited = get_visited(wire2, 2, wire1_visited)
print("getting crossing points")
for k, v in wire2_visited.items():
    if len(v["visited_by"]) == 2:
        crossings.append(v["steps"])

#closest_crossing = None
#closest_crossing_distance = None
#print("getting closest crossing")
#for crossing in crossings:
#    manhattan_distance = abs(crossing[0]) + abs(crossing[1])
#    if closest_crossing_distance is None or manhattan_distance < closest_crossing_distance:
#        closest_crossing_distance = manhattan_distance
#        closest_crossing = crossing

#print("closest crossing was at {} with a distance of {}".format(closest_crossing, closest_crossing_distance))
print("Shortest path to crossing was {}".format(min(crossings)))