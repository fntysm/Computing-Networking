def arithmetic_arranger(problems):
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
        


array = ["35+6", "33-9", "44+2"]
print(arithmetic_arranger(array))
