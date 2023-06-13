import numpy as np


class Model:
    def __init__(self):
        self.rpc_file_path = 'C:/Users/lenovo/Desktop/RG300_43.rcp'
        self.number_tasks = 0
        self.data = []
        self.AdjacencyMatrix = np.array([])

    def constructGraph(self):
        self.AdjacencyMatrix = np.full((self.number_tasks, self.number_tasks), float('inf'))
        for i in range(self.number_tasks):
            weight = self.data[i][0]
            successors = self.data[i][6:]
            for successor in successors:
                self.AdjacencyMatrix[i][successor - 1] = -weight

        '''np.set_printoptions(threshold=np.inf)
        print(self.AdjacencyMatrix)'''

    def fetchData(self):
        tableau_adjacence = []
        poids = []
        f = open(self.rpc_file_path, "r")
        T = f.read()
        T = T.split()
        n = len(T) - 1
        i = 6
        while i <= n:
            adjacence = []
            c = 0
            poids.append(int(T[i]))
            i += 5
            nombre_succ = int(T[i])
            while c <= nombre_succ:
                adjacence.append(int(T[i + c]))
                c += 1
            tableau_adjacence.append(adjacence)
            i += c

        return tableau_adjacence, poids, len(poids)

    def BellmanFord(self):  # implementation of bellman Ford algorithm
        # initialization
        # assuming that we start from task 1 which is a dummy task with no predecessors
        dist = [float("inf")] * self.number_tasks
        dist[0] = 0
        pred = [-1] * self.number_tasks

        # relaxation of edges
        ''' the flag : to detect no changes, 
        it turns to true when there is no changes after two consecutive iterations, 
        so we can stop early and save time
        '''

        for i in range(self.number_tasks - 1):
            flag = False
            for u in range(self.number_tasks):
                for v in range(self.number_tasks):
                    if dist[u] != float('inf') and self.AdjacencyMatrix[u][v] != float('inf') and dist[v] > dist[u] + \
                            self.AdjacencyMatrix[u][v]:
                        dist[v] = dist[u] + self.AdjacencyMatrix[u][v]
                        pred[v] = u
                        flag = True
            if not flag:
                break

        # detection of negative cycles
        for u in range(self.number_tasks):
            for v in range(self.number_tasks):
                if dist[u] != float("inf") and self.AdjacencyMatrix[u][v] != float("inf") and dist[v] > dist[u] + \
                        self.AdjacencyMatrix[u][v]:
                    return False
        return dist, pred

    def CriticalPath(self):
        dist, prev = self.BellmanFord()
        path = []
        task = self.number_tasks - 1  # because dummy source is 0 so dummy end is n-1 given we have n tasks
        while task != -1:
            path.append(task + 1)
            task = prev[task]

        return dist[self.number_tasks - 1], path[::-1]

    def taskMinStartTime(self, task):
        pass

    def taskMaxStartTime(self, task):
        pass
