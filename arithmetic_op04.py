#Create a variable called 'number' and assign it the three-digit number.
number=456
#Find the 'number' first digit and assign to x1.
x1=number%10
print(x1)
#Find the 'number' second digit and assign to x2.
x2=number//10
x22=x2%10
print(x22)
#Find the 'number' third digit and assign to x3.
x3=number//100
print(x3)
#Create a variable called 'answer' and assign it the sum of the three digits.
answer=x1+x22+x3
#print the sum of the three digits.
print(answer)