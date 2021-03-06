#
# 따라하며 배우는 파이썬과 데이터과학(생능출판사 2020)
# 12.18 빠진 데이터를 깨끗하게 메워 보자, 327쪽
#
import pandas as pd

weather = pd.read_csv('d:/data/weather.csv', index_col = 0, encoding='CP949')
weather.fillna( weather['평균풍속'].mean(), inplace = True)
print(weather.loc['2012-02-11'])