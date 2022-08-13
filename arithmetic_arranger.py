# import numpy as np y=np.transpose(x)
def transposee(matrix):
    result = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
    return result

def arithmetic_arranger(problems, bool=False):
    problemsConstruction = []
    countProblems = problems.__len__()
    if  countProblems > 5:
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
            secondDigits = secondOperandstr.__len__()-1
            if firstDigits>4 or secondDigits>4:
                return "Error: Numbers cannot be more than four digits."
        except ValueError:
            return "Error: Numbers must only contain digits."
        lines = max(firstDigits,secondDigits)+2
        problemConstruction = [firstOperand,secondOperand,problem[pos],lines]
        problemsConstruction.append(problemConstruction)
    print(problemsConstruction)
    ''''op = problemsConstruction
    problemsConstruction = transposee(op)
    print("sa transposée: ",problemsConstruction)'''
    arranged_problems = ""
    for i in range(0,countProblems):
        string = countProblems * '{:>8}'
        firstOperandstr = str(problemsConstruction[i][0])
        secondOperandstr = str(abs(problemsConstruction[i][1]))
        operationSign = problemsConstruction[i][2]
        maxDigits = problemsConstruction[i][3] - 2
        lines = problemsConstruction[i][3]
        arranged_problems += " "*maxDigits + firstOperandstr + "\n" + operationSign +" "*maxDigits + secondOperandstr + "\n" + "-"*lines+ "\n"
    return arranged_problems






array = ["3475-6", "14+6353","89-367","542+369","25-96"]
print(arithmetic_arranger(array))


