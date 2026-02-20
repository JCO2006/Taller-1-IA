from typing import Any, Tuple
from algorithms import utils
from algorithms.problems import MultiSurvivorProblem


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def manhattanHeuristic(state, problem):
    """
    The Manhattan distance heuristic.
    """
    # TODO: Add your code here
    utils.raiseNotDefined()


def euclideanHeuristic(state, problem):
    """
    The Euclidean distance heuristic.
    """
    # TODO: Add your code here
    utils.raiseNotDefined()


def survivorHeuristic(state: Tuple[Tuple, Any], problem: MultiSurvivorProblem):
    """
    Your heuristic for the MultiSurvivorProblem.

    state: (position, survivors_grid)
    problem: MultiSurvivorProblem instance

    This must be admissible and preferably consistent.

    Hints:
    - Use problem.heuristicInfo to cache expensive computations
    - Go with some simple heuristics first, then build up to more complex ones
    - Consider: distance to nearest survivor + MST of remaining survivors
    - Balance heuristic strength vs. computation time (do experiments!)
    """
    # TODO: Add your code here

    position, survivors_grid = state
    survivors = survivors_grid.asList()

    # Si no quedan sobrevivientes
    if len(survivors) == 0:
        return 0

    # re basica Distancia al sobreviviente más cercano 
    manhattan_distances = []
    for s in survivors:
        d = abs(position[0] - s[0]) + abs(position[1] - s[1])
        manhattan_distances.append(d)

    nearest_distance = min(manhattan_distances)

    # --- MST entre sobrevivientes restantes ---
    # Usamos algoritmo tipo Prim sencillo

    mst_cost = 0
    visited = set()
    remaining = set(survivors)

    # Empezamos desde un sobreviviente cualquiera
    current = survivors[0]
    visited.add(current)
    remaining.remove(current)

    while remaining:
        min_edge = float("inf")
        next_node = None

        for v in visited:
            for r in remaining:
                d = abs(v[0] - r[0]) + abs(v[1] - r[1])
                if d < min_edge:
                    min_edge = d
                    next_node = r

        mst_cost += min_edge
        visited.add(next_node)
        remaining.remove(next_node)

    return nearest_distance + mst_cost