import numpy as np


class Model:
    def __init__(self):
        self.rpc_file_path = 'C:/Users/lenovo/Desktop/test.rcp'
        self.number_tasks = 0
        self.data = []
        self.AdjacencyMatrix = np.array([])

    def constructGraph(self):  # construct adjacency matrix
        print(self.number_tasks)
        print(self.AdjacencyMatrix)
        for i in range(self.number_tasks):
            weight = self.data[i][0]
            for j in range(self.number_tasks):
                if j in self.data[i][6::]:
                    self.AdjacencyMatrix[i][j] = -weight
        np.set_printoptions(threshold=np.inf)
        print(self.AdjacencyMatrix)

    def fetchData(self): # fetch data from rcp file and fill in the attributes
        with open(self.rpc_file_path, 'r') as f:
            rpc_data = f.readlines()
        # fill in the attributes
        self.data = [list(map(int, line.strip().split())) for line in rpc_data if line.strip().split()]
        self.number_tasks = self.data[0][0]
        self.data = self.data[2::]
        self.AdjacencyMatrix = np.array([[float('inf')] * self.number_tasks] * self.number_tasks)

    def minimalDuration(self):  # implementation of bellman Ford algorithm
        # initialization
        # assuming that we start from task 1 which is a dummy task with no predecessors
        dist = np.array([0.] + [float('inf')] * (self.number_tasks - 1))
        pred = [-1] * self.V
        # iterating through nodes
        i = 1
        ''' the flag : to detect no changes, 
        it turns to true when there is no changes after two consecutive iterations, 
        so we can stop early and save time
        '''
        flag = False
        while i != self.number_tasks and not flag:


            i += 1

    def taskMinStartTime(self, task):
        pass

    def taskMaxStartTime(self, task):
        pass
