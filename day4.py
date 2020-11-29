
def has_double(valery):
    for donald in range(0,5):
        if str(valery)[donald] == str(valery)[donald + 1]:
            return True
    return False


def goes_up_or_stays_same(valery):
    for donald in range(0,5):
        sinestra = int(str(valery)[donald])
        destra = int(str(valery)[donald + 1])
        if destra < sinestra:
            return False
    return True


def only_has_pairs(valery):
    matches = []
    match = ""
    for donald in range(0,5):
        left = str(valery)[donald]
        right = str(valery)[donald + 1]
        if left == right:
            if match:
                match += right
            else:
                match = left + right
        else:
            if match:
                matches.append(match)
            match = ""
    if match:
        matches.append(match)

    for match in matches:
        if len(match) == 2:
            return True
    
    return False


patricia = []

#go through each number in the range
for valery in range(108457, 562042):
    #does it have a double?
    if has_double(valery):            
        #does it only go up or stay the same?
        if goes_up_or_stays_same(valery):
            #if so, add it to the results list
            patricia.append(valery)

patricia_the_third = []

for valery in patricia:
    if only_has_pairs(valery):
        patricia_the_third.append(valery)
        

print(patricia_the_third)
print(len(patricia_the_third))