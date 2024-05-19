import traceback
import logging

## how to create a DFS
graph = {
  0 : [1, 3, 4],
  1 : [0, 2, 5],
  2 : [1],
  3 : [0, 5, 6, 7],
  4 : [0],
  5 : [1, 3],
  6 : [3, 7],
  7 : [0, 3, 6],
  8 : []
}

def dfs(graph, node):
    # The video has visited as an array. I changed this to set because 'n not in visited' is O(1) instead of O(n).
    # See this link for more: https://wiki.python.org/moin/TimeComplexity.
    visited = set()
    stack = []

    visited.add(node)
    stack.append(node) 

    while stack:
        s = stack.pop()
        print(s, end = " ")

        # Reverse iterate through the edge list so results match recursive version.
        for n in reversed(graph[s]):
            # Because visited is a set, this lookup is O(1).
            if n not in visited:
                visited.add(n)
                stack.append(n)

        
def main():
    try:
        dfs(graph, 2)
    except Exception as e:
        logging.error(traceback.format_exc())
        
main()



# how to visualize DFS