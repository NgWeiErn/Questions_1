# dict = {1: ['a'], 2: ['b']}
#
# if 'a' in dict.values():
#     print('b')
#
# dict[3] = []
#
# dict[3].append('c')
#
# print(len(dict[3]))
#
#
# def add_key_and_values(equiv, *values):
#     dict[equiv] = []
#     print(values[0])
#     print(values[1])
#     for value in values:
#         dict[equiv].append(value)
#
# add_key_and_values(3, 'c', 'd')
#
# print(dict)
#
# print(dict.values())
#
# for equiv, value in dict.items():
#     if 'c' in value:
#         print(equiv)


# import matplotlib.pyplot as plt
# from shapely.geometry.polygon import LinearRing
# import matplotlib.ticker as ticker
#
# ring_poly = LinearRing([[4,3],[2,6],[3,12],[2,17],[5,20],[9,21],[14,19],[20,14],[18,3],[11,7]])
# x_poly, y_poly = ring_poly.xy
#
# ring = LinearRing([[7,11],[10,14],[11,4],[12,21],[16,3],[16,10],[17,4],[18,7],[18,17],[20,7]])
# x, y = ring.xy
#
# fig = plt.figure(1, figsize=(15,15), dpi=100)
# ax = fig.add_subplot(111)
# ax.plot(x_poly, y_poly)
# ax.plot(x, y, 'ro')
# ax.set_title('Polygon Edges')
#
# tick_spacing = 1
# ax.xaxis.set_major_locator(ticker.MultipleLocator(tick_spacing))
# ax.yaxis.set_major_locator(ticker.MultipleLocator(tick_spacing))
# ax.set_aspect(1)
# plt.show()

# mat = []
#
# with open('input_question_3') as f_in:
#     content = f_in.readlines()
# content = [x.strip() for x in content]
#
# for line in content:
#     list_char = line.split()
#     list_int = list(map(int, list_char))
#     mat.append(list_int)

# logic

# r_init = len(mat)
# c_init = len(mat[0])

# create new 2D-list, initialized with zeros

# mat_new = [[0 for col in range(c_init)] for row in range(r_init)]
#
# print(r_init)
# print(c_init)
#
# for row in mat_new:
#     print(row)

# print(max(10,10))

import networkx as nx

G=nx.MultiGraph()
G.add_node('A',role='manager')
G.add_edge('A','B',relation = 'friend')
G.add_edge('A','C', relation = 'business partner')
G.add_edge('A','B', relation = 'classmate')
G.node['A']['role'] = 'team member'
G.node['B']['role'] = 'engineer'

print(G)
