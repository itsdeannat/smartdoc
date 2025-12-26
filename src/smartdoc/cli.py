import typer

from .check import check


app = typer.Typer()


@app.callback()
def main():
    pass

app.command(name="check")(check)


if __name__ == "__main__":
    app()