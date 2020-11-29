if __name__ == "__main__":
    with open("inputs/day8.txt", 'r') as fh:
        raw_input = fh.readline().strip()

    # get all layers from input
    layers = []
    layer = []
    row_count = 0

    for row_start in range(0, len(raw_input), 25):
        row = raw_input[row_start:row_start + 25]
        layer.append(list(row))

        if row_count == 5:
            layers.append(layer)
            layer = []
            row_count = 0
        else:
            row_count += 1

    # get layer with minimum number of zeroes
    min_zeroes = 200
    layer_min_zeroes = None

    for layer in layers:
        zero_count = 0
        for row in layer:
            for pixel in row:
                if pixel == '0':
                    zero_count += 1
        if zero_count < min_zeroes:
            min_zeroes = zero_count
            layer_min_zeroes = layer

    # get num 1's * num 2's
    one_count = 0
    two_count = 0
    for row in layer_min_zeroes:
        for pixel in row:
            if pixel == '1':
                one_count += 1  
            elif pixel == '2':
                two_count += 1

    # render image
    # 0 = black, 1 = white, 2 = transparent
    image = layers[0]
    for layer in layers[1:]:
        for row in range(6):
            for pixel in range(25):
                if image[row][pixel] == '2':
                    image[row][pixel] = layer[row][pixel]
                if image[row][pixel] == '0':
                    image[row][pixel] = ' '
                if image[row][pixel] == '1':
                    image[row][pixel] = u'\U0001f4a9'

    for row in image:
        print("".join(row))