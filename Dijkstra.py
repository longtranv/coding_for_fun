def Dijkstra(graph, start, end):
    queue = []
    current_node = start
    distance_sum_fromStart = {}
    result = {}
    queue.append(start)
    for node in graph:
        distance_sum_fromStart[node] = (float('inf'), None)
    
    distance_sum_fromStart[start] = (0, None)
    
    while len(result)+1<len(distance_sum_fromStart):
        current_node = queue.pop(0)

        for neiborNode, weight in graph[current_node].items():
            distance_from_root = weight + distance_sum_fromStart[current_node][0]
            
            if isinstance(distance_sum_fromStart[neiborNode], tuple) and len(distance_sum_fromStart[neiborNode]) > 1:
                if distance_from_root <= distance_sum_fromStart[neiborNode][0] and neiborNode!=start:
                    distance_sum_fromStart[neiborNode] = (distance_from_root, current_node)
        distance_sum_fromStart[current_node] = None

        current_nodes_considered = {}
        for item in  distance_sum_fromStart.keys():
            if distance_sum_fromStart[item] != None:
                if item != start and distance_sum_fromStart[item][0] > 0 and isinstance(distance_sum_fromStart[item], tuple):
                    current_nodes_considered[item] = distance_sum_fromStart[item]

        next_node_considered, Min = next(iter(current_nodes_considered.items()))
        for key in current_nodes_considered.keys():
            if isinstance(current_nodes_considered[key], tuple) and current_nodes_considered[key][0]!= float('inf'):
                if key != start and current_nodes_considered[key][0] <= Min[0]:
                    next_node_considered = key
                    Min = current_nodes_considered[key]
            
        result[next_node_considered] = Min
        queue.append(next_node_considered)
    
    previous_node = result[end][1]
    path = []
    path.append(end)
    path.insert(0, result[end][1])
    while previous_node != start:
        path.insert(0, result[previous_node][1])
        previous_node = result[previous_node][1]

    return path

        

        
            
# Example graph representation
graph = {
    '0': {'1': 2.5, '2': 2, '3': 2.1},
    '1': {'0': 2.5, '4': 1},
    '2': {'0':2, '4':0.6, '5':1.5},
    '3': {'0':2.1, '5': 2.5},
    "4": {'1':1, '2':0.6, '6':2.3},
    "5": {'2':1.5, '3': 2.5, '6': 1.9, '7':2},
    "6": {'4':2.3, '5':1.9, '7':1.8, '8':1.7},
    "7": {'5':2, '6':1.8, '8':2},
    "8": {'6':1.7, '7':2}
    }
Start = '0'
End = '7'
print(Dijkstra(graph, Start, End))


               


