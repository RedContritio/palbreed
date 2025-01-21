import os
import json
import heapq

class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_edge(self, u, v, weight=1):
        if u not in self.adj_list:
            self.adj_list[u] = []
        self.adj_list[u].append((v, weight))

    def get_neighbors(self, u):
        return self.adj_list.get(u, [])


def dijkstra(graph, start, goal):
    distances = {}
    distances[start] = 0
    pq = [(0, start)]
    previous_nodes = {start: None}

    while pq:
        current_distance, current_node = heapq.heappop(pq)
        
        if current_node == goal:
            path = []
            while current_node is not None:
                path.insert(0, current_node)
                current_node = previous_nodes[current_node]
            return distances[goal], path
        
        print(current_node, graph.get_neighbors(current_node))
        for neighbor, weight in graph.get_neighbors(current_node):
            distance = current_distance + weight
            
            if neighbor not in distances or distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_node
                heapq.heappush(pq, (distance, neighbor))

    return -1, []


if __name__ == '__main__':
    data_dir = 'data'
    breed_data_dir = os.path.join(data_dir, "breed")
    i18n_data_dir = os.path.join(data_dir, "i18n")
    skills_data_dir = os.path.join(data_dir, "skills")
    
    pal_names = json.load(open(os.path.join(i18n_data_dir, "pal_names.json"), "r", encoding="utf-8"))
    
    breed_combi = json.load(open(os.path.join(breed_data_dir, "breed_combi.json"), "r", encoding="utf-8"))
    breed_gender = json.load(open(os.path.join(breed_data_dir, "breed_gender.json"), "r", encoding="utf-8"))
    breed_self = json.load(open(os.path.join(breed_data_dir, "breed_self.json"), "r", encoding="utf-8"))
    breed_unique = json.load(open(os.path.join(breed_data_dir, "breed_unique.json"), "r", encoding="utf-8"))
    
    passive_skills = json.load(open(os.path.join(skills_data_dir, "passive_skills.json"), "r", encoding="utf-8"))
    
    print(len(pal_names))
    print(len(breed_combi))
    print(len(passive_skills))
    
    g = Graph()
    g.add_edge('A', 'B', 1)
    g.add_edge('A', 'C', 2)
    g.add_edge('B', 'D', 3)
    g.add_edge('C', 'D', 1)
    g.add_edge('D', 'E', 2)
    shortest_path_length, path = dijkstra(g, 'A', 'E')
    
    print(shortest_path_length, path)
