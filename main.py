while True:
    primer = input("Введи пример: ")

    chasti = primer.split()

    a = chasti[0]
    oper = chasti[1]
    b = chasti[2]


    if oper == "+":
        print(a, "+", b, "=", float(a) + float(b))

    elif oper == "-":
        print(a, "-", b, "=", float(a) - float(b))

    elif oper == "*":
        print(a, "*", b, "=", float(a) * float(b))

    elif oper == "/":
        if float(b) == 0:
            print("На ноль делить нельзя")
        else:
            print(a, "/", b, "=", float(a) / float(b))

    elif oper == "//":
        if float(b) == 0:
            print("На ноль делить нельзя")
        else:
            print(a, "//", b, "=", float(a) // float(b))

    elif oper == "%":
        if float(b) == 0:
            print("На ноль делить нельзя")
        else:
            print(a, "%", b, "=", float(a) % float(b))

    elif oper == "**":
        print(a, "**", b, "=", float(a) ** float(b))

    elif oper == "==":
        print(a, "==", b, "=", float(a) == float(b))

    elif oper == "!=":
        print(a, "!=", b, "=", float(a) != float(b))

    elif oper == ">":
        print(a, ">", b, "=", float(a) > float(b))

    elif oper == "<":
        print(a, "<", b, "=", float(a) < float(b))

    elif oper == ">=":
        print(a, ">=", b, "=", float(a) >= float(b))

    elif oper == "<=":
        print(a, "<=", b, "=", float(a) <= float(b))

    elif oper == "and":
        print(a, "and", b, "=", bool(float(a)) and bool(float(b)))

    elif oper == "or":
        print(a, "or", b, "=", bool(float(a)) or bool(float(b)))

    elif oper == "not":
        print("not", a, "=", not bool(float(a)))

    elif oper == "in":
        spisok = b.strip("[]").split(",")
        print(a, "in", b, "=", float(a) in [float(x) for x in spisok])

    elif oper == "not_in":
        spisok = b.strip("[]").split(",")
        print(a, "not in", b, "=", float(a) not in [float(x) for x in spisok])

    elif oper == "is":
        print(a, "is", b, "=", a is b)

    elif oper == "is_not":
        print(a, "is not", b, "=", a is not b)

    else:
        print("Ошибка, нет такого оператора")