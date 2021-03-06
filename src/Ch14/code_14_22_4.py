#
# 따라하며 배우는 파이썬과 데이터과학(생능출판사 2020)
# 14.22 기대수명 데이터 읽어오기와 결측 확인하기, 392쪽
#
import pandas as pd 
import seaborn as sns    # 시각화를 위하여 Seaborn 라이브러리를 이용함

life = pd.read_csv('d:/data/life_expectancy.csv')
life = life[['Life expectancy', 'Year', 'Alcohol',
           'Percentage expenditure', 'Total expenditure',
           'Hepatitis B', 'Measles', 'Polio', 'BMI', 'GDP',
           'Thinness 1-19 years', 'Thinness 5-9 years']]

life.dropna(inplace = True)
print(life.shape)