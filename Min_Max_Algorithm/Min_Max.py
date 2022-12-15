# I066, Srihari Thyagarajan, B3
# Min Max Algorithm


# Maximizer Function
def Maximizer(nodes_list_sequence):
    return max(nodes_list_sequence)

# Maximizer Function
def Minimizer(nodes_list_sequence):
    return min(nodes_list_sequence)

# Minimizer Function
def minimax(levels, nodes_list_sequence):
    if levels % 2 != 0:
        new = []
        for i in nodes_list_sequence:
            if type(i) == list:
                new.append(Minimizer(i))
            else:
                new.append(Minimizer(nodes_list_sequence))
                break

    else:
        new = []
        for i in nodes_list_sequence:
            if type(i) == list:
                new.append(Maximizer(i))
            else:
                new.append(Maximizer(nodes_list_sequence))
                break

    return new

# Main Function
def main():
    run = True
    while run:
        total_levels = 2
        terminals = []
        for i in range(3):
            t = []
            a1, a2, a3 = map(int, input().split())
            t.append(a1)
            t.append(a2)
            t.append(a3)
            terminals.append(t)
        nodes = terminals
        print(terminals)
        print(nodes)
        level = total_levels - 1

        while level >= 0:
            nodes = minimax(level, nodes)
            level -= 1
        print(nodes)

        run = int(input("Enter 1 to Continue, 0 to Exit the program : "))


main()
# Input Data - 
# 3 12 8
# 2 4 6
# 14 5 2