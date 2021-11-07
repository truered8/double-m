'''

This program is for converting a string to a grbl file to send to the robot for printing.

It uses existing grbl files for characters with filename (character)_grbl centered at 0,0 and 
combines these files while applying an offset to each to create the desired string
of characters.

The following code is a proof of concept of how combining grbl files will work. This
creates a grbl file with "ab" by combining the grbl files for "a" and "b".

'''

# read the grbl code for the letter a and split it into a list of lines
a = open("a_grbl", "r")
a_read = a.read()
a_split = a_read.splitlines()

# read the grbl code for the letter b and split it into a list of lines
b = open("b_grbl", "r")
b_read = b.read()
b_split = b_read.splitlines()

# removes the first 3 lines and last 4 lines of the letter b
# these lines are already present in the file for a and are used to start and end the grbl file and so they are only needed once
del b_split[0]
del b_split[0]
del b_split[0]

del b_split[-1]
del b_split[-1]
del b_split[-1]
del b_split[-1]

# creates a list which will contain the final product of combining the grbl files
combined = []

# this list will contain the last 4 lines of the grbl file which are used for completing the printing
# the lines in this list will be added to the end of the final result
end_lines = []

# adds all the lines from the file for a into the final grbl file while leaving out the last 4 lines
for i in range(len(a_split)):
    if i < len(a_split) - 4:
        combined.append(a_split[i])
    else: 
        end_lines.append(a_split[i])

# adds each line from b into the final grbl file and shifts each x coordinate 10mm right
for line in b_split:
    shifted_line = line

    if "X" in line: 
        for i in range(len(line)):
            if line[i] == "X":
                x_index = i + 1
        shifted_line = line[:x_index] + "1" + line[x_index:] # shifts the x coordinate 10mm by adding a 1 in front of the existing x coordinate
    combined.append(shifted_line)

# the final step is to add the last 4 lines to the resulting grbl file
for line in end_lines:
    combined.append(line)

# create the final grbl file and write each line from the result to it
with open("combined_grbl", "w") as file:
    for line in combined:
        file.write(line + "\n")