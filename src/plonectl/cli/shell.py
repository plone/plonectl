from plonectl import utils
from typing_extensions import Annotated

import typer


typer_app = typer.Typer()


def _default_shell() -> str:
    """Return the default shell interface to use."""
    return utils.PloneShell.shells[0]


def _interface_callback(value: str):
    available_shells = utils.PloneShell.shells
    if value not in available_shells:
        raise typer.BadParameter(f"Only {', '.join(available_shells)} are supported")
    return value


@typer_app.callback(invoke_without_command=True, no_args_is_help=True)
def main(
    ctx: typer.Context,
    interface: Annotated[
        str,
        typer.Option(
            default_factory=_default_shell,
            help=(
                f"Which Python shell to use. Valid options are: {', '.join(utils.PloneShell.shells)}. "
                f"Default shell: {utils.PloneShell.shells[0]}. "
            ),
            show_default=False,
            callback=_interface_callback,
        ),
    ],
    site_id: Annotated[
        str,
        typer.Option(
            help="Plone site to be loaded on shell startup.",
            show_default=False,
        ),
    ] = "",
):
    """Start a shell inside the current installation.

    It is possible to choose the Python shell to be used.
    """
    shell = utils.PloneShell(ctx=ctx, shell=interface, default_site=site_id)
    # Start shell
    shell()
