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
        photos = list()

        for i in self.photos:
            photos.append(tuple(i, fun(i)))

        photos.sort(key=lambda x: x[1], reverse=True)

        return photos


class Photo:
    def __init__(self, pixel_array, name: str):
        self.name = name
        if pixel_array is list:
            self.pixels = pixel_array
        elif pixel_array is numpy.ndarray:
            self.pixels = numpy.aslist(pixel_array)
            for row in self.pixels:
                for col in range(len(row)):
                    row[col] = color(row[col][0], row[col][1], row[col][2])

        self.avgcol = self.avgColor()



    def greyscale(self):
        avg, count = 0
        for i in self.pixels:
            for j in i:
                grey = (j.red + j.green + j.blue) / 3
                avg += color.colDistance(j, grey)
                count += 1

        return avg / count

    def avgColor(self):
        avgr = 0
        avgg = 0
        avgb = 0
        count = 0
        for pixel in self.pixels:
            avgr += pixel.red
            avgg += pixel.green
            avgb += pixel.blue
            count += 1
        avgr /= count
        avgb /= count
        avgg /= count
        return color.Color(avgr, avgb, avgg)


def compPhoto(c, p1):
    return color.colDistance(c, p1.avgcol)




