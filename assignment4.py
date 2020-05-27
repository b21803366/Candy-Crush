import sys
def fib(number):
    if number==1 or number==2:
        return 1
    else:
        return fib(number-1)+fib(number-2)
def connected(x1,y1,x2,y2,notIncluded):
    if(x1<0 or x1>=len(numbers)) or (x2<0 or x2>=len(numbers)):
        return 0
    elif(y1<0 or y1>=len(numbers[x1])) or (y2<0 or y2>=len(numbers[x2])):
        return 0
    for i in range(len(notIncluded)):
        if x1==notIncluded[i][0] and y1==notIncluded[i][1]:
            return 0
    notIncluded.append([])
    notIncluded[len(notIncluded)-1].append(x1)
    notIncluded[len(notIncluded)-1].append(y1)
    if numbers[x1][y1]==numbers[x2][y2]:
        if x1==x2 and y1==y2:
            return 1
        else:
            return connected(x1-1,y1,x2,y2,notIncluded) or connected(x1+1,y1,x2,y2,notIncluded) or connected(x1,y1-1,x2,y2,notIncluded) or connected(x1,y1+1,x2,y2,notIncluded)
    else:
        return 0

def removeFromList(numbers,willRemove):
    for i in range(len(willRemove)):
        numbers[willRemove[i][0]][willRemove[i][1]]=-1
    for i in range(len(numbers[0])):
        for j in range(len(numbers)-1,-1,-1):
            if numbers[j][i]==-1:
                for k in range(j-1,-1,-1):
                    if numbers[k][i]!=-1:
                        numbers[j][i]=numbers[k][i]
                        numbers[k][i]=-1
                        break
    for i in range(len(numbers[0])):
        emptyLine=1
        for j in range(len(numbers)-1,-1,-1):
            if numbers[j][i]!=-1:
                emptyLine=0
                break
        if emptyLine==1 and i!=(len(numbers[0])-1):
            for k in range(len(numbers)):
                numbers[k][i]=numbers[k][i+1]
                numbers[k][i+1]=-1



numbers=[]

inputFile=open("input.txt","r")
i=0
for line in inputFile.readlines():
    numbers.append([])
    for j in range(line.count(" ")+1):
        numbers[i].append(int(line.split(" ")[j]))
    i+=1
for i in range(len(numbers)):
        print(i+1,end="")
        print("| ",end="")
        for j in range(len(numbers[i])):
            if(numbers[i][j]!=-1):
                print(numbers[i][j],end=" ")
            else:
                print(" ",end=" ")
        print("")
notIncluded=[]
point=0
while 1:
    maxNumber=numbers[0][0]
    minNumber=numbers[0][0]
    for i in range(len(numbers)):
        if(max(numbers[i])>maxNumber):
            maxNumber=int(max(numbers[i]))
        if(min(numbers[i])<minNumber):
            minNumber=int(min(numbers[i]))
    choose=input("Please enter a row and column number: ")
    if len(choose.split(" "))!=2:
        print("You enter wrong amount of argument!")
        continue
    row=int(choose.split(" ")[0])-1
    column=int(choose.split(" ")[1])-1
    if row>len(numbers) or column>len(numbers[0]):
        print("You enter a wrong value!")
        continue
    while row > maxNumber or column > maxNumber or row < minNumber or column < minNumber:
        print("Please enter a correct size!")
        choose=input("Please enter a row and column number: ")
        row=int(choose.split(" ")[0])
        column=int(choose.split(" ")[1])

    currentNumber=numbers[row][column]
    willRemove=[]
    k=0
    for i in range(len(numbers)):
        for j in range(len(numbers[i])):
            if numbers[i][j]==currentNumber:
                notIncluded=[]
                if connected(i,j,row,column,notIncluded):
                    willRemove.append([i,j])
                    k+=1
    point+=fib(len(willRemove))
    print("You have",point,"points.")
    removeFromList(numbers,willRemove)
    allEmpty=1
    for i in range(len(numbers)):
        for j in range(len(numbers[0])):
            if numbers[i][j]!=-1:
                allEmpty=0
                break
        if allEmpty==0:
            break
    if allEmpty:
        print("Congratulations! You finished the game with",point,"points.")
        break
    for i in range(len(numbers)):
        print(i+1,end="")
        print("| ",end="")
        for j in range(len(numbers[i])):
            if(numbers[i][j]!=-1):
                print(numbers[i][j],end=" ")
            else:
                print(" ",end=" ")
        print("")



