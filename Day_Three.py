import sys
file = open('file.txt', 'r') 
 
Matrix = []
l =[]
while 1: 
    
    # read by character 
    char = file.read(1)
    if not char:
        if(char == ''):
            Matrix.append(l)
            break
        else:
            break
    l.append(char)
    if char == "\n" :
        Matrix.append(l)
        l = []
  
file.close() 
 
print(len(Matrix))
print(len(l))
print("----------------------------------")
#for i in range(0,len(Matrix)):
#    for j in range(0,len(l)):
#        print(Matrix[i][j],end=" ")
#    print( str(i) + "\n")
i = 0
j = 0
count = 0

y = 1
find = False
Result = []
for x in [1,3,5,7,1]:
    if(x == 7):
        find = True
    if( x == 1 and find):
        y = 2
    while(i < len(Matrix) and j < len(l)):
        if(Matrix[i][j] == "#"):
            count = count + 1
        j = j + x
        if(j >= len(l)):
            j = j - len(l)
        i = i + y 
    print(count)
    Result.append(count)  
    i = 0
    j = 0
    count = 0
print(Result[2]*Result[0]*Result[3]*Result[1]*Result[4])