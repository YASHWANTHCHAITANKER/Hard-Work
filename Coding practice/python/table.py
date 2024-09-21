''' user=int(input("Enter your number : "))
for i in range(1,11):
    a=(f"{user}X{i}={user*i}")
    print(a)
'''
user = int(input("Enter your number : "))
i = 1
while(i<=10):
    print(f"{user}X{i}={user*i}")
    i=i+1