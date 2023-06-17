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
        self.counter.getStatisticsFrom19To20()
        print(self.counter.from19To20DF)
        print()
        self.counter.getStatisticsFrom22()
        print(self.counter.spearman)
        print()
        self.counter.getStatisticsFrom23To26()
        print(self.counter.from23To26DF)
        print()
        self.counter.getStatisticsFrom27To28()
        print(self.counter.from27To28DF)
        print()
        self.counter.getStatisticsFrom29To31()
        print(self.counter.from29To31DF)
        print()
        self.counter.getStatisticsFrom32To33()
        print(self.counter.from32To33DF)
        print()
        self.counter.getStatisticsFrom34To36()
        print(self.counter.from34To36DF)
        print()


if __name__ == "__main__":
    run = Run("/home/mrred/Загрузки/Korepina_M_O.csv", sep=";")
    run.getFrom1To11Results()
