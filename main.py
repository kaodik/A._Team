i = int(input())
def printOutput(i):
    count=0
    output=0
    arr = []
    ones = 0
    while count < i:
        inp = str(input())
        arr.insert(i, inp)
        count +=1
    for x in arr:
        for k in x:
            if k == '1':
                ones += 1
        if(ones > 1):
            output+=1
            ones = 0
        else:
            ones=0
    print(output)

if __name__ == '__main__':
    printOutput(i)
