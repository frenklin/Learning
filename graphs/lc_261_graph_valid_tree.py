class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        # Create Graph
        graph_dic = {}

        for start,end in edges:
            if start not in graph_dic:
                graph_dic[start] = [end]
            else:
                graph_dic[start].append(end)

            if end not in graph_dic:
                graph_dic[end] = [start]
            else:
                graph_dic[end].append(start)

        # DFS to detect cycles
        visited = set()

        stack = [(0,-1)]

        while stack:

            node, parent = stack.pop()
            visited.add(node)
            if node in graph_dic:
                for next_node in graph_dic[node]:
                    if next_node not in visited:
                        stack.append((next_node, node))
                    else:
                        if next_node != parent:
                            return False

        # check if we can traverse all node
        if len(visited) != n:
            return False

        return True
# TimeComplexity O(V+E)
# https://www.youtube.com/watch?v=994TPE325bs
