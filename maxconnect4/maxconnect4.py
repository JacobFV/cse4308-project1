#!/bin/env python3

from typing import Dict, List, Tuple
import typer
app = typer.Typer(add_completion=False)


@app.command()
def interactive(
    input_file: str = typer.Argument(..., help='Input filename'),
    first_player: str = typer.Option(...,
                                     help='"computer-first" or "human-first"'),
    depth: int = typer.Option(..., help='Depth of the search tree'),
):
    # 1. If computer-next, goto 2, else goto 5.
    # 2. Print the current board state and score. If the board is full, exit.
    # 3. Choose and make the next move.
    # 4. Save the current board state in a file called computer.txt (in same format as input file).
    # 5. Print the current board state and score. If the board is full, exit.
    # 6. Ask the human user to make a move (make sure that the move is valid, otherwise repeat request to the user).
    # 7. Save the current board state in a file called human.txt (in same format as input file).
    # 8. Goto 2.


@app.command('one-move')
def one_move(
    input_file: str = typer.Argument(..., help='Input filename'),
    output_file: str = typer.Argument(..., help='Output filename'),
    depth: int = typer.Argument(..., help='Depth of search'),
):
    pass


if __name__ == '__main__':
    app()
