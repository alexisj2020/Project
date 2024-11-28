import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#import time series and co2 data
with open ("data/co2_mm_gl_space.txt") as file1:
    time=[]
    co2=[]
    for line in file1:
        #y=line[0:4]
        #m=line[8:10]
        #ym=m+'/'+y
        time.append(line[13:22])
        #time.append(ym)
        avg=line[25:32]
        co2.append(avg)
        timeco2=[time,co2]

#import temperature data
with open ("data/Temperature.txt") as file2:
    temp=[]
    for i, line in enumerate(file2):
        if i>=347:
            temp.append(line[12:21])
        if i>=891:
            break

#import sea ice area data
with open ("data/sea_extent.txt") as file3:
    ice=[]
    for i, line in enumerate(file3):
        if i>=2:
            ice.append(line[9:-1])
        if i>=546:
            break

#import sea ice extent data
with open ("data/sea_ice_extent.txt") as file5:
    ice_ex=[]
    for i, line in enumerate(file5):
            ice_ex.append(line[:6])

#import ocean ph data
with open ("data/phdata.txt") as file4:
    ph=[]
    timeph=[]
    for i, line in enumerate(file4):
        ph.append(line[:6])

#remove empty entries in ph data
for i in range(len(ph)):
    if ph[i] == 'NaN\t19':
       ph[i] = ''
    if ph[i] == 'NaN\t20':
       ph[i] = ''

ph1=[]
#replace empty entries with np.nan
for string in (ph):
    if string == '':
        string = np.nan
    ph1.append(string)

#remove spaces in entries from co2 and time series
co2 = [x.strip(' ') for x in co2]
times=[]
for i in time:
    j = i.replace(' ','')
    times.append(j)

#remove empty characters from elements in ice_exs list
ice_exs=[]
for i in ice_ex:
    j = i.replace('\t','')
    ice_exs.append(j)

#remove header row
co2.pop(0)
times.pop(0)

#replace strings with floats in each list
times2 = [float(string) for string in times]
co2_2=[float(string) for string in co2]
temp_2 = [float(string) for string in temp]
ice_2 = [float(string) for string in ice]
ph_2 = [float(string) for string in ph1]
ice_exs_2 = [float(string) for string in ice_exs]

#create function for calculating the annual data
def annual(dataset):
    n = 12
    datayear = [sum(dataset[i:i+12])/n for i in range(0,len(dataset),12)]
    datayear = datayear[:-1] #remove last year because dataset is not complete
    return(datayear)

year = times2[::12]
year = year[:-1]
tempyear1 = annual(temp_2)
co2year1 = annual(co2_2)
iceexyear1 = annual(ice_exs_2)