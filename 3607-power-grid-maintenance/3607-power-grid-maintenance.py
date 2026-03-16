import heapq
from collections import defaultdict

class Solution:
    def processQueries(self, c, connections, queries):

        parent = list(range(c+1))

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(a,b):
            pa,pb = find(a),find(b)
            if pa != pb:
                parent[pb] = pa

        # build components
        for u,v in connections:
            union(u,v)

        comp = defaultdict(list)

        for i in range(1, c+1):
            root = find(i)
            comp[root].append(i)

        # convert component nodes into heaps
        heaps = {}
        for root, nodes in comp.items():
            heapq.heapify(nodes)
            heaps[root] = nodes

        online = [True]*(c+1)

        ans = []

        for q,x in queries:

            if q == 2:
                online[x] = False

            else:
                if online[x]:
                    ans.append(x)
                else:
                    root = find(x)
                    heap = heaps[root]

                    while heap and not online[heap[0]]:
                        heapq.heappop(heap)

                    if heap:
                        ans.append(heap[0])
                    else:
                        ans.append(-1)

        return ans