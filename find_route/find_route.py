#!/bin/env python3

from typing import Dict, List, Tuple
import typer
app = typer.Typer(add_completion=False)


def file_to_2D_array(file) -> List[List[str]]:
    '''
    Return the contents of a file as a list of lines.
    '''
    with open(file) as f:
        for line in f:
            if 'END OF INPUT' in line:
                break
            yield line.strip().split()


# CLI annotations
@app.command()
def main(
    input_filename: str = typer.Argument(..., help='Input filename'),
    origin_city: str = typer.Argument(
        ..., help='The city where the route starts'),
    destination_city: str = typer.Argument(
        ..., help='The city where the route ends'),
    heuristic_filename: str = typer.Argument(
        None, help='Path to file containing \'dst weight\' tuples')
):
    # initialize constants
    edges = {
        (src, dst): int(distance)
        for src, dst, distance in file_to_2D_array(input_filename)
    }
    edges.update({(dst, src): distance for (
        src, dst), distance in edges.items()})
    heuristic = {dst: 0 for _, dst in edges}
    if heuristic_filename:
        heuristic.update({
            city: int(h)
            for city, h
            in file_to_2D_array(heuristic_filename)
        })

    # initialize variables
    expanded = 0
    generated = 1
    fringe = [(0, origin_city, [])]  # cost, city, path
    visited = []

    solution_cost = None
    solution_path = None

    while len(fringe) > 0:
        # Pop the first element from the sorted fringe
        cost, city, path = fringe.pop()
        expanded += 1
        if city == destination_city:
            # found the destination, stopping search
            visited.append(city)
            solution_cost = cost
            solution_path = path + [destination_city]
            break
        if city in visited:
            # already visited this city, skipping
            continue
        # adding city to visited
        visited.append(city)
        # adding children to fringe
        for (src, dst), distance in edges.items():
            if src == city:
                fringe.append((cost + distance, dst, path + [src]))
                generated += 1
        # sorting fringe
        fringe.sort(key=lambda x: x[0]+heuristic[x[1]], reverse=True)

    # print results
    print(f'nodes expanded: {expanded}')
    print(f'nodes generated: {generated}')
    if solution_cost is None or solution_path is None:
        solution_cost = 'infinity'
        print('route:')
        print('none')
    else:
        print(f'distance: %.1f km' % solution_cost)
        for src, dst in zip(solution_path[:-1], solution_path[1:]):
            print(f'{src} to {dst}, %.1f km' % edges[(src, dst)])


if __name__ == '__main__':
    app()
