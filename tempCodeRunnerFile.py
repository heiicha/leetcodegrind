def findEvenNumbers(digits):
    evens = [i for i in range(100,1000,2)]
    ans = []
    for num in evens:
        digitz = {digit for digit in str(num)}
        if digitz <= {i for i in digits}:
            ans.append(num)
    sorted = ans.sort()
    print(sorted)
        

findEvenNumbers([2,1,3,0])
    