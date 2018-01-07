mat = []

with open('input_question_8') as f_in:
    content = f_in.readlines()
content = [x.strip() for x in content]

for line in content:
    list_char = line.split()
    list_int = list(map(int, list_char))
    mat.append(list_int)

f_out = open('output_question_8', 'w')

print("Input matrix:")
f_out.write("Input matrix:\n")
for ls in mat:
    print(ls)
    f_out.write(str(ls) + "\n")

rows = len(mat)
columns = len(mat[0])

numlabel = 1

output_mat = [[0 for col in range(columns)] for row in range(rows)]

# equivalence_table = [x for x in range(30)] # rows*columns

# def doUnion(equivalence_table, a, b):
#     while equivalence_table[a] != a:
#         a = equivalence_table[a]
#     while equivalence_table[b] != b:
#         b = equivalence_table[b]
#     equivalence_table[b] = a

equivalence_dict = {}
equiv = 1

def in_dict(numlabel):
    for key, value in equivalence_dict.items():
        if numlabel in value:
            return True
    return False

def add_key_and_values(equiv, *values):
    equivalence_dict[equiv] = []
    for value in values:
        equivalence_dict[equiv].append(value)

def add_values(value_in, value_add):
    for key, value in equivalence_dict.items():
        if value_in in value:
            dict[key].append(value_add)

# if one value only
        # if inside temp continue
        # else add key and value, increase key


for row in range(rows):
    for col in range(columns):
        if mat[row][col] == 0:
            continue
        else:
            if row == 0 and col == 0: # if first row, first col
                output_mat[row][col] = numlabel
                if not in_dict(numlabel):
                    add_key_and_values(equiv, numlabel)
                    equiv += 1
                numlabel += 1
            elif row == 0 and col != 0: # if first row, not first col
                if mat[row][col-1] != 0:
                    output_mat[row][col] = output_mat[row][col-1]
                else:
                    output_mat[row][col] = numlabel
                    if not in_dict(numlabel):
                        add_key_and_values(equiv, numlabel)
                        equiv += 1
                    numlabel += 1
            elif row != 0 and col == 0:
                if mat[row-1][col] != 0:
                    output_mat[row][col] = output_mat[row-1][col]
                else:
                    output_mat[row][col] = numlabel
                    if not in_dict(numlabel):
                        add_key_and_values(equiv, numlabel)
                        equiv += 1
                    numlabel += 1
            else:
                if mat[row-1][col] == 0 and mat[row][col-1] == 0:
                    output_mat[row][col] = numlabel
                    if not in_dict(numlabel):
                        add_key_and_values(equiv, numlabel)
                        equiv += 1
                    numlabel += 1
                elif mat[row-1][col] == 1 and mat[row][col-1] == 0:
                    output_mat[row][col] = output_mat[row-1][col]
                elif mat[row][col-1] == 1 and mat[row-1][col] == 0:
                    output_mat[row][col] = output_mat[row][col-1]
                else:
                    top = output_mat[row-1][col]
                    left = output_mat[row][col-1]
                    output_mat[row][col] = top

                    # if two values
        # if value1 not in temp AND value2 not in temp, add new key and add both value, increase key
        # if value1 not in temp AND value2 in temp, add value1 to key of value2
        # if value1 in temp AND value2 not in temp, add value2 to key of value1
        # if value1 in temp and value2 in temp, continue
                    if not in_dict(top) and not in_dict(left):
                        add_key_and_values(equiv, top, left)
                        equiv += 1
                    elif not in_dict(top) and in_dict(left):
                        add_values(left, top)
                    elif in_dict(top) and not in_dict(left):
                        add_values(top, left)
                    else:
                        if top > left:


                    # if top > left:
                    #     doUnion(equivalence_table, left, top)
                    # elif top < left:
                    #     doUnion(equivalence_table, top, left)
                    # else:
                    #     continue


def retrieve_equivalence(value):
    for key, value_arr in equivalence_dict.items():
        if value in value_arr:
            return key

for row in range(rows):
    for col in range(columns):
        if output_mat[row][col] != 0:
            output_mat[row][col] = retrieve_equivalence(output_mat[row][col])



print("Output matrix:")
f_out.write("Output matrix:\n")
for ls in output_mat:
    f_out.write("[")
    for i in ls:
        print("{0:2}".format(i), end=',')
        f_out.write("{0:2},".format(i))
    print("")
    f_out.write("]\n")

f_out.close()


