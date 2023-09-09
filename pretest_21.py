# Odd Add Odd Add
def main():
    num = int(input("Please enter your number: ")) 

    if num % 2 == 0:
        return('even')
    else:
        return('odd')

result = main()
print(result)