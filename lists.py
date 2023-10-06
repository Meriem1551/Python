#spliting string
str = "Hello there dudes"
print(str.split(' '))
fib1 = [1,1,2,3,5,8,13]
print(fib1[2]) #print item at pos 2
print(fib1[0:5]) # print items from 0th to 5 not including 5th
fib2 = [21,34,55]
print(fib1 + fib2) #joining fib1 and fib2
fib1[0] = 9 # changing value
fib = fib1 + fib2
fib.append(89) #appending an item
print(fib) #print the modified list
fib.pop() #remove the last item
fib.remove(fib[2]) #remove a specific item
del(fib[5]) 
print(fib)
cars = ['mario', 'luigi', 'browser']
cars.append(5)
print(cars)
nums = [cars, fib1, [1,2,3,4]]
print(nums)
nums[0] #returns cars
print(nums[2][1]) #go to 2 list inside it return the 1st element
