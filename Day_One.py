import os,sys
def my_function(array_Integer,Limit1,Limit2):
   
    for x in range(len(array_Integer)):
        if(2020-Limit1 < array_Integer[x] < 2020-Limit2):
            for k in range(len(array_Integer)):
                if(2020-Limit1 < array_Integer[x] < 2020-Limit2):
                    for z in range(len(array_Integer)):
                        if(2020-Limit1 < array_Integer[x] < 2020-Limit2):
                            if(array_Integer[x] + array_Integer[k] + array_Integer[z] == 2020):
                                return tuple((array_Integer[x],array_Integer[k],array_Integer[z]))

 

f = open("input",'r',encoding = 'UTF-8').read()
arr = f.split('\n')
 
arr = [int(i) for i in arr] 
Limit1 = max(arr)
Limit2 = min(arr)
 
print(my_function(arr,Limit1,Limit2))