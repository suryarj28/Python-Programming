import random

test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

total_names = len(names)

random_name = random.randint(0, total_names - 1)

buyer_name = names[random_name]

print(f"{buyer_name} is going to buy the meal today!")