import random
num = random.randint(1, 10)
user_num = int(input("input:"))
if user_num == num:
    print("yes")
    exit()
else:
    if user_num < num:
        print("smaller replace:")
    else:
        print("bigger replace:")

    user_num = int(input("input:"))

    if user_num == num:
        print("yes")
        exit()
    else:
        if user_num < num:
            print("smaller replace:")
        else:
            print("bigger replace:")

    user_num = int(input("input:"))

    if user_num == num:
        print("yes")
    else:
        print("fail")

