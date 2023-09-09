def main():
    total = 0
    for i in range(10):
        num = float(input(f"Enter num: "))
        if num < 0:
            continue
        total += num
        
    print(int(total))
main()