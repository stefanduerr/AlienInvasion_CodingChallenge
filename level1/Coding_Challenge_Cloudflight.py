from os import listdir
from os.path import isfile, join

# main function to decipher the alien's movement
def decipher_aliens(position, movement):
    
    # direction variable, 1=right, 2=down, 3=left, 0=up
    direction = 1

    # iterate through list of movements
    for move in range(0, len(movement), 2):
        match movement[move]:

            # if F: check direction and add to X or Y
            case "F":
                match direction:
                    case 1:
                        position[0] += movement[move+1]
                    case 2:
                        position[1] += movement[move+1]
                    case 3:
                        position[0] -= movement[move+1]
                    case 0:
                        position[1] -= movement[move+1]

            # if T: adjust direction accordingly            
            case "T":
                direction = (direction + movement[move+1]) % 4
    
    # turn end position [X, Y] to string and return it
    position = " ".join(map(str, position))
    return position

# convert starting position and movements to lists
def convert_to_list(string):
    li = list(string.split(" "))
    li = [s.strip('\n') for s in li]

    #if numbers, turn into integers
    li = [int(i) if i.isnumeric() else str(i) for i in li]
    return li

# function to solve all levels
def process_inputs():

    # create a list of all files in input directory
    inputfiles = [f for f in listdir("input/") if isfile(join("input/", f))]

    # decipher all files in the directory
    for file in inputfiles:
        input_lvl = open("input\{}".format(file), "r")

        startpos = input_lvl.readline()
        movement = input_lvl.readline()

        # use previously explained "convert_to_list"-function
        startpos = convert_to_list(startpos)
        movement = convert_to_list(movement)
        
        # write all solutions to preferred output directory
        output_file = open("output\{}".format(file), "w+")
        output_file.write(decipher_aliens(startpos, movement))

# run the code
process_inputs()