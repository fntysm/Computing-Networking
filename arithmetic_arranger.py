def arithmetic_arranger(problems, bool=False):
    problemsConstruction = []
    if problems.__len__() > 5:
        return "Error: Too many problems."
    operators = ["+", "-"]
    for problem in problems:
        i = 0
        for op in operators:
            pos = problem.find(op)
            i += 1
            if pos!=-1:
                break
            elif -1 == pos and operators.__len__() == i:
                return "Error: Operator must be '+' or '-'."
        try:
            firstOperandstr = problem[0:pos]
            secondOperandstr = problem[pos::]
            firstOperand = int(firstOperandstr)
            secondOperand = int(secondOperandstr)
            firstDigits = firstOperandstr.__len__()
            secondDigits = secondOperandstr.__len__()
            if firstDigits>4 or secondDigits>4:
                return "Error: Numbers cannot be more than four digits."
        except ValueError:
            return "Error: Numbers must only contain digits."
        lines = max(firstDigits,secondDigits)+2
        problemConstruction = [firstOperand,secondOperand,problem[pos],lines]
        problemsConstruction.append(problemConstruction)
        print(firstOperand,"\n",problem[pos]," "*max(firstDigits,secondDigits),abs(secondOperand),"\n","-"*lines)
    arranged_problems = problemsConstruction
    return arranged_problems






array = ["3475+6", "14-53","89-36"]
print(arithmetic_arranger(array))
# print(f"{array[0]:>i}{array[1]:>}")

