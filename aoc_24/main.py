import day_01
import day_02
import day_03
import day_04
import day_05
import typer

aoc_days = [
    day_01.day,
    day_02.day,
    day_03.day,
    day_04.day,
    day_05.day,
]


app = typer.Typer()


@app.command("last")
def run_last_day():
    aoc_days[-1]()


if __name__ == "__main__":
    app()
