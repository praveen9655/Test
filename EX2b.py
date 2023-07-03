from queue import PriorityQueue
import sys

def memory_bounded_a_star(start_node, goal_node, max_memory):
    frontier = PriorityQueue()
    frontier.put((0, start_node))
    explored = set()
    total_cost = {start_node: 0}

    while not frontier.empty():
        # Check if memory limit has been reached
        if sys.getsizeof(explored) > max_memory:
            return None

        _, current_node = frontier.get()

        if current_node == goal_node:
            path = []
            while current_node != start_node:
                path.append(current_node)
                current_node = current_node.parent
            path.append(start_node)
            path.reverse()
            return path

        explored.add(current_node)

        for child_node, cost in current_node.children():
            if child_node in explored:
                continue

            new_cost = total_cost[current_node] + cost

            if child_node not in total_cost or new_cost < total_cost[child_node]:
                total_cost[child_node] = new_cost
                priority = new_cost + child_node.heuristic(goal_node)
                frontier.put((priority, child_node))

    return None
class Node:
    def __init__(self, state, parent=None):
        self.state = state
        self.parent = parent
        self.cost = 1

    def __eq__(self, other):
        return self.state == other.state

    def __hash__(self):
        return hash(self.state)

    def heuristic(self, goal):
        # Simple heuristic for demonstration purposes
        return abs(self.state - goal.state)

    def children(self):
        # Generates all possible children of a given node
        children = []
        for action in [-1, 1]:
            child_state = self.state + action
            child_node = Node(child_state, self)
            children.append((child_node, child_node.cost))
        return children

# Example usage
start_node = Node(1)
goal_node = Node(10)

path = memory_bounded_a_star(start_node, goal_node, max_memory=1000000)
if path is None:
    print("Memory limit exceeded.")
else:
    print("Path : ",[node.state for node in path])

