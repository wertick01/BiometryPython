from reader import Reader
from counter import Counter
from saver import Saver
import tkinter as tk
from tkinter import filedialog

class Run(object):
    def __init__(self, inputFilePath, outputDirPath, sep):
        self.reader = Reader(path=inputFilePath, sep=sep)
        self.name = self.reader.getName()
        self.reader.read()

        if self.reader.error != None:
            raise self.reader.error

        self.counter = Counter(self.reader.DataFrame)

        self.saver = Saver(path=outputDirPath, sep=";", format=self.reader.format)
        self.saver.parseFileName(name=self.name)
        self.saver.makeDir(self.saver.dir)

    def getAllResults(self):
        self.counter.getStatisticsFrom1To11()
        # print(self.counter.from1To11DF)
        # print()
        self.counter.getStatisticsFrom12To18()
        # print(self.counter.from12To18DF)
        # print()
        self.counter.getStatisticsFrom19To20()
        # print(self.counter.from19To20DF)
        # print()
        self.counter.getStatisticsFrom22()
        # print(self.counter.spearman)
        # print()
        self.counter.getStatisticsFrom23To26()
        # print(self.counter.from23To26DF)
        # print()
        self.counter.getStatisticsFrom27To28()
        # print(self.counter.from27To28DF)
        # print()
        self.counter.getStatisticsFrom29To31()
        # print(self.counter.from29To31DF)
        # print()
        self.counter.getStatisticsFrom32To33()
        # print(self.counter.from32To33DF)
        # print()
        self.counter.getStatisticsFrom34To36()
        # print(self.counter.from34To36DF)
        # print()
        self.counter.formatToFinalLine(name=self.name)
        # print(self.counter.finalLine)

    def saveFiles(self):
        self.saver.save(dataframe=self.counter.from1To11DF, numbers="_1_to_11", name=self.name)
        self.saver.save(dataframe=self.counter.from12To18DF, numbers="_12_to_18", name=self.name)
        self.saver.save(dataframe=self.counter.from19To20DF, numbers="_19_to_20", name=self.name)
        self.saver.save(dataframe=self.counter.spearman, numbers="_22", name=self.name)
        self.saver.save(dataframe=self.counter.from23To26DF, numbers="_23_to_26", name=self.name)
        self.saver.save(dataframe=self.counter.from27To28DF, numbers="_27_to_28", name=self.name)
        self.saver.save(dataframe=self.counter.from29To31DF, numbers="_29_to_31", name=self.name)
        self.saver.save(dataframe=self.counter.from32To33DF, numbers="_32_to_33", name=self.name)
        self.saver.save(dataframe=self.counter.from34To36DF, numbers="_34_to_36", name=self.name)
        self.saver.save(dataframe=self.counter.finalLine, numbers="_FINAL", name=self.name)


# функция для считывания исходного файла
def open_file():
    return filedialog.askopenfilename()

# функция для выбора места сохранения файла с ответом
def save_file():
    return filedialog.askdirectory()

# функция для вызова скрипта
def run_script():
    inputFilePath = open_file()
    outputDirPath = save_file()

    run = Run(inputFilePath=inputFilePath, outputDirPath=outputDirPath, sep=";")
    run.getAllResults()

    run.saveFiles()
    return

if __name__ == "__main__":
    root = tk.Tk()

    # кнопки для запуска программы и выбора файлов
    run_button = tk.Button(root, text="Run Script", command=run_script)
    open_button = tk.Button(root, text="Open File", command=open_file)
    save_button = tk.Button(root, text="Save File", command=save_file)

    # размещение кнопок на экране
    open_button.pack(side=tk.LEFT)
    run_button.pack(side=tk.LEFT)
    save_button.pack(side=tk.LEFT)

    root.mainloop()
