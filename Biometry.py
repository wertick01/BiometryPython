import os
os.system('pip install numpy pandas datetime scipy sklearn colorama sklearn')
import numpy as np
import pandas as pd
import math
import datetime
import scipy
from scipy import stats
import sklearn
from colorama import init, Fore, Back, Style

init()

def console_picture():
    print(Style.BRIGHT + Fore.RED)
    print("   |||||||        |||||||||||   |||||||      |||||||||||   |||||||||||   |||||||||||   |||||||||||   |||||||")
    print("   |||   ||||         |||       |||   |||    |||           |||     |||       |||       |||           |||   ||||")
    print("   |||      |||       |||       |||    |||   |||           |||               |||       |||           |||      |||")
    print("   |||       |||      |||       |||   |||    |||||||||||   |||               |||       |||||||||||   |||       |||")
    print("   |||       |||      |||       |||||||      |||||||||||   |||               |||       |||||||||||   |||       |||")
    print("   |||      |||       |||       |||  |||     |||           |||               |||       |||           |||      |||")
    print("   |||   ||||         |||       |||   |||    |||           |||     |||       |||       |||           |||   ||||")
    print("   |||||||        |||||||||||   |||    |||   |||||||||||   |||||||||||       |||       |||||||||||   |||||||")
    print()
    print()
    print("   |||||||     |||         |||")
    print("   |||   |||     |||     |||")
    print("   |||   |||       ||| |||")
    print("   |||||||           |||")
    print("   |||||||           |||")
    print("   |||   |||         |||")
    print("   |||   |||         |||")
    print("   |||||||           |||")
    print()
    print()
    print("   |||           |||   |||||||            |||||||      |||||||||||   |||||||")
    print("   ||||||     ||||||   |||   |||          |||   |||    |||           |||   ||||")
    print("   |||  ||| |||  |||   |||    |||         |||    |||   |||           |||      |||")
    print("   |||    |||    |||   |||   |||          |||   |||    |||||||||||   |||       |||")
    print("   |||           |||   |||||||            |||||||      |||||||||||   |||       |||")
    print("   |||           |||   |||  |||           |||  |||     |||           |||      |||")
    print("   |||           |||   |||   |||          |||   |||    |||           |||   ||||")
    print("   |||           |||   |||    |||         |||    |||   |||||||||||   |||||||")
    print()
    print()
console_picture()

finaly = pd.DataFrame(columns = [str(i) for i in range(1, 38)])

print('???????? ???????????? ???????? ???????????? ?? ?????????????? .csv')
print(r'?????????????? ???????? ?? ?????????? (?? ?????????????? C:\user\...\file.csv)')
path = input(r"????????: ")
data = pd.read_csv(path, sep = ';')
df = pd.DataFrame(columns = ['Height', 'Weight'])
df.loc['var'] = data[['Height', 'Weight']].var()
df.loc['mean'] = data[['Height', 'Weight']].mean()
df.loc['median'] = data[['Height', 'Weight']].median()
df.loc['quantile_25'] = data[['Height', 'Weight']].quantile(0.25)
df.loc['quantile_75'] = data[['Height', 'Weight']].quantile(0.75)
print(r'?????????????? ???????? ?? ????????????????????, ?? ?????????????? ?????????????????? ???????????? (?? ?????????????? C:\user\...\directory\).')
final = input(r'????????: ')
dir_ = path.split("\\")[-1].split('_')[0]
mkdir = final + dir_
os.mkdir(mkdir)
mkdir += '\\'
name = '_result_2_to_11.csv'
print('Running')
df.to_csv(mkdir+dir_+name)

finaly.loc[0, '1'] = 1
finaly.loc[0, '2'] = round(df.loc['var', 'Height'], 2)
finaly['3'] = round(df.loc['mean', 'Height'], 2)
finaly['4'] = round(df.loc['median', 'Height'], 2)
finaly['5'] = round(df.loc['quantile_25', 'Height'], 2)
finaly['6'] = round(df.loc['quantile_75', 'Height'], 2)
finaly['7'] = round(df.loc['var', 'Weight'], 2)
finaly['8'] = round(df.loc['mean', 'Weight'], 2)
finaly['9'] = round(df.loc['median', 'Weight'], 2)
finaly['10'] = round(df.loc['quantile_25', 'Weight'], 2)
finaly['11'] = round(df.loc['quantile_75', 'Weight'], 2)

dat = data.copy()
q25 = dat[['Height', 'Weight']].quantile(0.25)
q75 = dat[['Height', 'Weight']].quantile(0.75)
IQR = q75 - q25
cut_off = IQR * 1.5
cut_off
lower, upper = q25 - cut_off, q75 + cut_off

dat_st = data[['Height']].copy()
dat_st[dat_st['Height'] > upper['Height']] = None
dat_st[dat_st['Height'] < lower['Height']] = None
rs_sk = pd.DataFrame(columns = ['Height'])
rs_sk.loc['var'] = [dat_st[['Height']].var().values[0]]
rs_sk.loc['mean'] = [dat_st[['Height']].mean().values[0]]
rs_sk.loc['median'] = [dat_st[['Height']].median().values[0]]

dat[dat['Height'] > upper['Height']] = None
dat[dat['Height'] < lower['Height']] = None
dat[dat['Weight'] > upper['Weight']] = None
dat[dat['Weight'] < lower['Weight']] = None
dat['BMI'] = dat['Weight'] / (dat['Height']*0.01)**2
q25_bmi = dat[['BMI']].quantile(0.25)
q75_bmi = dat[['BMI']].quantile(0.75)
IQR_bmi = q75_bmi - q25_bmi
cut_off_bmi = IQR_bmi * 1.5
cut_off_bmi
lower_bmi, upper_bmi = q25_bmi - cut_off_bmi, q75_bmi + cut_off_bmi
dat[dat['BMI'] > upper_bmi['BMI']] = None
dat[dat['BMI'] < lower_bmi['BMI']] = None

rs = pd.DataFrame(columns = ['BMI'])
rs.loc['var'] = dat[['BMI']].var()
rs.loc['mean'] = dat[['BMI']].mean()
rs.loc['median'] = dat[['BMI']].median()

rs_res = pd.DataFrame(columns = ['Height', 'BMI'])
rs_res[['Height']] = rs_sk[['Height']]
rs_res[['BMI']] = rs[['BMI']]

name_2 = '_13_to_18.csv'
rs_res.to_csv(mkdir+dir_+name_2)

finaly['12'] = 1
finaly['13'] = round(rs_res.loc['var', 'Height'], 2)
finaly['14'] = round(rs_res.loc['mean', 'Height'], 2)
finaly['15'] = round(rs_res.loc['median', 'Height'], 2)
finaly['16'] = round(rs_res.loc['var', 'BMI'], 2)
finaly['17'] = round(rs_res.loc['mean', 'BMI'], 2)
finaly['18'] = round(rs_res.loc['median', 'BMI'], 2)

dct = {'Low': 1, 'Moderate': 2, 'High': 3}
data_j = data.copy()
data_j[['Physical activity']] = data_j[['Physical activity']].replace(dct)
data_j = data_j.rename(columns = {
    'Maximum degree of disk degeneration in lumbar spine': 'MDD',
    'Physical activity': 'PA'
}
                      )
drt = pd.DataFrame(columns = ['Spearman'])
drt.loc['22'] = round(stats.spearmanr(data_j.PA, data_j.MDD)[0], 2)
name_2_1 = '_22.csv'
drt.to_csv(mkdir+dir_+name_2_1)

finaly['22'] = drt.loc['22', 'Spearman']

data_i = data.copy()
data_i = data_i.fillna(data_i.mean(numeric_only=True))
dm = data_i.copy()
dm['Date of birth'] = pd.to_datetime(dm['Date of birth'])
dm['Date of visit'] = pd.to_datetime(dm['Date of visit'])
a = dm['Date of visit'] - dm['Date of birth']
dm['Age'] = [int(i.days/365) for i in a]
corr, pvalue = scipy.stats.pearsonr(dm['Body fat mass'], dm['Age'])
dt_1 = pd.DataFrame(columns = ['result'])
dt_1.loc['correllation'] = corr
dt_1.loc['p-value'] = pvalue
name_3 = '_19_to_20.csv'
dt_1.to_csv(mkdir+dir_+name_3)

finaly['19'] = round(dt_1.loc['correllation', 'result'], 2)
finaly['20'] = round(dt_1.loc['p-value', 'result'], 2)
finaly['21'] = 1

data_i = dat.dropna()
dm = data_i.copy()
dm['Date of birth'] = pd.to_datetime(dm['Date of birth'])
dm['Date of visit'] = pd.to_datetime(dm['Date of visit'])
a = dm['Date of visit'] - dm['Date of birth']
dm['Age'] = [int(i.days/365) for i in a]
import sklearn.linear_model as lm
from sklearn.feature_selection import f_regression
skm = lm.LinearRegression()
dm_1 = dm[['Age', 'BMI']].dropna()
np_bmi = dm_1['BMI'].to_numpy()
np_age = dm_1['Age'].to_numpy()
np_bmi = np_bmi
np_age = np_age.reshape(-1, 1)
skm.fit(np_age, np_bmi)
f_statistic, p_value = f_regression(np_age, np_bmi)
g = pd.DataFrame(columns = ['res'])
g.loc['free'] = skm.intercept_
g.loc['regr'] = skm.coef_
g.loc['det_coeff'] = 1 - (1-skm.score(np_age, np_bmi))*(len(np_bmi)-1)/(len(np_bmi)-np_age.shape[1]-1)
g.loc['p_value'] = p_value
name__ = '_23_to_26.csv'
g.to_csv(mkdir+dir_+name__)

finaly['23'] = round(g.loc['regr', 'res'], 2)
finaly['24'] = round(g.loc['free', 'res'], 2)
finaly['25'] = round(g.loc['det_coeff', 'res'], 2)
finaly['26'] = round(g.loc['p_value', 'res'], 3)

data_i = dat.copy()
male, female = data_i[data_i['Sex'] == 'Male'], data_i[data_i['Sex'] == 'Female']

male_bmi, female_bmi = male[['BMI']], female[['BMI']]

male_bfm, female_bfm = male[['Body fat mass']], female[['Body fat mass']]

dtt = pd.DataFrame(columns = ['res'])
dtt.loc['p_value_27'] = round(float(scipy.stats.ttest_ind(male_bmi, female_bmi, nan_policy='omit', equal_var=False).pvalue.data), 3)
dtt.loc['p_value_28'] = round(float(scipy.stats.ttest_ind(male_bfm, female_bfm, nan_policy='omit', equal_var=False).pvalue[0]), 3)

name_5 = '_27_to_28.csv'
dtt.to_csv(mkdir+dir_+name_5)

finaly['27'] = dtt.loc['p_value_27', 'res']
finaly['28'] = dtt.loc['p_value_28', 'res']

da = pd.DataFrame(columns = ['p_value'])

dat = data.copy()

real_2002 = {
    'Armenian': 0.78,# 
    'Bashkir': 1.15, #
    'Tatar': 3.83, #
    'Ukrainian': 2.03,#
    'German': 0.41, #
    'Chuvash': 1.13,#
    'Chechen': 0.94,#
    'Kazakh': 0.45,#
    'Yakut': 0.31,#
    'Russian': 79.83,#
    'Buryat': 0.31,#
    'Uzbek': 0.09,#
       }
dft = pd.DataFrame(real_2002.items())
dft = dft.rename(columns = {0: '', 1: 'Ethnicity_1'})
dft = dft.set_index('')
a = pd.concat([dft, dat['Ethnicity'].value_counts()], axis=1)
a['Ethnicity'] = (100. * a.Ethnicity / a.Ethnicity.sum())
a['Ethnicity'] = a['Ethnicity']/100
a['Ethnicity_1'] = a['Ethnicity_1']/100
b = pd.DataFrame(a.Ethnicity_1 * dat['Ethnicity'].value_counts().sum())
c = pd.DataFrame(dat['Ethnicity'].value_counts())
red = pd.concat([b, c], axis=1).fillna(0)
nexp_2002 = (red.Ethnicity-red.Ethnicity_1)**2/red.Ethnicity_1
p_2002 = scipy.stats.chi2.sf(nexp_2002.sum(), 11)

real_2010 = {
    'Armenian': 0.83,#
    'Bashkir': 1.11,#
    'Tatar': 3.72,#
    'Ukrainian': 1.35,#
    'German': 0.28,#
    'Chuvash': 1.01,#
    'Chechen': 1.,#
    'Kazakh': 0.45,#
    'Yakut': 0.34,#
    'Russian': 77.71,#
    'Buryat': 0.32,#
    'Uzbek': 0.2,#
}
dft_2010 = pd.DataFrame(real_2010.items())
dft_2010 = dft_2010.rename(columns = {0: '', 1: 'Ethnicity_1'})
dft_2010 = dft_2010.set_index('')
a_2010 = pd.concat([dft_2010, dat['Ethnicity'].value_counts()], axis=1)
a_2010['Ethnicity'] = (100. * a_2010.Ethnicity / a_2010.Ethnicity.sum())
a_2010['Ethnicity'] = a_2010['Ethnicity']/100
a_2010['Ethnicity_1'] = a_2010['Ethnicity_1']/100
b_2010 = pd.DataFrame(a_2010.Ethnicity_1 * dat['Ethnicity'].value_counts().sum())
c_2010 = pd.DataFrame(dat['Ethnicity'].value_counts())
red = pd.concat([b_2010, c_2010], axis=1).fillna(0)
nexp_2010 = (red.Ethnicity-red.Ethnicity_1)**2/red.Ethnicity_1
p_2010 = scipy.stats.chi2.sf(nexp_2010.sum(), 11)

dag = pd.DataFrame(data['Maximum degree of disk degeneration in lumbar spine'].value_counts())
reg = pd.DataFrame(columns = ['our', 'juornal'])
reg.loc[2] = [dag.loc[2, 'Maximum degree of disk degeneration in lumbar spine'] / dag.sum()][0][0], 0.066
reg.loc[3] = [dag.loc[3, 'Maximum degree of disk degeneration in lumbar spine'] / dag.sum()][0][0], 0.528
reg.loc[4] = [dag.loc[4, 'Maximum degree of disk degeneration in lumbar spine'] / dag.sum()][0][0], 0.34
reg.loc[5] = [dag.loc[5, 'Maximum degree of disk degeneration in lumbar spine'] / dag.sum()][0][0], 0.066
nexp_MDD = dag['Maximum degree of disk degeneration in lumbar spine'].sum() * (reg.our-reg.juornal)**2/reg.juornal
p_MDD = scipy.stats.chi2.sf(nexp_MDD.sum(), 3)

da.loc['p_value_2002_???29'] = p_2002
da.loc['p_value_2010_???30'] = p_2010
da.loc['MaxDegrDisk_???31'] = p_MDD

name_6 = '_29_to_31.csv'
da.to_csv(mkdir+dir_+name_6)

finaly['29'] = round(da.loc['p_value_2002_???29', 'p_value'], 3)
finaly['30'] = round(da.loc['p_value_2010_???30', 'p_value'], 3)
finaly['31'] = round(da.loc['MaxDegrDisk_???31', 'p_value'], 3)

from sklearn import preprocessing
dct = {'Low': 1, 'Moderate': 2, 'High': 3}
data_3 = data.copy()
data_3[['Physical activity']] = data_3[['Physical activity']].replace(dct)
pa_1 = scipy.stats.mannwhitneyu(
    data_3[data_3['Sex'] == 'Female']['Physical activity'].values, 
    data_3[data_3['Sex'] == 'Male']['Physical activity'].values
)
mdd_1 = scipy.stats.mannwhitneyu(
    data_3[data_3['Sex'] == 'Female']['Maximum degree of disk degeneration in lumbar spine'].values, 
    data_3[data_3['Sex'] == 'Male']['Maximum degree of disk degeneration in lumbar spine'].values
)
data_2 = pd.DataFrame(columns = ['result'])
data_2.loc['32'] = pa_1[1]
data_2.loc['33'] = mdd_1[1]
name_7 = '_32_to_33.csv'
data_2.to_csv(mkdir+dir_+name_7)

finaly['32'] = round(data_2.loc['32', 'result'], 3)
finaly['33'] = round(data_2.loc['33', 'result'], 3)

import pandas as pd
final = pd.DataFrame(columns = ['result'])
final.loc['34'] = 1
final.loc['35'] = 1
final.loc['36'] = 1
name_8 = '_34_to_36.csv'
data_2.to_csv(mkdir+dir_+name_8)

finaly['34'] = final.loc['34', 'result']
finaly['35'] = final.loc['35', 'result']
finaly['36'] = final.loc['36', 'result']
finaly['37'] = 1

name_9 = '_final_result.csv'
finaly.to_csv(mkdir+dir_+name_9)

print('Done\nFile has been saved to:', mkdir)


