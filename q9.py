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

class Point(object):

    def __init__(self, x, y):
        self.Point = (x, y)

    def __str__(self):
        return str(self.Point)

    def getX(self):
        return self.Point[0]

    def getY(self):
        return self.Point[1]

    def getPoint(self):
        return self.Point

class Polygon():

    def __init__(self, points):
        self.Vertices = tuple(points)

    def __str__(self):
        string = ""
        for vertex in self.Vertices:
            string += "{}, ".format(vertex)
            if vertex == self.Vertices[len(self.Vertices)-1]:
                string = string[:-2]
        return string

    def getVertex(self, i):
        return self.Vertices[i]

    def getLength(self):
        return len(self.Vertices)

def point_in_poly(point, poly):
    n = poly.getLength()
    p_x, p_y = point.getX(), point.getY()

    # check if point is a vertex
    for i in range(n):
        vertex = poly.getVertex(i)
        if p_x == vertex.getX() and p_y == vertex.getY():
            return "inside"

   # check if point is on a horizontal boundary
    for i in range(n+1)[1:]:
        v1 = poly.getVertex(i-1)
        v2 = poly.getVertex(i%n)
        if v1.getY() == v2.getY() == point.getY() and \
                        point.getX() > min(v1.getX(), v2.getX()) and \
                        point.getX() < max(v1.getX(), v2.getX()):
            return "inside"

    inside = False

    for i in range(n+1)[1:]:
        v1, v2 = poly.getVertex(i-1), poly.getVertex(i % n)
        v1_x, v1_y, v2_x, v2_y = v1.getX(), v1.getY(), v2.getX(), v2.getY()
        if p_y > min(v1_y, v2_y):
            if p_y <= max(v1_y, v2_y):
                if p_x <= max(v1_x, v2_x):
                    if v1_y != v2_y:
                        xints = (p_y - v1_y)*(v2_x - v1_x)/(v2_y - v1_y) + v1_x
                    if v1_x == v2_x or p_x <= xints:
                        inside = not inside

    if inside:
        return "inside"
    else:
       return "outside"

with open('input_question_9_polygon') as f_in:
    content = f_in.readlines()
content = [x.strip() for x in content]

ls = []
for line in content:
    list_char = line.split()
    list_int = list(map(int, list_char))
    point = Point(list_int[0], list_int[1])
    ls.append(point)

poly = Polygon(ls)
del ls

with open('input_question_9_points') as f_in:
    content = f_in.readlines()
content = [x.strip() for x in content]

points = []
for line in content:
    list_char = line.split()
    list_int = list(map(int, list_char))
    point = Point(list_int[0], list_int[1])
    points.append(point)

f_out = open('output_question_9', 'w')
for point in points:
    # print("{0: <2}".format(point.getX()), "{0: <2}".format(point.getY()), point_in_poly(point, poly))
    f_out.write(str(point.getX()) + " " +
                str(point.getY()) + " " +
                str(point_in_poly(point, poly)) +
                "\n")
f_out.close()
