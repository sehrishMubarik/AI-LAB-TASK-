from collections import deque

def waterJugProblemDFS(capacity1, capacity2, goal):
    stack = [(0, 0, [])]  
    visited = set()

    while stack:
        jug1, jug2, path = stack.pop()
        
        if (jug1, jug2) in visited:
            continue
        visited.add((jug1, jug2))
        new_path = path + [(jug1, jug2)]
        
        if jug1 == goal or jug2 == goal:
            print("Solution Found")
            print("Steps:")
            for action in new_path:
                print(action)
            return True


        rules = [
            (capacity1, jug2),  
            (jug1, capacity2),  
            (0, jug2),          
            (jug1, 0),          
            (jug1 - min(jug1, capacity2 - jug2), jug2 + min(jug1, capacity2 - jug2)),  
            (jug1 + min(jug2, capacity1 - jug1), jug2 - min(jug2, capacity1 - jug1)),  
        ]

        for new_state in rules:
            if new_state not in visited:
                stack.append((*new_state, new_path)) 
    print("No Solution found")
    return False

jug1Capacity = 4
jug2Capacity = 3
target = 2          
waterJugProblemDFS(jug1Capacity, jug2Capacity, target)

