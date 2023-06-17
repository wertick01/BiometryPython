import os

class Saver(object):

    def __init__(self, path, sep, format):
        self.path = path
        self.sep = sep
        self.format = format

    def parseFileName(self, name):
        prefix = ""
        if "/" in self.path:
            prefix = "/"
        if "\\" in self.path:
            prefix = "\\"
        
        if prefix != "":
            self.prefix = prefix
            self.dir = self.path + self.prefix + name
        else:
            raise ValueError("Wrong file path")
        
    def makeDir(self, dir):
        if os.path.isdir(dir):
            for file in os.listdir(dir):
                os.remove(os.path.join(dir, file))
            return
        else:
            os.mkdir(dir)
            return

    def save(self, dataframe, numbers, name):
        try:
            path = self.dir + self.prefix + name + numbers + "." + self.format
            if self.format == "csv":
                self.DataFrame = dataframe.to_csv(path, sep = self.sep)
            elif self.format == "xlsx":
                self.DataFrame = dataframe.to_excel(path, sep = self.sep)

        except FileNotFoundError:
            raise FileNotFoundError
        except Exception:
            raise Exception