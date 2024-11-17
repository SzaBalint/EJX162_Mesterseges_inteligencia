import time


class BranchAndBound:
    nodes = {}
    index = 'S'
    to_add = 0
    global_min = 99999
    possible_next_nodes = []
    is_g_reached = False
    previous_paths = []
    best_path = ''
    is_algorithm_ended = False
    extensions = 0
    extended_list: set[int] = set()
    goal_index = 'G'
    version = ''
    heuristic_distances = {}

    def __init__(self, nodes: dict[str:list], version: str, heuristic_distances: dict[str:int] = None):
        self.nodes = nodes
        self.version = version
        if heuristic_distances is not None:
            self.heuristic_distances = heuristic_distances

        self.possible_next_nodes.clear()
        self.extended_list.clear()
        self.previous_paths.clear()

    def algorithm(self):
        start = time.time()
        while True:
            print(self.index, end="")
            self.read_neighbours()
            self.get_least_value_node()
            if self.is_algorithm_ended:
                print()
                print(f'Extensions: {self.extensions}')
                print(f'Time elapsed: {time.time() - start}s')
                return self.best_path

    def read_neighbours(self):
        insertion_index = 0
        continue_outer_for_loop = False
        for neighbour in self.nodes[self.index]:
            for key, value in neighbour.items():
                self.extensions += 1
                key += f'<-{self.index}'
                value += self.to_add
                if self.version == 'heuristic' or self.version == 'A*':
                    value += self.heuristic_distances[key.split('<-')[0]]
                if key.split('<-')[0] == self.goal_index:
                    print(key.split('<-')[0], end="")
                    if value < self.global_min:
                        self.global_min = value
                        self.best_path = self.search_among_previous_paths(key)
                        self.previous_paths.append(self.best_path)
                    self.is_g_reached = True
                    continue_outer_for_loop = True
                    continue
                self.possible_next_nodes.insert(insertion_index, {key: value})
            if continue_outer_for_loop:
                continue
            insertion_index += 1

    def get_least_value_node(self):
        min_value = 999999
        key_to_continue = ''
        for obj in self.possible_next_nodes:
            key = list(obj.keys())[0]
            value = list(obj.values())[0]
            if self.version == 'extended list' or self.version == 'A*':
                if key.split('<-')[0] in self.extended_list:
                    continue
            if value < min_value:
                min_value = value
                key_to_continue = key
        if key_to_continue == '':
            self.is_algorithm_ended = True
            return
        self.possible_next_nodes.remove({key_to_continue: min_value})

        if self.version == 'extended list' or self.version == 'A*':
            self.extended_list.add(key_to_continue.split('<-')[0])

        if self.is_g_reached:
            if min_value >= self.global_min:
                self.is_algorithm_ended = True
                return

        if not self.search_among_previous_paths(key_to_continue):
            self.previous_paths.append('S' + key_to_continue.split('<-')[0])
        else:
            self.previous_paths.append(self.search_among_previous_paths(key_to_continue))

        self.index = key_to_continue.split('<-')[0]
        if self.version == 'heuristic' or self.version == 'A*':
            self.to_add = min_value - self.heuristic_distances[key_to_continue.split('<-')[0]]
        else:
            self.to_add = min_value

    def search_among_previous_paths(self, key):
        convert = key.split('<-')[1]
        for i in reversed(range(len(self.previous_paths))):
            if self.previous_paths[i].endswith(convert):
                return self.previous_paths[i] + key.split('<-')[0]

        return False
