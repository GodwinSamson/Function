#reverse of a number
def reverse_number(num):
    if num== 0:
        return 0
    elif num == 1:
        return 1
    elif num== 2:
        return 3
    elif num == 3:
        return 2
    elif num == 4:
        return 4
    else:
        return "Invalid number"
number = int(input("enter a number between 0 and 4"))
reversed_number = reverse_number(number)
print("Reversed number", reversed_number)


