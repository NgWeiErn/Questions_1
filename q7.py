import itertools

def populate(m, n):
    mat = [[y + 1 for x in range(n)] for y in range(m)]

    return mat

def unique_permutations(r, d):
    """Create generator containing all unique permutations with `r` R'es and `D` D's."""
    total = r + d
    for indices in itertools.combinations(range(total), d):
        lst = ['R']*total
        for index in indices:
            lst[index] = 'D'
        yield lst

def operations_comb(mat, target):

    m = len(mat)
    n = len(mat[0])
    unique_perm = unique_permutations(m-1,n-1)
    list_paths = []

    for ls in unique_perm:
        list_num = []
        list_num.append(mat[0][0])
        sum = mat[0][0]
        i = 0
        j = 0
        for char in ls:
            if char == 'D':
                i += 1
                sum += mat[i][j]
                list_num.append(mat[i][j])
            elif char == 'R':
                j += 1
                sum += mat[i][j]
                list_num.append(mat[i][j])
        if sum == target:
            list_paths.append(ls)

    return list_paths

'''Combinatorics'''
mat_4_4 = populate(4, 4)
list_paths = operations_comb(mat_4_4, 19)
for path in list_paths:
    print("19 ", ''.join(path))

mat_9_9 = populate(9, 9)

f_out = open('output_question_7', 'w')

list_paths = operations_comb(mat_9_9, 65)
for path in list_paths:
    f_out.write("65 " + ''.join(path) + "\n")
f_out.write("\n")

list_paths = operations_comb(mat_9_9, 72)
for path in list_paths:
    f_out.write("72 " + ''.join(path) + "\n")
f_out.write("\n")

list_paths = operations_comb(mat_9_9, 90)
for path in list_paths:
    f_out.write("90 " + ''.join(path) + "\n")
f_out.write("\n")

list_paths = operations_comb(mat_9_9, 110)
for path in list_paths:
    f_out.write("110 " + ''.join(path) + "\n")

f_out.close()
