num_1 = input('Enter first number: ') # take first n.o as input 
num_2 = input('Enter second number: ') # take second n.o as input

result = num_1 + num_2
# But these numbers are stored as strings

print(type(num_1),type(num_2)) # this shows that numbers are stored as strings

print('Sum of two numbers is: ',result)
# it will literally concatenate those numbers



#................DO TYPECONVERSION....................
num_3 = float(input('Now Enter first number: '))
num_4 = input('then Enter second number: ')

print(type(num_3),type(num_4)) # now datatype is changed to float 

sum = num_3+float(num_4)
print('Sum of two numbers is: ',sum)

print(type(num_4))

# KEY POINT: PYTHON ka typeconversion doesn't do any change in 
# original variable ka datatype , but rather it creates a new data of it
