def calPoints(operations):
    soln = []

    for i in operations:
        try:
            soln.append(int(i))
        except:
            pass
        if i == "+":
            soln.append(soln[-1] + soln[-2])
        elif i == "D":
            soln.append(2 * soln[-1])
        elif i == "C":
            del soln[-1]

    return sum(soln)


ops = ["5","-2","4","C","D","9","+","+"]

print(calPoints(ops))
