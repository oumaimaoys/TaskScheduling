
import functions as func

rpc_file_path = 'C:/Users/lenovo/Desktop/RG300_45.rcp'

data, weights, number_tasks = func.fetchData(rpc_file_path)

AdjacencyMatrix = func.constructGraph(number_tasks, weights, data)

duree_min, path = func.CriticalPath(number_tasks, AdjacencyMatrix)

print("duree minimal= ", duree_min)

print(func.taskMinStartTime(100, AdjacencyMatrix, number_tasks))
print(func.taskMaxStartTime(100, AdjacencyMatrix, number_tasks))