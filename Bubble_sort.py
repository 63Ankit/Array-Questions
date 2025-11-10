#  Bubble Sort Ascending Order
'''
def Pattern(n):
    arr=[73,5,40,15,50]
    for j in range(len(arr)):
        for i in range(len(arr)-1):
            if arr[i]>arr[i+1]:
                temp=arr[i]
                arr[i]=arr[i+1]
                arr[i+1]=temp
    for i in range(len(arr)):
        print(arr[i])

Pattern(9)


#  Bubble Sort Descending Order
def Pattern(n):
    arr=[73,5,40,15,50]
    for j in range(len(arr)):
        for i in range(len(arr)-1):
            if arr[i]<arr[i+1]:
                temp=arr[i]
                arr[i]=arr[i+1]
                arr[i+1]=temp
    for i in range(len(arr)):
        print(arr[i])

Pattern(9)

#  Bubble Sort Character Descending Order
def Pattern():
    arr=["D","E","A","B","F"]
    for j in range(len(arr)):
        for i in range(len(arr)-1):
            if ord(arr[i])<ord(arr[i+1]):
                temp=arr[i]
                arr[i]=arr[i+1]
                arr[i+1]=temp
    for i in range(len(arr)):
        print(arr[i])

Pattern()

# Bubble Sort Character Ascending Order
def Pattern():
    arr=["D","E","A","B","F"]
    for j in range(len(arr)):
        for i in range(len(arr)-1):
            if ord(arr[i])>ord(arr[i+1]):
                temp=arr[i]
                arr[i]=arr[i+1]
                arr[i+1]=temp
    for i in range(len(arr)):
        print(arr[i])

Pattern()

'''
# Bubble Sort Character Ascending Order without using ord function.
def Pattern():
    arr=["D","E","A","B","F"]
    for j in range(len(arr)):
        for i in range(len(arr)-1):
            if str(arr[i])>str(arr[i+1]):
                temp=arr[i]
                arr[i]=arr[i+1]
                arr[i+1]=temp
    for i in range(len(arr)):
        print(arr[i])

Pattern()

