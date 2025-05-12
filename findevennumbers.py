def findEvenNumbers(digits):
    evens = [i for i in range(100,1000,2)]
    ans = []
    digitcount = {digits.count(i) for i in digits}
    for num in evens:
        digitz = [int(digit) for digit in str(num)]
        valid = True
        for i in digitz:
            if digitz.count(i) > digits.count(i):
                valid = False
                break
        if valid:
            ans.append(num)
    
    ans.sort()
    return ans
        
#test case
findEvenNumbers([2,1,3,0])
    