import pandas as pd
from scipy import stats

class Counter(object):
    def __init__(self, dataframe):
        # self.from1To12DF = pd.DataFrame(columns=[str(i) for i in range(1, 12)])
        self.DataFrame = dataframe
        self.from1To11DF = pd.DataFrame(columns=["Height", "Weight"])
        self.from12To18DF = pd.DataFrame(columns=["Height", "BMI"])
        self.spearman = pd.DataFrame(columns = ['Spearman'])

    def getStatisticsFrom1To11(self):
        self.from1To11DF.loc["var"] = self.DataFrame[["Height", "Weight"]].var()
        self.from1To11DF.loc["mean"] = self.DataFrame[["Height", "Weight"]].mean()
        self.from1To11DF.loc["median"] = self.DataFrame[["Height", "Weight"]].median()
        self.from1To11DF.loc["quantile_25"] = self.DataFrame[["Height", "Weight"]].quantile(0.25)
        self.from1To11DF.loc["quantile_75"] = self.DataFrame[["Height", "Weight"]].quantile(0.75)

    def getIQRParams(self, dataframe, *args):
        q25 = dataframe[[i for i in args]].quantile(0.25)
        q75 = dataframe[[i for i in args]].quantile(0.75)
        cut_off = (q75 - q25) * 1.5
        return q25 - cut_off, q75 + cut_off
    
    def getStatisticsFrom12To18(self):
        lowerHW, upperHW = self.getIQRParams(self.DataFrame, "Height", "Weight")

        newDataIQR = self.DataFrame.copy()
        newDataIQR[newDataIQR["Height"] > upperHW["Height"]] = None
        newDataIQR[newDataIQR["Height"] < lowerHW["Height"]] = None

        self.from12To18DF.Height = [
            newDataIQR[["Height"]].var().values[0],
            newDataIQR[["Height"]].mean().values[0],
            newDataIQR[["Height"]].median().values[0],
        ]

        newDataIQR[newDataIQR["Weight"] > upperHW["Weight"]] = None
        newDataIQR[newDataIQR["Weight"] < lowerHW["Weight"]] = None
        newDataIQR["BMI"] = newDataIQR["Weight"] / (newDataIQR["Height"]*0.01)**2

        lowerBMI, upperBMI = self.getIQRParams(newDataIQR, "BMI")
        newDataIQR[newDataIQR["BMI"] > upperBMI["BMI"]] = None
        newDataIQR[newDataIQR["BMI"] < lowerBMI["BMI"]] = None

        self.from12To18DF.BMI = [
            newDataIQR[["BMI"]].var().values[0],
            newDataIQR[["BMI"]].mean().values[0],
            newDataIQR[["BMI"]].median().values[0],
        ]

    def getStatisticsFrom22(self):
        dataForSpearman = self.DataFrame.copy()
        dataForSpearman[["Physical activity"]] = dataForSpearman[["Physical activity"]].replace({
            'Low': 1, 
            'Moderate': 2, 
            'High': 3,
        })

        self.spearman.loc["22"] = stats.spearmanr(
            dataForSpearman["Physical activity"], 
            dataForSpearman["Maximum degree of disk degeneration in lumbar spine"],
        )[0]
