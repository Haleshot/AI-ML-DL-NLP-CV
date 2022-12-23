import constraint
problem = constraint.Problem()
problem.addVariable('x', [1,2,3])
problem.addVariable('y', range(10))

def our_constraint (x, y):
    if x + y >= 5:
        return True

problem. addConstraint(our_constraint, ['x','y'])

solutions = problem.getSolutions()

for solution in solutions:
    print (solution)


length = len(solutions)
print(" (x,y) E (", end="")
for index, solution in enumerate (solutions):
    if index == length - 1:
        print("(0),())".format(solution['x'],solution['y']),end="")
    else:
        print(" ({},{}),".format (solution['x'], solution['y']), end="")
print ("}")