'''

This program is for converting a string to a grbl file to send to the robot for printing.

It uses existing grbl files for characters with filename (character)_block_0001 centered at 0,0 and 
combines these files while applying an offset to each to create the desired string
of characters.

The following function combines all the characters into a single line.

TODO - create files with multiple lines instead of combining entire string into one line
TODO - calibrate grbl files with hardware to ensure that the files will be printed correctly
'''

def convert_to_grbl(text):
    result = []
    end_lines = []
    shift_difference = 6
    shift = 0

    for i in range(len(text)):
        # since we do not have a file for a space character just apply the shift
        if text[i] == " ":
            shift += shift_difference
        elif i == 0:
            # read the grbl file for the first character and split it into a list of lines
            char = open("grbl_files/"+text[0]+"_block_0001", "r")
            char_read = char.read()
            char_split = char_read.splitlines()

            # adds all the lines from the file for a into the final grbl file while leaving out the last 4 lines
            for i in range(len(char_split)):
                if i < len(char_split) - 4:
                    result.append(char_split[i])
                else: 
                    end_lines.append(char_split[i])
        else:
            # offset the next character
            if text[i-1] == "i": # smaller offset for i since it is thinner
                shift += shift_difference-4
            elif text[i-1] == "w": # larger offset for w since it is wider
                shift += shift_difference+3
            else:
                shift += shift_difference

            # read the grbl file for the character and split it into a list of lines
            char = open("grbl_files/"+text[i]+"_block_0001", "r")
            char_read = char.read()
            char_split = char_read.splitlines()

            # removes the first 3 lines and last 4 lines of the letter b
            # these lines are already present in the file for a and are used to start and end the grbl file and so they are only needed once
            del char_split[0]
            del char_split[0]
            del char_split[0]

            del char_split[-1]
            del char_split[-1]
            del char_split[-1]
            del char_split[-1]

            # adds each line from the character into the final grbl file 
            # and shifts each x coordinate 
            for line in char_split:
                shifted_line = line

                if "X" in line: 
                    # find where the x value starts
                    for i in range(len(line)):
                        if line[i] == "X":
                            x_index = i + 1
                    
                    # find where the x value ends
                    for i in range(len(line) - x_index):
                        if line[x_index+i] == " ":
                            num_end_index = x_index+i
                    
                    # shift the x coordinate right by the shift
                    shifted_line = line[:x_index] + str(float(line[x_index:num_end_index])+shift) + line[num_end_index:] 
                result.append(shifted_line)

    # the final step is to add the last 4 lines to the resulting grbl file
    for line in end_lines:
        result.append(line)

    # create the final grbl file and write each line from the result to it
    with open("result_grbl", "w") as file:
        for line in result:
            file.write(line + "\n")

# testing the function by combining the alphabet into one grbl file
convert_to_grbl("abcdefghijklmnopqrstuvwxyz")