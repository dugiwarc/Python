def evalExpr(lst):
    """
    parameters : lst of type lst:
    returns : evaluation of the expression inside brackets;
    """
    for i, e in enumerate(lst): # i is the index and e the actual element in the iteration
        if isinstance(e, list) and len(e) == 3:
            lst[i] = eval(str(lst[i][0]) + lst[i][1] + str(lst[i][2]))
    return lst

new_list = evalExpr([[2, "+", 5], 3, 5, [2,'*', 4], [2,'**', 4]])

print(new_list)