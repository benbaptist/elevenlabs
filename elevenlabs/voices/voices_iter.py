class VoicesIter:
    def __init__(self, voices):
        self.list = voices.list

        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        i = self.i
        self.i += 1

        try:
            return self.list[i]
        except IndexError:
            raise StopIteration
