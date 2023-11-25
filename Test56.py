
N_W = input("Enter your score: ")
if N_W == "W":

    while N_W == "W":
        print("ติด ร")
        break
else:

    N_2 = input("Enter your score: ")
    N_3 = input("Enter your score: ")
    N_4 = input("Enter your score: ")

    Total_score = int(N_W) + int(N_2) + int(N_3) + int(N_4)

    while Total_score >= 0 and Total_score <= 100:
        if Total_score >= 80:
            print("4")
        elif Total_score >=75 and Total_score < 80:
            print("3.5")
        elif Total_score >=70 and Total_score < 75:
            print("3")
        elif Total_score >=65 and Total_score < 70:
            print("2.5")
        elif Total_score >=60 and Total_score < 65:
            print("2")
        elif Total_score >=55 and Total_score < 60:
            print("1.5")
        elif Total_score >=50 and Total_score < 55:
            print("1")
        else:
            print("0")
        break





