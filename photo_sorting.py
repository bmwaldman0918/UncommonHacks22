import color
import numpy


class PhotoLib:
    def __init__(self, x: iter = None):
        if x:
            self.photos = list(x)
        else:
            self.photos = list()

    # returns a list of photos sorted by a given function
    def sort(self, fun):
        sorted_photos = list(self.photos)

        sorted_photos.sort(key=fun, reverse=False)

        return sorted_photos


class Photo:
    def __init__(self, pixel_array, name: str):
        self.name = name
        self.pixels = list()
        if pixel_array is list:
            self.pixels = pixel_array
        else:
            self.pixels = numpy.ndarray.tolist(pixel_array)
            for row in self.pixels:
                for col in range(len(row)):
                    row[col] = color.Color(row[col][0], row[col][1], row[col][2])

    def greyscale(self):
        avg, count = 0, 0
        for i in self.pixels:
            for j in i:
                grey = (j.red + j.green + j.blue) / 3
                avg += color.colDistance(j, grey)
                count += 1

        return avg / count

    @staticmethod
    def comp_by_col(c: color.Color):
        return lambda x: x.col_dist(c)

    def col_dist(self, c):
        total_dist = 0.0
        count = 0
        for row in self.pixels:
            for pixel in row:
                count += 1
                total_dist += color.colDistance(c, pixel)
        try:
            # print("avg Dist: " + str(total_dist / count))
            return total_dist / count
        except ZeroDivisionError:
            # print("total Dist: " + str(total_dist))
            return total_dist
