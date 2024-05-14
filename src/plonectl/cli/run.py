from pathlib import Path
from plonectl import utils
from typing_extensions import Annotated

import typer


typer_app = typer.Typer()


def _script_callback(value: Path):
    if not value.exists():
        raise typer.BadParameter(f"Script {value} not found.")
    return value


@typer_app.callback(invoke_without_command=True, no_args_is_help=True)
def main(
    ctx: typer.Context,
    script: Annotated[
        Path,
        typer.Argument(
            help=("Path to a script to be run"),
            callback=_script_callback,
        ),
    ],
):
    """Run a script."""
    utils.run_script(ctx=ctx, path=script)
