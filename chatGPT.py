from queue import PriorityQueue

def Dijkstra(graph, start, end):
    queue = PriorityQueue()
    queue.put((0, start))

    distance_sum_fromStart = {node: (float('inf'), None) for node in graph}
    distance_sum_fromStart[start] = (0, None)

    while not queue.empty():
        current_distance, current_node = queue.get()

        if current_node == end:
            break

        for neighbor_node, weight in graph[current_node].items():
            distance_from_root = weight + current_distance

            if distance_from_root < distance_sum_fromStart[neighbor_node][0]:
                distance_sum_fromStart[neighbor_node] = (distance_from_root, current_node)
                queue.put((distance_from_root, neighbor_node))

    path = []
    while current_node != start:
        path.insert(0, current_node)
        current_node = distance_sum_fromStart[current_node][1]

    path.insert(0, start)
    return path

# Example graph representation and start/end nodes
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
