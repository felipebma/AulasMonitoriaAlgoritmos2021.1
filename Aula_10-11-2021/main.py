def bfs(graph, origin, destiny):
    parent = []
    visited = []
    for _ in range(len(graph)):
        parent.append(-1)
        visited.append(False)
    visited[origin] = True
    curr_level = [origin]
    while len(curr_level) > 0:
        next_level = []
        for node in curr_level:
            if node == destiny:
                return parent
            for next in graph[node]:
                if not visited[next]:
                    parent[next] = node
                    visited[next] = True
                    next_level.append(next)
        curr_level = next_level


def dfs(graph, origin, destiny):
    stack = [origin]
    visited = []
    for _ in range(len(graph)):
        visited.append(False)
    while len(stack) > 0:
        node = stack.pop(-1)
        if node == destiny:
            return True
        for next in graph[node]:
            if not visited[next]:
                visited[next] = True
                stack.append(next)
    return False


def print_path(origin, parent: dict, node):
    if parent[node] != -1:
        return print_path(origin, parent, parent[node]) + str(node)
    elif node != origin:
        return "não tem caminho"
    return str(node)


graph = []

for _ in range(10):
    graph.append([])

graph[0].append(1)
graph[1].append(0)
graph[1].append(2)
graph[2].append(0)
graph[2].append(3)
graph[3].append(0)
graph[3].append(4)
graph[4].append(2)

parent = bfs(graph, 0, 4)

print(parent)
print(print_path(0, parent, 3))
print(print_path(0, parent, 6))

graph2 = []

for _ in range(4):
    graph2.append([])

graph2[0].append(1)
graph2[0].append(3)
graph2[1].append(2)
graph2[1].append(3)
graph2[3].append(2)

# print(dfs(graph2, 0, 6))


# print("----------------")
# print("Caminho para o a")
# print_path(parent, 0)
# print("----------------")
# print("Caminho para o b")
# print_path(parent, 1)
# print("----------------")
# print("Caminho para o c")
# print_path(parent, 2)
# print("----------------")
# print("Caminho para o d")
# print_path(parent, 3)
# print("----------------")
# print("Caminho para o e")
# print_path(parent, 4)
