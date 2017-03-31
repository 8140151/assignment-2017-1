from collections import deque

g = {
    0: [1, 2],
    1: [0, 2],
    2: [0, 1, 3, 4],
    3: [2, 4],
    4: [2, 3]
}


q = deque()

def bfs(g, node, q):

    visited = [False for k in g.keys()]
    inqueue = [False for k in g.keys()]

    q.appendleft(node)
    inqueue[node] = True

    combs = []
    combs2 =[]

    i = 1
    while not (len(q) == 0):
        c = q.pop()
        inqueue[c] = False
        visited[c] = True
        print("Visiting", c)
        i += 1
        for v in g[c]:
            if v > c:
               combs2.append((c,v))
               print("combs2",combs2)
            else:
               print("nothing")

            if  not visited[v] and not inqueue[v]:
                print("test", c, v)
                combs.append((c, v))
                print("combs",combs)
                q.appendleft(v)
                inqueue[v] = True

bfs(g, 0, q)

