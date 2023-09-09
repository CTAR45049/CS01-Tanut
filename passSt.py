def main():
    num1 = int(input())
    num2 = int(input())
    num3 = int(input())
    
    greatest = num1
    
    if num2 > greatest:
        greatest = num2
    
    if num3 > greatest:
        greatest = num3
    
    print(greatest)

main()