
def ImportFile():
    file = open("Day4/input.txt")
    fileLines_string = file.readlines()

    output = []
    for line_count, line in enumerate(fileLines_string):
        if line == "\n":
            line = line.replace("\n", "new card")
        else:
            line = line.replace("\n", "")
        output.append(list(line))
        print(line_count, line)

    # print(output)
    return output


ImportFile()
