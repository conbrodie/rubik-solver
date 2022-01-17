#  o------o
#         |       
#         |
#  o<-----o
# each 4 letters are a face labeled from the top left, going clockwise
testData =  ("g","g","w","o", # top face
            "o","b","b","b", # left face
            "y","g","o","y", # front face
            "r","y","w","g", # right face
            "r","y","b","r", # bottom face
            "r","w","w","o") # back face
def F(v):
    return tuple(v[i] for i in [0,1,5,6,4,16,17,7,11,8,9,10,3,13,14,2,15,12,18,19,20,21,22,23])

def Fi(v):
    return tuple(v[i] for i in inverse([0,1,5,6,4,16,17,7,11,8,9,10,3,13,14,2,15,12,18,19,20,21,22,23]))
def U(v):
    return tuple(v[i] for i in [3,0,1,2,8,9,6,7,12,13,10,11,20,21,14,15,16,17,18,19,4,5,22,23])

def Ui(v):
    return tuple(v[i] for i in inverse([3,0,1,2,8,9,6,7,12,13,10,11,20,21,14,15,16,17,18,19,4,5,22,23]))

def R(v):
    return tuple(v[i] for i in [0,9,10,3,4,5,6,7,8,17,18,11,15,12,13,14,16,23,20,19,2,21,22,1])

def Ri(v):
    return tuple(v[i] for i in inverse([0,9,10,3,4,5,6,7,8,17,18,11,15,12,13,14,16,23,20,19,2,21,22,1]))

def inverse(p):
    return [p.index(i) for i in range(len(p))] 

def isSolved(currentConfig):
    C = {
        # W and Y
        # g front
        ("w","w","w","w","o","o","o","o","g","g","g","g","r","r","r","r","y","y","y","y","b","b","b","b"),
        # o front
        ("w","w","w","w","b","b","b","b","o","o","o","o","g","g","g","g","y","y","y","y","r","r","r","r"),
        # b front
        ("w","w","w","w","r","r","r","r","b","b","b","b","o","o","o","o","y","y","y","y","g","g","g","g"),
        # r front
        ("w","w","w","w","g","g","g","g","r","r","r","r","b","b","b","b","y","y","y","y","o","o","o","o"),

        # Y and W
        # G front
        ("y","y","y","y","r","r","r","r","g","g","g","g","o","o","o","o","w","w","w","w","b","b","b","b"),
        # O Front
        ("y","y","y","y","g","g","g","g","o","o","o","o","b","b","b","b","w","w","w","w","r","r","r","r"),
        # B Front
        ("y","y","y","y","o","o","o","o","b","b","b","b","r","r","r","r","w","w","w","w","g","g","g","g"),
        # R Front
        ("y","y","y","y","b","b","b","b","r","r","r","r","g","g","g","g","w","w","w","w","o","o","o","o"),

        # G and B
        # g front
        ("g","g","g","g","r","r","r","r","w","w","w","w","o","o","o","o","b","b","b","b","y","y","y","y"),
        # o front
        ("g","g","g","g","w","w","w","w","o","o","o","o","y","y","y","y","b","b","b","b","r","r","r","r"),
        # b front
        ("g","g","g","g","o","o","o","o","y","y","y","y","r","r","r","r","b","b","b","b","w","w","w","w"),
        # r front
        ("g","g","g","g","y","y","y","y","r","r","r","r","w","w","w","w","b","b","b","b","g","g","g","g"),

        # B and G
        # W front
        ("b","b","b","b","o","o","o","o","w","w","w","w","r","r","r","r","g","g","g","g","y","y","y","y"),
        # O front
        ("b","b","b","b","y","y","y","y","o","o","o","o","w","w","w","w","g","g","g","g","r","r","r","r"),
        # Y front
        ("b","b","b","b","r","r","r","r","y","y","y","y","o","o","o","o","g","g","g","g","w","w","w","w"),
        # r front
        ("b","b","b","b","w","w","w","w","r","r","r","r","y","y","y","y","b","b","b","b","o","o","o","o"),

        # O and R
        # Y front
        ("o","o","o","o","b","b","b","b","y","y","y","y","g","g","g","g","r","r","r","r","w","w","w","w"),
        # G front
        ("o","o","o","o","y","y","y","y","g","g","g","g","w","w","w","w","r","r","r","r","b","b","b","b"),
        # W front
        ("o","o","o","o","g","g","g","g","w","w","w","w","b","b","b","b","r","r","r","r","y","y","y","y"),
        # B front
        ("o","o","o","o","w","w","w","w","b","b","b","b","y","y","y","y","r","r","r","r","g","g","g","g"),

        # R and O
        # Y front
        ("r","r","r","r","g","g","g","g","y","y","y","y","b","b","b","b","o","o","o","o","w","w","w","w"),
        # G front
        ("r","r","r","r","w","w","w","w","g","g","g","g","y","y","y","y","o","o","o","o","b","b","b","b"),
        # W front
        ("r","r","r","r","b","b","b","b","w","w","w","w","g","g","g","g","o","o","o","o","y","y","y","y"),
        # B front
        ("r","r","r","r","y","y","y","y","b","b","b","b","w","w","w","w","o","o","o","o","g","g","g","g")}
    for solvedConfig in C:
        if vaildConfiguration(currentConfig, solvedConfig):
            return True
    return False

def vaildConfiguration(currentConfig, solvedConfig):
    return currentConfig == solvedConfig

def NS(u, S):
   V = { move(u) for move in {F,Fi,U,Ui,R,Ri} }
   E = { (v,u) for v in V } | { (u,v) for v in V }
   return { v for v in V for u in S if (u,v) in E }

def solution(problemInstance):  
    u = problemInstance
    explored = {()}
    queue = [[u]]
    if isSolved(u):
        return [0]
    while queue:
        path = queue.pop(0)
        u = path[-1]
        if u not in explored:
            D = {u}
            neighbours = NS(u, D)
            for n in neighbours:
                newPath = list(path)
                newPath.append(n)
                queue.append(newPath)
                if isSolved(n):
                    return newPath
            explored.add(u)
    

def printSolution(solutionInstance):
    print('Smallest number of moves required to solve:', (len(solutionInstance) - 1))


printSolution(solution(testData))



