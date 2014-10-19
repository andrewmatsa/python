file = open("text.txt")
bugs = []
for line in file.readlines():
    if 'bug' in line.lower():
        bugs.append(line)

parser_file = open("report.txt", "w")
parser_file.write("".join(bugs))
parser_file.close()