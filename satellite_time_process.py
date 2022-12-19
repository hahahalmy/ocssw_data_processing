# -*- coding: utf-8 -*-
"""
Created on Thu Sep 29 16:06:11 2022

@author: Lenovo
"""

import pandas as pd


def day_of_year(row):
    year = int(row["yy"]);
    month = int(row["mm"]);
    day = int(row["dd"]);
    # 定义每个月的天数 year, month, day
    days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # 处理闰年
    if year % 400 == 0 or (year % 100 != 0 and year % 4 == 0):
        days_in_month[2] = 29

    # 计算从1月1日到给定日期的天数
    days = sum(days_in_month[:month]) + day

    return days

# return year+dat    ex.2010203
def year_day(row):
    year = int(row["yy"]);
    day = int(row["time"]);
    if day>99:
        return str(year) + str(day)
    elif day >9:
        return str(year) + "0" + str(day)
    else:
        return str(year) + "00" + str(day)

data = pd.read_excel("D:\\insitu_Rrs_PRE_2018_2020.xls");
data["time"] = data.apply(day_of_year, axis = 1);
data["time"] = data.apply(year_day, axis=1)

data_time = list(set(data["time"]))


f = open("D:\\filelist.txt", "r")
line = f.readline() 
line = line[:-1]
filename = []
filename.append(line)
while line:
    line = f.readline()
    line = line[:-1]
    filename.append(line)

answer = []
for time in data_time:
    for file in filename:
        if(time == file[1:8]):
            answer.append(file);
    

