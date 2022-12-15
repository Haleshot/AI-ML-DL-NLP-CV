# I066, Srihari Thyagarajan, B3
# A * Algorithm


def sorting_second(l):
    return l[1]

def add_nodes():
    limit = int(input("Enter the Limit for the Number of Nodes : "))
    Nodes = []

    for i in range(limit):
        n = []
        Node_name, Hsld, Path_Cost = map(str, input("Enter the Node Name, Heuristic Straight Line Distance and Path Cost respectively : ").split())
        buffer = int(Hsld) + int(Path_Cost)
        n.extend([Node_name, buffer])
        Nodes.append(n)

    for i in range(limit):
        buffer = int(Nodes[i][1])
        Nodes[i][1] = buffer

    Total_Nodes_Sequence.extend(Nodes)
    Total_Nodes_Sequence.sort(key=sorting_second)
    return Total_Nodes_Sequence
        


Total_Nodes_Sequence = []
Initial_State_Name, Hsld1 = map(str, input("Enter the Initial Node Name, Heuristic Straight Line Distance : ").split())
Goal_state_Name, Hsld2 = map(str, input("Enter the Goal State Node Name, Heuristic Straight Line Distance : ").split())


A = []
C = []

B = []
D = []

A.append(Initial_State_Name)
A.append(int(Hsld1))
C.append(A)

B.append(Goal_state_Name)
B.append(int(Hsld2))
D.append(B)

print("The Initial State is : ", C)
print("The Goal State is : ", D)

ready = []
closed = []
closed.extend(C)


def main():
    run = True
    while run:
        if C == D:
            print("Goal Result Reached.")
            run = False

        else:
            add_nodes()
            print(Total_Nodes_Sequence)
            print("The Vertice with the smallest value : ", Total_Nodes_Sequence[0])
            print("Hence we expand {} Node : ".format(Total_Nodes_Sequence[0]))
            closed.extend(Total_Nodes_Sequence[0])
            
            if Total_Nodes_Sequence[0][0] == D[0][0] and Total_Nodes_Sequence[0][1] == D[0][1]:
                print("Success!")
                print("The Path Sequence is : ", closed)
                run = False

main()

