import sys
import typer


typer_app = typer.Typer()


@typer_app.command()
def start(ctx: typer.Context):
    """Start server."""
    from Zope2.Startup.serve import main

    wsgiconf = ctx.obj.config.wsgiconf
    sys.exit(main(argv=["plonectl", str(wsgiconf)]))
