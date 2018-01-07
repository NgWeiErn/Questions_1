mat = []

with open('input_question_8') as f_in:
    content = f_in.readlines()
content = [x.strip() for x in content]

for line in content:
    list_char = line.split()
    list_int = list(map(int, list_char))
    mat.append(list_int)

rows = len(mat)
columns = len(mat[0])

numlabel = 1

output_mat = [[0 for col in range(columns)] for row in range(rows)]

equivalence_table = [x for x in range(30)] # rows*columns

def doUnion(equivalence_table, a, b):
    while equivalence_table[a] != a:
        a = equivalence_table[a]
    while equivalence_table[b] != b:
        b = equivalence_table[b]
    equivalence_table[b] = a

for row in range(rows):
    for col in range(columns):
        if mat[row][col] == 0:
            continue
        else:
            if row == 0 and col == 0: # if first row, first col
                output_mat[row][col] = numlabel
                numlabel += 1
            elif row == 0 and col != 0: # if first row, not first col
                if mat[row][col-1] != 0:
                    output_mat[row][col] = output_mat[row][col-1]
                else:
                    output_mat[row][col] = numlabel
                    numlabel += 1
            elif row != 0 and col == 0:
                if mat[row-1][col] != 0:
                    output_mat[row][col] = output_mat[row-1][col]
                else:
                    output_mat[row][col] = numlabel
                    numlabel += 1
            else:
                if mat[row-1][col] == 0 and mat[row][col-1] == 0:
                    output_mat[row][col] = numlabel
                    numlabel += 1
                elif mat[row-1][col] == 1 and mat[row][col-1] == 0:
                    output_mat[row][col] = output_mat[row-1][col]
                elif mat[row][col-1] == 1 and mat[row-1][col] == 0:
                    output_mat[row][col] = output_mat[row][col-1]
                else:
                    top = output_mat[row-1][col]
                    left = output_mat[row][col-1]
                    output_mat[row][col] = top

                    if top > left:
                        doUnion(equivalence_table, left, top)
                    elif top < left:
                        doUnion(equivalence_table, top, left)
                    else:
                        continue


for row in range(rows):
    for col in range(columns):
        if output_mat[row][col] != 0:
            output_mat[row][col] = equivalence_table[output_mat[row][col]]

for idx, val in enumerate(equivalence_table):
    print(idx, val)

f_out = open('output_question_8', 'w')

for ls in output_mat:
    for i in ls:
        f_out.write("{} ".format(i))
    f_out.write("\n")

f_out.close()


