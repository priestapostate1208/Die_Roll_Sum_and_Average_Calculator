import random
number_of_rolls = int(input("Please input the number of dice rolls as an integer.   "))
# try:
#     number_of_rolls = int(input("Please input the number of dice rolls as an integer.   "))
# except ValueError:
#     print("That is not an integer - please input an integer.")

num_sum=0
num_avg=0
die_roll=[]
#digits
for x in range(number_of_rolls):
    die_roll.append(random.randrange(1,16))
print (die_roll, "\n") #This prints the list.
#the above code works.

def calculate_sum(die_roll):
    for x in die_roll:
        global num_sum
        num_sum+=x
    print(f"The sum of the dice rolls is {num_sum}.")
    return num_sum

def calculate_avg(num_sum, number_of_rolls):
    global num_avg
    num_avg=(num_sum/number_of_rolls)
    print (f"The average of the dice rolls is {num_avg}."  )
    return num_avg

calculate_sum(die_roll)
calculate_avg(num_sum, number_of_rolls)
