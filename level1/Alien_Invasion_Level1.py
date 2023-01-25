from os import listdir
import os
from os.path import isfile, join

# main function to decipher the alien's movement
def decipher_aliens(startpos, position, movement):
    
    # direction variable, 1=right, 2=down, 3=left, 0=up
    direction = 1
    move_list = []
    # iterate through list of movements
    for move in range(0, len(movement), 2):
        match movement[move]:

            # if F: check direction and add to X or Y
            case "F":
                match direction:
                    case 1:
                        # add steps to move list
                        for x in range(position[0]+1, position[0]+movement[move+1]+1):
                            move_list.append([x, position[1]])
                        position[0] += movement[move+1]
                    case 2:
                        for x in range(position[1]+1, position[1]+movement[move+1]+1):
                            move_list.append([position[0], x])
                        position[1] += movement[move+1]
                    case 3:
                        for x in range(position[0]-1, position[0]-movement[move+1]-1, -1):
                            move_list.append([x, position[1]])
                        position[0] -= movement[move+1]
                    case 0:
                        for x in range(position[1]-1, position[1]-movement[move+1]-1, -1):
                            move_list.append([position[0], x])
                        position[1] -= movement[move+1]

            # if T: adjust direction accordingly            
            case "T":
                direction = (direction + movement[move+1]) % 4
    
    # turn end position [X, Y] to string and return it
    move_list.insert(0, startpos)
    position = " ".join(map(str, position))
    # move_list = " ".join(map(str, move_list))
    
    print(move_list)
    return move_list

# convert starting position and movements to lists
def convert_to_list(string):
    li = list(string.split(" "))
    li = [s.strip('\n') for s in li]

    #if numbers, turn into integers
    li = [int(i) if i.isnumeric() else str(i) for i in li]
    return li

# function to solve all levels
def process_inputs():
    path = os.path.dirname(os.path.abspath(__file__))
    # # create a list of all files in input directory
    inputfiles = [f for f in listdir("{}\input".format(path)) if isfile(join("{}\input".format(path), f))]
    print(inputfiles)
    # # decipher all files in the directory
    for file in inputfiles:
        input_lvl = open("{}\input\{}".format(path, file), "r")

        # read inputs
        world = input_lvl.readline()
        startpos = input_lvl.readline()
        movement = input_lvl.readline()

        # use previously explained "convert_to_list"-function
        startpos = convert_to_list(startpos)
        position = startpos[:]
        movement = convert_to_list(movement)
        
        move_list = decipher_aliens(startpos, position, movement)

        # write all solutions to preferred output directory
        output_file = open("{}\output\{}".format(path, file), "w+")

        # write in output file, remove brackets and commas
        with open("{}\output\{}".format(path, file), "w+") as f:
            for line in move_list:
                f.write(f"{line}\n")

        with open("{}\output\{}".format(path, file), 'r') as my_file:
            text = my_file.read()
            text = text.replace("[", "")
            text = text.replace("]", "")
            text = text.replace(",", "")

        # write the fixed list (no brackets, no commas) into the final output file
        with open("{}\output\{}".format(path, file), 'w') as my_file:
            my_file.write(text)

# run the code
process_inputs()