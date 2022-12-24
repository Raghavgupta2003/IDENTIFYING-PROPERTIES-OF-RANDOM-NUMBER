import random
print("<--PROGRAM FOR IDENTIFYING THE PROPERTIES OF A RANDOM NUMBER BETWEEN A RANGE-->")
print()
a = int(input('Enter the starting range : '))
b = int(input('Enter the ending range : '))
c = random.randint(a,b)
print(f'Range is ({a},{b}) and the randomly picked number is {c}')
print()
print("Properties---->")
if c%2 == 0:
    print(f'{c} is an even number.')
else:
    print(f'{c} is an odd number.')
if c > 0:
    print(f'{c} is a positive number.')
else:
    print(f'{c} is a negative number.')
flag = False
if c > 1:
    for i in range(2,c):
        if (c%i) == 0:
            flag = True
            break
    if flag:
        print(f'{c} is a composite number.')
    else:
        print(f'{c} is a prime number.')
