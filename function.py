# #function.py
#function takes no argument

# divide code into useful blocks 
# allowing us to order our code 
# make it more readable
# reuse it and save some time
# code resue is very important in programming
# Dry (don't repet yourself) principle.

# syntax
# syntax for user-defined function
# def fubction_name(argument):
# """
#  function 
# """


# definre greet hello everone

# def greet():
# 	print('hello everyone!!!')# defultreturn none
# greet()

# def greet():
# 	"""
# 	this is greet funtion for greeting return none
# 	"""
# 	greet()
# 	help(greet)


#function call
# greet()
# b = greet #function assingment
# c = b
# print(c())

#positional argument
#function takes one required positional argument

# def greet(name):#return none
# 	print('hello {}!'.format(name))
# greet('nima')

#function takes two required positional argument

# def add(a,b):#retur none
# 	print(a+b)
# a = add(6,7)
# print(a)

 #return object from function 
# def add(a,b):#return value
# 	return a+b
# result = add(5,7)
# print(result)

# keyword argument

# def info(name,age,addr):
# 	print(f'my name is:{name}\nage:{age}\naddress:{addr}')
	#positional argument
# info('nima',20,'tokha')#expected output
# info(20,'tokha','nima')#notexpected output
#keyword argument
# info(age=20,addr='tokha',name='nima')

#default argument
# def info(name='nima'):
# 	print('my name is {}'.format(name))
# 	# info()
# info('ram')
# note: the defult arguments are not reevaluated each time the function is called. USE NONE AND Docstrings to specify dynamic defult argument.

#function takes one required positional argument and one default(or optional)argument
# def mul(a,b=5):
# 	print(a+b)
# # mul(3)
# mul(6,6)

#exercise:
#fibonacci searies is the sum of the two preceding numbers.
#the simplest is the series 1,1,2,3,5,6,etc.
# def fibonacci(n): #function with argument n
# 	a,b = 0,1
# 	while b < n:
# 		print(b)
# 		a,b = b, a+b
# fibonacci(20)

#fibonic sereise in list

# def fibonacci(n):
# 	fibonacci_series =[]
# 	a,b = 0,1
# 	while b < n:
# 		fibonacci_series.append(a)
# 		a,b = b, a+b
# 	return(fibonacci_series)
# result = fibonacci(20)
# print(result)

