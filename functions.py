import numpy as np


def constructGraph(number_tasks, weights, data):
    adjacency_matrix = np.full((number_tasks, number_tasks), float('inf'))
    for i in range(number_tasks):
        weight = weights[i]
        successors = data[i]
        for successor in successors:
            adjacency_matrix[i][successor - 1] = -weight
    return adjacency_matrix


def fetchData(rpc_file_path):
    adjacency_table = []
    weights = []
    with open(rpc_file_path, "r") as f:
        data = f.read().split()

    n = len(data) - 1
    i = 6
    while i <= n:
        weights.append(int(data[i]))
        i += 5
        nombre_succ = int(data[i])
        task_successors = [int(data[i + c]) for c in range(1, nombre_succ + 1)]
        adjacency_table.append(task_successors)
        i += nombre_succ + 1

    return adjacency_table, weights, len(weights)


def BellmanFord(number_tasks, AdjacencyMatrix):  # implementation of bellman Ford algorithm
    # initialization
    # assuming that we start from task 1 which is a dummy task with no predecessors
    dist = [float("inf")] * number_tasks
    dist[0] = 0
    pred = [-1] * number_tasks

    # relaxation of edges
    ''' the flag : to detect no changes, 
    it turns to true when there is no changes after two consecutive iterations, 
    so we can stop early and save time
    '''

    for i in range(number_tasks - 1):
        flag = False
        for u in range(number_tasks):
            for v in range(number_tasks):
                if dist[u] != float('inf') and AdjacencyMatrix[u][v] != float('inf') and dist[v] > dist[u] + \
                        AdjacencyMatrix[u][v]:
                    dist[v] = dist[u] + AdjacencyMatrix[u][v]
                    pred[v] = u
                    flag = True
        if not flag:
            break

    # detection of negative cycles
    for u in range(number_tasks):
        for v in range(number_tasks):
            if dist[u] != float("inf") and AdjacencyMatrix[u][v] != float("inf") and dist[v] > dist[u] + \
                    AdjacencyMatrix[u][v]:
                return False
    return dist, pred


def CriticalPath(number_tasks, AdjacencyMatrix):
    dist, prev = BellmanFord(number_tasks, AdjacencyMatrix)
    path = []
    task = number_tasks - 1  # because dummy source is 0 so dummy end is n-1 given we have n tasks
    while task != -1:
        path.append(task + 1)
        task = prev[task]

    return -dist[number_tasks - 1], path[::-1]


def taskMinStartTime(task, AdjacencyMatrix, number_tasks):
    dist, prev = BellmanFord(number_tasks, AdjacencyMatrix)
    tast_index = task - 1
    return np.abs(dist[tast_index])


def taskMaxStartTime(task, AdjacencyMatrix, number_tasks):
    dist, prev = BellmanFord(number_tasks, AdjacencyMatrix)
    tast_index = task - 1
    return np.abs(dist[-1]) - np.abs(dist[tast_index])
