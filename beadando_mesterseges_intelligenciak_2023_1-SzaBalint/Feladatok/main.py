import bfs_and_dfs
import time
from branch_and_bound import BranchAndBound


def populate_heuristic_values(first_line: str, heuristic_distances: dict[str:int]):
    to_slice = first_line.split(' ')
    for i in range(len(to_slice)):
        if i > 0:
            separate = to_slice[i].split('-')
            heuristic_distances.update({separate[0]: int(separate[1])})


def populate_nodes_with_values(file_name: str, names: set[str]):
    nodes = {}
    for name in names:
        nodes.update({name: []})

    with open(file_name) as f:
        lines = f.read().splitlines()

    i = 0
    for line in lines:
        if i == 0:
            i += 1
            continue

        split = line.split(' ')
        node_name = split[0]
        neighbour_name = split[1]
        value = int(split[2])

        nodes[node_name].append({neighbour_name: value})

    return nodes


def populate_nodes(file_name: str, names: set[str]):
    nodes = {}
    heuristic_distances = {}
    for name in names:
        nodes.update({name: []})

    with open(file_name) as f:
        # https://stackoverflow.com/questions/12330522/how-to-read-a-file-without-newlines
        lines = f.read().splitlines()

    i = 0
    for line in lines:
        if i == 0:
            populate_heuristic_values(line, heuristic_distances)
            i += 1

        split = line.split(' ')
        node_name = split[0]
        neighbour_name = split[1]
        nodes[node_name].append(neighbour_name)
    return nodes, heuristic_distances


def print_nodes(nodes: dict[str:list]):
    for key, value in nodes.items():
        print(key, value)
    print()


def branch_and_bounds(nodes: dict[str:list], heuristic_distances: dict[str:int]):
    names = ['basic', 'extended list', 'heuristic', 'A*']
    for version in names:
        print('Branch and Bound ' + version)
        print('Nodes that were examined: ', end="")
        if version == 'heuristic' or version == 'A*':
            bnb = BranchAndBound(nodes, version, heuristic_distances)
        else:
            bnb = BranchAndBound(nodes, version)
        print(f'Best path: {bnb.algorithm()}')
        print()


def bfs_and_dfss(nodes: dict[str:list]):
    print(bfs_and_dfs.bfs(nodes, 'S', 'G'))
    print(bfs_and_dfs.dfs(nodes, 'S', 'G'))


def best_first_and_beam(nodes: dict[str:list], width: int, version: str, heu):
    # https://www.baeldung.com/cs/beam-search
    # not working currently
    open_list = [{'S': 0}]
    closed_list = []
    min_value = 99999
    min_key = ''
    path = ''
    while len(open_list) != 0:
        min_value = 99999
        for item in open_list:
            for key, value in item.items():
                if value < min_value:
                    min_value = value
                    min_key = key
        best_node = {min_key: min_value}
        open_list.remove(best_node)
        closed_list.append(best_node)

        if min_key == 'G':
            path += min_key
            return path

        neighbours = nodes[min_key]
        for item in neighbours:
            if item not in open_list and item not in closed_list:
                open_list.append(item)
            elif item in open_list:
                # ???
                pass
            elif item not in closed_list:
                open_list.append(item)

        if version == 'beam':
            if len(open_list) > width:
                smallest_values = sorted(open_list, key=lambda x: list(x.values())[0])[:width]
                open_list = smallest_values
                print(open_list)
    return path


def hill_climbing(nodes: dict[str:list], heuristic_distances: dict[str:int]):
    key = 'S'
    path = key
    key_to_continue = ''
    min_number = 99999
    is_algorithm_ended = False
    extensions = 0
    possible_next_nodes = []
    while True:
        min_number = 99999
        for current_node in nodes[key]:
            extensions += 1
            if current_node == 'G':
                path += current_node
                is_algorithm_ended = True
                break
            possible_next_nodes.append(current_node)

        if is_algorithm_ended:
            break

        for name in possible_next_nodes:
            value = heuristic_distances[name]
            if value < min_number:
                min_number = value
                key_to_continue = name
        possible_next_nodes.remove(key_to_continue)
        path += key_to_continue
        key = key_to_continue
    return path, extensions


def best_first_search(graph, heuristics):
    start_time = time.time()

    queue = [{'node': 'S', 'path': ['S'], 'cost': 0, 'heuristic': heuristics['S']}]
    visited = set()
    visited.add('S')
    goal = 'G'
    extensions = 0

    while queue:
        queue.sort(key=lambda x: x['heuristic'])
        current_node_info = queue.pop(0)
        node, path, cost = current_node_info['node'], current_node_info['path'], current_node_info['cost']

        if node == goal:
            end_time = time.time()
            time_elapsed = end_time - start_time
            print(f"Route: {''.join(path)}")
            print(f"Expansions count: {extensions}")
            print(f"Best First Search run time: {time_elapsed * 1000} ms")
            return

        current_node = graph[node]
        for item in current_node:
            extensions += 1
            for key, value in item.items():
                if key not in path and key not in visited:
                    visited.add(key)
                    new_path = path + [key]
                    new_cost = value + cost
                    heuristic_value = heuristics.get(key, 0)
                    queue.append({'node': key, 'path': new_path, 'cost': new_cost, 'heuristic': heuristic_value})

    end_time = time.time()
    time_elapsed = end_time - start_time
    print("Destination not found")
    print(f"Best First Search run time: {time_elapsed * 1000} ms")


def graphs(i: int):
    node_names = [{'A', 'B', 'C', 'D'},
                  {'S', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'X', 'Y'},
                  {'S', 'X', 'Y', 'Z', 'W', 'G'},
                  {'S', 'A', 'B', 'C', 'G'},
                  {'S', 'A', 'B', 'C', 'D', 'G'}]
    nodes, heuristic_distances = populate_nodes(f'datas/graph_{i}.txt', node_names[i - 1])
    nodes_with_values = populate_nodes_with_values(f'datas/graph_{i}.txt', node_names[i - 1])
    bfs_and_dfss(nodes)
    print(hill_climbing(nodes, heuristic_distances))
    best_first_search(nodes_with_values, heuristic_distances)
    # print_nodes(nodes)
    # print_nodes(nodes_with_values)
    branch_and_bounds(nodes_with_values, heuristic_distances)
    print()


def main():
    while True:
        print('1, First Graph')
        print('2, Second Graph')
        print('3, Third Graph')
        print('4, Fourth Graph')
        print('5, Fifth Graph')
        inp = input('Which graph would you like to see?: ')
        i = 0
        match inp:
            case '1' | '2' | '3' | '4' | '5':
                i = int(inp)
            case 'end':
                break
            case _:
                print("Wrong input! Numbers only.", end='\n\n')
                continue
        graphs(i)


if __name__ == "__main__":
    main()
