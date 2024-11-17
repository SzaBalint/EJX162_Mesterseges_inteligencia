def bfs(graph, start, end):
    queue = [[start]]
    while queue:
        path = queue.pop(0)
        print(path)
        node = path[-1]
        if node == end:
            return path
        for adjacent in graph.get(node, []):
            new_path = list(path)
            new_path.append(adjacent)
            queue.append(new_path)


def dfs(graph, start, end):
    queue = [[start]]
    while queue:
        path = queue.pop(0)
        print(path)
        node = path[-1]
        if node == end:
            return path
        for adjacent in graph.get(node, []):
            new_path = list(path)
            new_path.append(adjacent)
            queue.insert(0, new_path)