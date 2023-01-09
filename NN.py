def NearestNeightbor(m, n):
    i = 0
    way = [i]
    used = [i]
    res = 0

    while(len(used) < n):
        last = way[-1]
        NN = tuple([-1, float('inf')])
        available_nodes = [node for node in range(n) if not(node in used)]

        for j in available_nodes:
            if(m[last][j][1] < NN[1]):
                NN = m[last][j]
   
        way.append(NN[0])
        used.append(NN[0])
        res += NN[1]
    
    res += m[0][way[-1]][1]

    print(res)
    print(way)

if __name__ == "__main__":
    matrix = []
    max_node = 0

    with open("./my_test.txt") as file:
        for line in file:
            a, b, val = map(int, line.split())
            max_node = max([max_node, a, b])

            while(max_node > len(matrix)):
                matrix.append([])
            
            matrix[a - 1].append(tuple([b - 1, val]));
            matrix[b - 1].append(tuple([a - 1, val]))
    
    for node in range(max_node): 
        matrix[node].insert(node, tuple([node, 0])); 

    NearestNeightbor(matrix, max_node)
        