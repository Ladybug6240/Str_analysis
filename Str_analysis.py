def str_analysis():
    s = int(0)
    a = str(input("Enter the string for analysis: "))
    b = str(input("Enter the letter you want to count: "))
    for i in a:
        if i == b:
            s = s + 1
    print("The count of the letters: " + str(s))


str_analysis()

