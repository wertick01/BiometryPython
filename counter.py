import pandas as pd
from scipy import stats
import sklearn.linear_model as lm
from sklearn.feature_selection import f_regression
from statsmodels.formula.api import ols
import statsmodels.api as stm

class Counter(object):

    def __init__(self, dataframe):
        # self.from1To12DF = pd.DataFrame(columns=[str(i) for i in range(1, 12)])
        self.DataFrame = dataframe
        self.from1To11DF = pd.DataFrame(columns=["Height", "Weight"])
        self.from12To18DF = pd.DataFrame(columns=["Height", "BMI"])
        self.from19To20DF = pd.DataFrame(columns=["results"])
        self.spearman = pd.DataFrame(columns = ["Spearman"])
        self.from23To26DF = pd.DataFrame(columns=["results"])
        self.from27To28DF = pd.DataFrame(columns=["T-Test"])
        self.from29To31DF = pd.DataFrame(columns=["Chi^2"])
        self.from32To33DF = pd.DataFrame(columns=["Mann-Uitney"])
        self.from34To36DF = pd.DataFrame(columns=["ANOVA"])
        self.finalLine = pd.DataFrame(columns=[str(i) for i in range(1, 38)])
        # self.finalLine = pd.DataFrame(columns=["result"])

        self.real2010 = {
            "Armenian": 0.84,#
            "Bashkir": 1.26,#
            "Tatar": 4.21,#
            "Ukrainian": 1.53,#
            "German": 0.32,#
            "Chuvash": 1.15,#
            "Chechen": 1.13,#
            "Kazakh": 0.51,#
            "Yakut": 0.38,#
            "Russian": 87.97,#
            "Buryat": 0.36,#
            "Uzbek": 0.24,#
        }

        self.real2021 = {
            "Armenian": 0.81,#
            "Bashkir": 1.35,#
            "Tatar": 3.97,#
            "Ukrainian": 0.74,#
            "German": 0.18,#
            "Chuvash": 0.91,#
            "Chechen": 1.44,#
            "Kazakh": 0.55,#
            "Yakut": 0.43,#
            "Russian": 88.97,#
            "Buryat": 0.38,#
            "Uzbek": 0.27,#
        }

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

        anovaDF = newDataIQR[newDataIQR["Subsample"] == 1]
        self.anovaDF = anovaDF[["BMI", "LDDD", "Physical activity"]]

        lowerBMI, upperBMI = self.getIQRParams(newDataIQR, "BMI")
        newDataIQR[newDataIQR["BMI"] > upperBMI["BMI"]] = None
        newDataIQR[newDataIQR["BMI"] < lowerBMI["BMI"]] = None

        self.from12To18DF.BMI = [
            newDataIQR[["BMI"]].var().values[0],
            newDataIQR[["BMI"]].mean().values[0],
            newDataIQR[["BMI"]].median().values[0],
        ]

        self.newDataBMI = newDataIQR

    def getStatisticsFrom19To20(self):
        newDataWithAge = self.DataFrame.copy()
        newDataWithAge = newDataWithAge.fillna(newDataWithAge.mean(numeric_only=True))
        newDataWithAge["Date of birth"] = pd.to_datetime(newDataWithAge["Date of birth"])
        newDataWithAge["Date of visit"] = pd.to_datetime(newDataWithAge["Date of visit"])
        age = newDataWithAge["Date of visit"] - newDataWithAge["Date of birth"]
        newDataWithAge["Age"] = [int(i.days/365) for i in age]
        self.newDataWithAge = newDataWithAge
        corr, pvalue = stats.pearsonr(newDataWithAge["Body fat mass"], newDataWithAge["Age"])
        self.from19To20DF.loc["correlation"] = corr
        self.from19To20DF.loc["p-value"] = pvalue

    def getStatisticsFrom22(self):
        self.dataWithDigitPA = self.DataFrame.copy()
        self.dataWithDigitPA[["Physical activity"]] = self.dataWithDigitPA[["Physical activity"]].replace({
            "Low": 1, 
            "Moderate": 2, 
            "High": 3,
        })

        self.spearman.loc["22"] = stats.spearmanr(
            self.dataWithDigitPA["Physical activity"], 
            self.dataWithDigitPA["Maximum degree of disk degeneration in lumbar spine"],
        )[0]

    def getStatisticsFrom23To26(self):
        linearModel = lm.LinearRegression()
        self.newDataWithAge["BMI"] = self.newDataBMI.BMI
        self.newDataWithAge = self.newDataWithAge[["Age", "BMI"]].dropna()
        npAge, npBMI = self.newDataWithAge.Age.to_numpy().reshape(-1, 1), self.newDataWithAge.BMI.to_numpy()
        linearModel.fit(npAge, npBMI)
        self.from23To26DF.loc["free-coefficient"] = linearModel.intercept_
        self.from23To26DF.loc["regression-coefficient"] = linearModel.coef_
        self.from23To26DF.loc["det-coefficient"] = 1 - (1-linearModel.score(npAge, npBMI))*(len(npBMI)-1)/(len(npBMI)-npAge.shape[1]-1)
        _, self.from23To26DF.loc["p-value"] = f_regression(npAge, npBMI)

    def getStatisticsFrom27To28(self):
        male, female = self.newDataBMI[self.newDataBMI["Sex"] == "Male"], self.newDataBMI[self.newDataBMI["Sex"] == "Female"]
        self.from27To28DF.loc["BMI"] = float(stats.ttest_ind(male[["BMI"]], female[["BMI"]], nan_policy="omit", equal_var=False).pvalue[0])
        self.from27To28DF.loc["Body fat mass"] = float(stats.ttest_ind(male[["Body fat mass"]], female[["Body fat mass"]], nan_policy="omit", equal_var=False).pvalue[0])

    def getChi2ByEthnicity(self, realStatisticsDict, degreesOfFreedom=11):
        ethnicityDataFrame = pd.DataFrame(realStatisticsDict.items())
        ethnicityDataFrame = ethnicityDataFrame.rename(columns={0: "", 1: "EthnicityReal"})
        ethnicityDataFrame.set_index("", inplace=True)
        ethnicityDataFrame = pd.concat([ethnicityDataFrame, pd.DataFrame(self.DataFrame["Ethnicity"].value_counts())], axis = 1)
        ethnicityDataFrame = ethnicityDataFrame.rename(columns={"count": "Ethnicity"})
        ethnicityDataFrame.Ethnicity = ethnicityDataFrame.Ethnicity / ethnicityDataFrame.Ethnicity.sum()
        ethnicityDataFrame.EthnicityReal = ethnicityDataFrame.EthnicityReal / 100
        res = pd.concat([pd.DataFrame(ethnicityDataFrame.EthnicityReal * self.DataFrame["Ethnicity"].value_counts().sum()), pd.DataFrame(self.DataFrame["Ethnicity"].value_counts())], axis=1).fillna(0).rename(columns={"count": "Ethnicity"})
        nexp = (res.Ethnicity - res.EthnicityReal)**2 / res.EthnicityReal
        return stats.chi2.sf(nexp.sum(), degreesOfFreedom)
    
    def getStatisticsFrom29To31(self, degreesOfFreedom=11):
        self.from29To31DF.loc["2010 Ethnicity statistics"] = self.getChi2ByEthnicity(self.real2010, degreesOfFreedom=degreesOfFreedom) # !!! may be mistake ---> TODO
        self.from29To31DF.loc["2021 Ethnicity statistics"] = self.getChi2ByEthnicity(self.real2021, degreesOfFreedom=degreesOfFreedom)

        mDDD = pd.DataFrame(self.DataFrame["Maximum degree of disk degeneration in lumbar spine"].value_counts())
        mDDDStatistics = pd.DataFrame(columns = ["our", "juornal"])
        mDDDStatistics.loc[1] = [mDDD.loc[1] / mDDD.sum()][0][0], 0.0094
        mDDDStatistics.loc[2] = [mDDD.loc[2] / mDDD.sum()][0][0], 0.0654
        mDDDStatistics.loc[3] = [mDDD.loc[3] / mDDD.sum()][0][0], 0.5234
        mDDDStatistics.loc[4] = [mDDD.loc[4] / mDDD.sum()][0][0], 0.3364
        mDDDStatistics.loc[5] = [mDDD.loc[5] / mDDD.sum()][0][0], 0.0654
        nexp_MDD = mDDD.reset_index()["Maximum degree of disk degeneration in lumbar spine"].sum() * (mDDDStatistics.our - mDDDStatistics.juornal)**2 / mDDDStatistics.juornal

        self.from29To31DF.loc["Maximum degree of disk degeneration in lumbar spine"] = stats.chi2.sf(nexp_MDD.sum(), 3)

    def getStatisticsFrom32To33(self):
        self.from32To33DF.loc["Sex / Physical activity"] = stats.mannwhitneyu(
            self.dataWithDigitPA[self.dataWithDigitPA["Sex"] == "Female"]["Physical activity"].values, 
            self.dataWithDigitPA[self.dataWithDigitPA["Sex"] == "Male"]["Physical activity"].values,
        )[1]

        self.from32To33DF.loc["Sex / Maximum degree of disk degeneration in lumbar spine"] = stats.mannwhitneyu(
            self.dataWithDigitPA[self.dataWithDigitPA["Sex"] == "Female"]["Maximum degree of disk degeneration in lumbar spine"].values, 
            self.dataWithDigitPA[self.dataWithDigitPA["Sex"] == "Male"]["Maximum degree of disk degeneration in lumbar spine"].values
        )[1]

    def getStatisticsFrom34To36(self):
        self.anovaDF = self.anovaDF.rename(columns={"Physical activity": "PA"})
        anovaModel = ols("BMI ~ LDDD + PA + LDDD*PA", data=self.anovaDF).fit()
        anovaResult = stm.stats.anova_lm(anovaModel, typ=2)

        self.from34To36DF.loc["LDDD (P-value)"] = anovaResult.loc["LDDD"]["PR(>F)"]
        self.from34To36DF.loc["PA (P-value)"] = anovaResult.loc["PA"]["PR(>F)"]

        sm = anovaResult.loc["PA"]["sum_sq"] + anovaResult.loc["LDDD"]["sum_sq"] + anovaResult.loc["LDDD:PA"]["sum_sq"]
        self.from34To36DF.loc["Proportion of the explained variance"] = sm / (anovaResult.loc["Residual"]["sum_sq"] + sm)

    def formatToFinalLine(self, name):
        self.finalLine.loc[name] = [
            1,
            round(self.from1To11DF.loc['var', 'Height'], 2),
            round(self.from1To11DF.loc['mean', 'Height'], 2),
            round(self.from1To11DF.loc['median', 'Height'], 2),
            round(self.from1To11DF.loc['quantile_25', 'Height'], 2),
            round(self.from1To11DF.loc['quantile_75', 'Height'], 2),
            round(self.from1To11DF.loc['var', 'Weight'], 2),
            round(self.from1To11DF.loc['mean', 'Weight'], 2),
            round(self.from1To11DF.loc['median', 'Weight'], 2),
            round(self.from1To11DF.loc['quantile_25', 'Weight'], 2),
            round(self.from1To11DF.loc['quantile_75', 'Weight'], 2),
            1,
            round(self.from12To18DF.loc[0, 'Height'], 2),
            round(self.from12To18DF.loc[1, 'Height'], 2),
            round(self.from12To18DF.loc[2, 'Height'], 2),
            round(self.from12To18DF.loc[0, 'BMI'], 2),
            round(self.from12To18DF.loc[1, 'BMI'], 2),
            round(self.from12To18DF.loc[2, 'BMI'], 2),
            round(self.from19To20DF.loc['correlation', 'results'], 2),
            round(self.from19To20DF.loc['p-value', 'results'], 2),
            1,
            round(self.spearman.loc["22", 'Spearman'], 2),
            round(self.from23To26DF.loc["regression-coefficient", 'results'], 2),
            round(self.from23To26DF.loc["free-coefficient", 'results'], 2),
            round(self.from23To26DF.loc["det-coefficient", 'results'], 2),
            round(self.from23To26DF.loc["p-value", 'results'], 3),
            round(self.from27To28DF.loc["BMI", 'T-Test'], 3),
            round(self.from27To28DF.loc["Body fat mass", 'T-Test'], 3),
            round(self.from29To31DF.loc["2010 Ethnicity statistics", 'Chi^2'], 3),
            round(self.from29To31DF.loc["2021 Ethnicity statistics", 'Chi^2'], 3),
            round(self.from29To31DF.loc["Maximum degree of disk degeneration in lumbar spine", 'Chi^2'], 3),
            round(self.from32To33DF.loc["Sex / Physical activity", 'Mann-Uitney'], 3),
            round(self.from32To33DF.loc["Sex / Maximum degree of disk degeneration in lumbar spine", 'Mann-Uitney'], 3),
            round(self.from34To36DF.loc["LDDD (P-value)", 'ANOVA'], 2),
            round(self.from34To36DF.loc["PA (P-value)", 'ANOVA'], 2),
            round(self.from34To36DF.loc["Proportion of the explained variance", 'ANOVA'], 2),
            1,
        ]
        