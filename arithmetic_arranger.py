
# when we wanted to transopse a 2d arrayn, we could've used numpy:  import numpy as np y=np.transpose(x)
# but i chose to write a function
def transposee(matrix):
    result = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
    return result

def arithmetic_arranger(problems, bool=False):
    # arranged_problems will be a 2d array where we have each problem digested in each array
    arranged_problems = []
    # problemsConstruction would hold the first and second operand, the operator and the number of dashes
    problemsConstruction = []
    # now, we will count the amount of problems supplied into the function, if it's more than 5, we will show an error
    countProblems = problems.__len__()
    if  countProblems > 5:
        return "Error: Too many problems."
    elif countProblems == 0:
        return "No problem was supplied"
    operators = ["+", "-"]
    # now, because the existence of only one operator from the array: operators is required: we will check it
    for problem in problems:
        i = 0
        for op in operators:
            pos = problem.find(op)
            i += 1
            if pos!=-1:
                break
            elif -1 == pos and operators.__len__() == i:
                return "Error: Operator must be '+' or '-'."
        # now that we have an operation with one accepted operator, we will check if it operands got only DIGITS
        try:
            firstOpstr = problem[0:pos].split(" ")
            firstOperandstr = firstOpstr[0]
            secondOpstr = problem[pos::].split(" ")
            secondOperandstr = secondOpstr[1]
            firstOperand = int(firstOperandstr)
            secondOperand = int(secondOperandstr)
            if problem[pos]=="-":
                secondOperand = (-1)*secondOperand
            firstDigits = firstOperandstr.__len__()
            secondDigits = secondOperandstr.__len__()
            if firstDigits>4 or secondDigits>4:
                return "Error: Numbers cannot be more than four digits."
        except ValueError:
            return "Error: Numbers must only contain digits."
        lines = max(firstDigits,secondDigits)+2
        problemConstruction = [firstOperand,secondOperand,problem[pos],lines]
        problemsConstruction.append(problemConstruction)
        line1 = firstOperandstr.rjust(lines)
        line21 = problem[pos].ljust(0,' ')
        line22 = secondOperandstr.rjust(lines-1,' ')
        dashes = '-'*lines
        arranged_problem = [line1,line21+line22,dashes]
        arranged_problems.append(arranged_problem)
    # we need the transposed array of arranged_problems, because we are printing the operations horizontally
    arranged_problemsT = transposee(arranged_problems)
    # in the next loop, we will code the displaying pattern:
    j = 0
    while (j < 3):
        i = 0
        k = 0
        while (k < countProblems):
            print(arranged_problemsT[j][k], end='    ')
            k += 1
            if (bool == True and j==2 and k==countProblems):
                print("")
                while(i<countProblems):
                    print((str(problemsConstruction[i][0] + problemsConstruction[i][1])).rjust(problemsConstruction[i][3]), end='    ')
                    i += 1
        print("")
        j += 1
    arranged_problems = ""
    return arranged_problems




