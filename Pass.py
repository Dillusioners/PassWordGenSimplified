import random

x = int(input("Enter the number of keywords you want"))
i = 1
pass_list = []
for i in range(x):
    inp = input("Enter your keyword")
    if i % 2 == 0:
        inp = inp.lower()
        pass_list.append(inp)
    else:
        inp = inp.upper()
        pass_list.append(inp)

num = random.randint(1, 100100)
num = str(num)
pass_list.append(num)
rand_list = random.choice(['!', '@', '#', '$', '%', '^', '&', '*', '?', '/', '+'])
pass_list.extend(rand_list)

c = " "

for n in range(len(pass_list)):
    c = c + pass_list[n]

print("The password is: ", c)
