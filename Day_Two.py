import sys,re
def my_function_Verify(Policy,Password):
    x =re.search("([0-9]+-[0-9]+) ?([A-Za-z ]+)",Policy)
    find1 = False
    if( x != None):
    
        c = str(x.group(2))
        result = [pos for pos, char in enumerate(Password) if char == c]
    
        for a in result :
            if( (a == int(str(x.group(1)).split("-")[0]) or  a == int(str(x.group(1)).split("-")[1])) and find1 == True):
                find1 = False
            else:
                if( a == int(str(x.group(1)).split("-")[0]) or  a == int(str(x.group(1)).split("-")[1])):
                    find1 = True
        if(find1 == True):
            return 1
        else:
            return 0
    else:
        print("Wrong Format")         

count = 0
f = open("input2.txt",'r',encoding = 'UTF-8').read()
arr = f.split('\n')
for i in range(0,len(arr)):
    result = arr[i].split(":")
    count = count + my_function_Verify(result[0],result[1])   
print(count)