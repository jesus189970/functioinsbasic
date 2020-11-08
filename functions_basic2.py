#Countdown
def countdown(t):
    countdown = []
    while t >= 0:
        countdown.append(t)
        t -= 1
       # print(countdown);

    return countdown

print(countdown(5))

#Print and Return
def print_and_return(a,b):
    print(a)
    return b

print(print_and_return(1,2))

#First Plus Length

def first_plus_length(array):
    # return c + first_plus_length.length;
    # 1 first_value 
    #first_value = array[0]

    # 2 length
    #length = len(array)

    # 3 return the sum of 1 and 2
    #return first_value + length

    return array[0] + len(array)

print(first_plus_length([1,2,3,4,5])) # array = [1,2,3,4,5]
'''
first value + length
'''

#Values Greater Then Second

#def values_greater_than_second(array):
  #  new_list = []
     #   if len(array) < 2 and len:
      #  return False
    
    #else:

def values_greater_than_second(array):
    
    if len(array) < 2:
        return False
    new_list = []
    secondval = array[1]
    for i in range(0, len(array), 1):
        if array[i] > secondval:
            new_list.append(array[i])
    print(len(new_list))
    return new_list



print(values_greater_than_second([5, 2, 3, 2, 1, 4]))
print(values_greater_than_second([3]))

#This Lengh, That Value
def length_and_value(a,b):
    x = a * str(b)
    return x

print(length_and_value(4,7))
print(length_and_value(6,2))