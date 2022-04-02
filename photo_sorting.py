import color


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

        photos.sort(key=lambda x: x[1], reverse = True)

        return photos


class Photo:
    def __init__(self, pixel_array: list, name: str):
        self.name = name
        self.pixels = pixel_array
        self.avgcol = self.avgColor()

    def greyscale(self):
        grey = list()
        for i in self.pixels:
            grey.append(list())
            for j in i:
                col = (j.red + j.green + j.blue) / 3
                grey[-1].append(color.Color(col, col, col))

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




