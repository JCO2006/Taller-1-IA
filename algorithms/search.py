from algorithms.problems import SearchProblem
import algorithms.utils as utils
from world.game import Directions
from algorithms.heuristics import nullHeuristic
from algorithms import utils


def tinyHouseSearch(problem: SearchProblem):
    """
    Returns a sequence of moves that solves tinyHouse. For any other building, the
    sequence of moves will be incorrect, so only use this for tinyHouse.
    """
    s = Directions.SOUTH
    w = Directions.WEST
    return [s, s, w, s, w, w, s, w]


def depthFirstSearch(problem: SearchProblem):
    """
    Search the deepest nodes in the search tree first.
    """
    #Usamos un stack, importado de utils.py
    frontier = utils.Stack()
    
    # El estado en la frontera guarda
    start_state = problem.getStartState()
    frontier.push((start_state, []))
    
    # Usamos un Set para buscar los nodos que ya visitamos
    visited = set()
    
    while not frontier.isEmpty():
        current_state, actions = frontier.pop()
        
        # Si sacamos el estado objetivo, retornamos el camino que armamos
        if problem.isGoalState(current_state):
            return actions
        
        if current_state not in visited:
            visited.add(current_state)
            
            # getSuccessors retorna una tupla
            for next_state, action, stepCost in problem.getSuccessors(current_state):
                # Solo agregamos a la pila si no lo hemos visitado antes
                if next_state not in visited:
                    # Concatenamos 
                    new_actions = actions + [action]
                    frontier.push((next_state, new_actions))
                    
    return []

def breadthFirstSearch(problem: SearchProblem):
    """
    Search the shallowest nodes in the search tree first.
    """
    # Usamos un queue para BFS, esa es la unica diferencia con DFS.
    frontier = utils.Queue()
    
    start_state = problem.getStartState()
    frontier.push((start_state, []))
    
    visited = set()
    
    while not frontier.isEmpty():
        current_state, actions = frontier.pop()
        
        if problem.isGoalState(current_state):
            return actions
            
        if current_state not in visited:
            visited.add(current_state)
            
            for next_state, action, stepCost in problem.getSuccessors(current_state):
                if next_state not in visited:
                    new_actions = actions + [action]
                    frontier.push((next_state, new_actions))
                    
    return []


def uniformCostSearch(problem: SearchProblem):
    """
    Search the node of least total cost first.
    """
    
    frontier = utils.PriorityQueue()
    

    start_state = problem.getStartState()
    
    frontier.push((start_state, [], 0), 0)
    
    visited = set()
    
    while not frontier.isEmpty():
        
        state, actions, cost = frontier.pop()
        
        if problem.isGoalState(state):
            return actions
        
        if state not in visited:
            visited.add(state)
            
            for successor, action, stepCost in problem.getSuccessors(state):
                
                new_cost = cost + stepCost
                new_actions = actions + [action]
                
                frontier.push((successor, new_actions, new_cost), new_cost)
    
    return []
    # TODO: Add your code here
    utils.raiseNotDefined()


def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic):
    """
    Search the node that has the lowest combined cost and heuristic first.
    """
    frontier = utils.PriorityQueue()
    
    start_state = problem.getStartState()
    h_start = heuristic(start_state, problem)
    frontier.push((start_state, [], 0), h_start)
    
    visited = set()
    
    while not frontier.isEmpty():
        state, actions, cost = frontier.pop()
        
        if problem.isGoalState(state):
            return actions
        
        if state not in visited:
            visited.add(state)
            
            for successor, action, stepCost in problem.getSuccessors(state):
                new_cost = cost + stepCost
                new_actions = actions + [action]
                h_successor = heuristic(successor, problem)
                f_score = new_cost + h_successor
                
                frontier.push((successor, new_actions, new_cost), f_score)
    
    return []


# Abbreviations (you can use them for the -f option in main.py)
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
