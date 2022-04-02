class PhotoLib:
    def __init__(self, x: iter = None):
        if x:
            self.photos = list(x)
        else:
            self.photos = list()

    ## returns a list of photos sorted by a given function
    def sort(self, fun):
        photos = list()

        for i in self.photos:
            photos.append(tuple(i, fun(i)))

        photos.sort(key=lambda x: x[1])

        return photos


class Photo:
    def __init__(self, pixel_array: list, name: str):
        self.name = name
        self.pixels = pixel_array
