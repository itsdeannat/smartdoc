import typer

from .analyze import analyze
from .summarize import summarize


app = typer.Typer()


@app.callback()
def main():
    pass

app.command(name="analyze")(analyze)
app.command(name="summarize")(summarize)


if __name__ == "__main__":
    app()