import pandas as pd

class Reader(object):

    def __init__(self, path, sep):
        self.path = path
        self.sep = sep
        self.format = path.split(".")[-1:][0]

    def getName(self):
        prefix = ""
        if "/" in self.path:
            prefix = "/"
        if "\\" in self.path:
            prefix = "\\"

        lastPart = self.path.split(prefix)[-1:][0]
        return lastPart.split(".")[0]

    def read(self):
        self.error = None
        self.DataFrame = None

        try:
            if self.format == "csv":
                self.DataFrame = pd.read_csv(self.path, sep = self.sep)
            elif self.format == "xlsx":
                self.DataFrame = pd.read_excel(self.path, sep = self.sep)

        except FileNotFoundError:
            self.error = "File not found."
        except pd.errors.EmptyDataError:
            self.error = "No data"
        except pd.errors.ParserError:
            self.error = "Parse error"
        except Exception:
            self.error = "Some other exception"
