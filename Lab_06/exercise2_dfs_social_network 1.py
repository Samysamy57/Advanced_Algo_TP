"""
Exercise 2: Graph Traversals - DFS for Social Network Analysis
"""


class SocialGraph:

    def __init__(self, num_users):
        self.num_users = num_users
        self.adj_list = {}
        for i in range(num_users):
            self.adj_list[i] = []

    def add_friendship(self, u, v):

        if u == v:
            return
        if v not in self.adj_list[u]:
            self.adj_list[u].append(v)
            self.adj_list[u].sort()  
        if u not in self.adj_list[v]:
            self.adj_list[v].append(u)
            self.adj_list[v].sort()

    def get_friends(self, u):
        return self.adj_list[u]

    def get_degree(self, u):
  
        return len(self.adj_list[u])

    def get_num_users(self):
        return self.num_users

    def get_num_edges(self):
  
        total_degree = 0
        for u in self.adj_list:
            total_degree = total_degree + len(self.adj_list[u])
        return total_degree // 2


# ---- Part A - Recursive DFS ----

def dfs_recursive_helper(graph, user, visited, result):
    visited[user] = True
    result.append(user)

    friends = graph.get_friends(user)
    for friend in friends:
        if visited[friend] == False:
            dfs_recursive_helper(graph, friend, visited, result)


def dfs_recursive(graph, start_user):
    visited = [False] * graph.get_num_users()
    result = []

    dfs_recursive_helper(graph, start_user, visited, result)
    return result


# ---- Part B - Iterative DFS with stack ----

def dfs_iterative(graph, start_user):
    visited = [False] * graph.get_num_users()
    result = []
    stack = []

    stack.append(start_user) 

    while len(stack) > 0:  
        current = stack.pop()  

        if visited[current] == False:
            visited[current] = True
            result.append(current)

            friends = graph.get_friends(current)
            for friend in friends:
                if visited[friend] == False:
                    stack.append(friend) 

    return result


# ---- Part C - Connected Components ----

def find_connected_components(graph):
    visited = [False] * graph.get_num_users()
    all_components = []
    users = graph.get_num_users()

    for i in range(users):
        if visited[i] == False:
            component = []
            dfs_recursive_helper(graph, i, visited, component)
            all_components.append(component)

    return all_components


# ---- Part D - Is Connected  ----

def is_connected(graph):
    components = find_connected_components(graph)

    if len(components) == 1:
        return True
    else:
        return False


# ---- Part E - Has Path  ----

def has_path(graph, start_user, target_user):
    visited = [False] * graph.get_num_users()
    stack = []

    stack.append(start_user)  

    while len(stack) > 0:  
        current = stack.pop()  

        if current == target_user:
            return True

        if visited[current] == False:
            visited[current] = True
            friends = graph.get_friends(current)
            for friend in friends:
                if visited[friend] == False:
                    stack.append(friend)  
    return False


# ---- Part F - Find Path ----

def find_path(graph, start_user, target_user):
    visited = [False] * graph.get_num_users()
    parent = {}
    stack = []
    path = []

    stack.append(start_user)  
    parent[start_user] = None

    while len(stack) > 0:  
        current = stack.pop()  

        if current == target_user:
            curr = target_user
            while curr is not None:
                path.append(curr)
                curr = parent[curr]
            path.reverse()
            return path

        if visited[current] == False:
            visited[current] = True

            friends = graph.get_friends(current)
            for friend in friends:
                if visited[friend] == False:
                    parent[friend] = current
                    stack.append(friend)  

    return []




def get_connected_components_sizes(graph):
    sizes = []
    components = find_connected_components(graph)

    for comp in components:
        sizes.append(len(comp))

    return sizes


def find_largest_component(graph):
    largest = []
    max_size = 0
    components = find_connected_components(graph)

    for comp in components:
        if len(comp) > max_size:
            max_size = len(comp)
            largest = comp

    return largest


def find_isolated_users(graph):

    isolated = []
    users = graph.get_num_users()

    for i in range(users):
        if graph.get_degree(i) == 0:
            isolated.append(i)

    return isolated


# ---- Tests ----

if __name__ == "__main__":
    g = SocialGraph(9)

    g.add_friendship(0, 1)
    g.add_friendship(1, 3)
    g.add_friendship(1, 4)
    g.add_friendship(3, 7)
    g.add_friendship(4, 5)
    g.add_friendship(5, 7)
    g.add_friendship(2, 4)
    g.add_friendship(2, 6)


    print("Social Network Graph")
    print("Users:", g.get_num_users())
    print("Edges:", g.get_num_edges())

    print("\n Part A: Recursive DFS from 0 ")
    print(dfs_recursive(g, 0))

    print("\nPart B: Iterative DFS from 0 ")
    print(dfs_iterative(g, 0))

    print("\nPart C: Connected Components ")
    for i, comp in enumerate(find_connected_components(g)):
        print("  Component", i + 1, ":", comp)

    print("\n Part D: Is Connected ")
    print(is_connected(g))

    print("\n Part E: Has Path ")
    print("0 -> 7:", has_path(g, 0, 7))
    print("0 -> 8:", has_path(g, 0, 8))

    print("\n Part F: Find Path ")
    print("0 -> 7:", find_path(g, 0, 7))
    print("0 -> 8:", find_path(g, 0, 8))

    print("\n Analytics ")
    print("Component sizes:", get_connected_components_sizes(g))
    print("Largest component:", find_largest_component(g))
    print("Isolated users:", find_isolated_users(g))
