def getMinMax(mylist, method='max'):
   minValue = 999999999999999999999999999999999
   maxValue = -minValue

   if method == 'max' :
       for value in mylist:
           if value > maxValue:
               maxValue = value;
       return maxValue
   elif method == 'min' :
       for value in mylist:
           if value < minValue:
               minValue = value;
       return minValue
   else :
       print('illegal method')


list_data = [27, 90, 30, 87, 56]
while(True):
   print(list_data)
   s = input('최대값을 원하면 max, 최소값을 원하면 min을 입력하시오: ')
   print(getMinMax(list_data, s))
