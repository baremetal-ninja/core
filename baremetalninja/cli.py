import typer

from . import core

app = typer.Typer()

app.command(core.clean)
app.command(core.build)
