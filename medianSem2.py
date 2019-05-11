
summ = 0
c = 0
result = 0
a = ''
while(input):
    a = str(input("Subject: "))

    if str(a) == "Algebra":
        grade = float(input("Estimated grade: "))
        summ += grade*0.6
        print(summ)

    elif a == "AlgoProg":
        grade = float(input("Estimated grade: "))
        summ += grade*0.6
        print(summ)

    elif a == "PPE":
        grade = float(input("Estimated grade: "))
        summ += grade*0.2
        print(summ)

    elif a == "PF":
        grade = float(input("Estimated grade: "))
        summ += grade*0.4
        print(summ)

    elif a == "Eng":
        grade = float(input("Estimated grade: "))
        summ += grade*0.3
        print(summ)

    elif a == "WEB":
        grade = float(input("Estimated grade: "))
        summ += grade*0.3
        print(summ)

    elif a == "FCR":
        grade = float(input("Estimated grade: "))
        summ += grade*0.3
        print(summ)

    elif a == "BDD":
        grade = float(input("Estimated grade: "))
        summ += grade*0.3
        print(summ)

Median = float(summ) / float(30)
