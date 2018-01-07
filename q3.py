# input

mat = []

with open('input_question_3') as f_in:
    content = f_in.readlines()
content = [x.strip() for x in content]

for line in content:
    list_char = line.split()
    list_int = list(map(int, list_char))
    mat.append(list_int)

f_out = open('input_question_3_formatted', 'w')

for i in range(len(mat)):
    for j in range(len(mat[i])):
        f_out.write("{0:3}".format(mat[i][j]))
        if j != (len(mat[i]) - 1):
            f_out.write(" ")
        else:
            f_out.write("\n")

f_out.close()
# logic

r_init = len(mat) # number of rows = 10
c_init = len(mat[0]) # number of columns = 20

# create new 2D-list, initialized with zeros

mat_new = [[0 for col in range(c_init)] for row in range(r_init)]

# pad original 2D-list with zeros

# adds an additional row of 20 zeros at the top and at the bottom
mat.insert(0,[0 for x in range(c_init)]) # first row
mat.append([0 for x in range(c_init)]) # last row

# iterate through every row, adding a zero at the beginning and at the end
for ls in mat:
    ls.insert(0,0) # first column
    ls.append(0)    # last column

for i in range(1, r_init + 1):
    for j in range(1, c_init + 1):
        mat_new[i-1][j-1] = max(mat[i-1][j-1], mat[i-1][j], mat[i-1][j+1], mat[i][j-1], mat[i][j],
                            mat[i][j+1], mat[i+1][j-1], mat[i+1][j], mat[i+1][j+1])

# output
f_out = open('output_question_3', 'w')

for i in range(len(mat_new)):
    for j in range(len(mat_new[i])):
        f_out.write(str(mat_new[i][j]))
        if j != (len(mat_new[i]) - 1):
            f_out.write(" ")
        else:
            f_out.write("\n")

f_out.close()
