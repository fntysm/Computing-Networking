# import numpy as np y=np.transpose(x)
def transposee(matrix):
    result = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
    return result

def arithmetic_arranger(problems, bool=False):
    arranged_problems = []
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
        line1 = firstOperandstr.rjust(lines)
        line21 = problem[pos].rjust(1)
        line22 = secondOperandstr[1::].rjust(lines-2)
        dashes = '-'*lines
        arranged_problem =""+line1+"\n"+line21+" "+line22+"\n"+dashes
        arranged_problems.append(arranged_problem)
    print(problemsConstruction)
    i=-1
    for lineOp in arranged_problems:
        print(lineOp, end=' ')
        i+=1
        if (bool==True):
            print((str(problemsConstruction[i][0]+problemsConstruction[i][1])).rjust(problemsConstruction[i][3]),"\n")






array = ["3475-6", "14+6353","25-96"]
print(arithmetic_arranger(array))


