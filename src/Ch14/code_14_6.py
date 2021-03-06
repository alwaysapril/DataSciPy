#
# 따라하며 배우는 파이썬과 데이터과학(생능출판사 2020)
# 14.6 선형 회귀를 사이킷런 라이브러리로 구현해 보자, 373쪽
#
import numpy as np 
from sklearn import linear_model  # scikit-learn 모듈을 가져온다

regr = linear_model.LinearRegression()

X = [[164], [179], [162], [170]]  # 다중회귀에도 사용하도록 함 
y = [53, 63, 55, 59]              # y = f(X)의 결과 
regr.fit(X, y)