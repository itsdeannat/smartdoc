import typer

from .check import check
from .summarize import summarize


app = typer.Typer()


@app.callback()
def main():
    pass

app.command(name="check")(check)
app.command(name="summarize")(summarize)


if __name__ == "__main__":
    app()