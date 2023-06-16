from reader import Reader
from counter import Counter

class Run(object):
    def __init__(self, path, sep):
        self.reader = Reader(path=path, sep=sep)
        self.reader.read()

        self.counter = Counter(self.reader.DataFrame)

    def getFrom1To11Results(self):
        self.counter.getStatisticsFrom1To11()
        print(self.counter.from1To11DF)
        print()
        self.counter.getStatisticsFrom12To18()
        print(self.counter.from12To18DF)
        print()
        self.counter.getStatisticsFrom22()
        print(self.counter.spearman)


if __name__ == "__main__":
    run = Run("/home/mrred/Загрузки/Korepina_M_O.csv", sep=";")
    run.getFrom1To11Results()
