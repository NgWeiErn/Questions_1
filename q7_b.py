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

# '''Combinatorics'''
# mat_4_4 = populate(4, 4)
# list_paths, list_paths_num = operations_comb(mat_4_4, 19)
# for i1, i2 in zip(list_paths, list_paths_num):
#     print(''.join(i1), " ", i2, sum(i2))
#
# mat_9_9 = populate(9, 9)
# list_paths, list_paths_num = operations_comb(mat_9_9, 72)
# for i1, i2 in zip(list_paths, list_paths_num):
#     print(i1, " ", i2, sum(i2))

'''Dynamic Programming'''
# def operations_dp(mat, target):
#     m = len(mat) - 1
#     n = len(mat[0]) - 1
#     pathList = []
#     dp(mat, target, m, n, i, )
#     return pathList

# def robotPaths(m, n):
#     pathList = []
#     getPaths(m, n, 1, 1, "", pathList)
#     return pathList
#
# def getPaths(m, n, i, j, path, pathList):
#     path = path + "({}, {})".format(i, j)
#     if i == m and j == n:
#         pathList.append(path)
#     elif i > m or j > n:
#         return
#     else:
#         getPaths(m, n, i + 1, j , path, pathList)
#         getPaths(m, n, i , j + 1, path, pathList)
#
# def printRobotPaths(path, row, col, r_idx, c_idx):
#    if ((r_idx == row-1) and (c_idx == col-1)):
#       print(path)
#       return
#
#    if r_idx == row-1:
#       printRobotPaths(path+'D',row,col,r_idx,c_idx+1)
#       return
#
#    if c_idx == col-1 :
#       printRobotPaths(path+'R',row,col,r_idx+1,c_idx)
#       return
#
#    printRobotPaths(path+'D',row,col,r_idx,c_idx+1)
#    printRobotPaths(path+'R',row,col,r_idx+1,c_idx)
#
#
#
# mat_9_1000 = populate(9, 1000)
#
# printRobotPaths("", 9, 9, 0, 0)

# ls_paths, ls_paths_num = operations_dp(mat_4_4, 19)
# for i1, i2 in zip(ls_paths, ls_paths_num):
#     print(i1, " ", i2, sum(i2))


