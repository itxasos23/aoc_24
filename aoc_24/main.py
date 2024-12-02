import typer

import day_01
import day_02

aoc_days = [
    day_01.day,
    day_02.day,
]


app = typer.Typer()


@app.command("last")
def run_last_day():
    aoc_days[-1]()


if __name__ == "__main__":
    app()
