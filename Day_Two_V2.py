import sys,re
def my_function_Verify(Policy,Password):
    x =re.search("([0-9]+-[0-9]+) ?([A-Za-z ]+)",Policy)
    if( x != None):
        if(int(str(x.group(1)).split("-")[0]) <= Password.count(str(x.group(2))) <= int(str(x.group(1)).split("-")[1])):
            #print("its okay")
            return 0
        else:
            #print("not okay")
            return 1
      
    else:
        print("Wrong Format")         

count = 0
f = open("input2.txt",'r',encoding = 'UTF-8').read()
arr = f.split('\n')
for i in range(0,len(arr)):
    result = arr[i].split(":")
    count = count + my_function_Verify(result[0],result[1])
    
print(count)