age = int(input("Hi there! Please enter your age: "))
sum_age = 0
counter = 1
while counter <= age:
    sum_age += counter
    counter += 1
print(f"The sum of all numbers from 1 to {age} is: {sum_age}")
