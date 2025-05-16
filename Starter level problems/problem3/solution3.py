def find_elder(age1, age2):
    if age1 > age2:
        print("Brother 1 is elder")
    elif age2 > age1:
        print("Brother 2 is elder")
    else:
        print("Both are of the same age")

find_elder(15, 18)