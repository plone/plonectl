from plonectl.utils import get_app_from_ctx
from typing_extensions import Annotated

import typer


typer_app = typer.Typer()


@typer_app.command()
def changepassword(
    ctx: typer.Context,
    username: str,
    password: Annotated[
        str, typer.Option(prompt=True, confirmation_prompt=True, hide_input=True)
    ],
):
    """Change password for a user."""
    import transaction

    app = get_app_from_ctx(ctx)
    acl_users = app.acl_users
    user = acl_users.getUser(username)
    if not user:
        typer.echo(f"User {username} does not exist.", err=True)
    else:
        with transaction.manager as tm:
            if "users" in acl_users.objectIds():
                acl_users.users.updateUserPassword(username, password)
            else:
                # Old user folder
                acl_users._doChangeUser(username, password, user.roles, user.domains)
            tm.note(f"Change password for user {username}")
        app._p_jar.sync()


@typer_app.command()
def createsuperuser(
    ctx: typer.Context,
    username: str,
    password: Annotated[
        str, typer.Option(prompt=True, confirmation_prompt=True, hide_input=True)
    ],
):
    """Create a new Manager on the root User Folder."""
    import transaction

    app = get_app_from_ctx(ctx)
    acl_users = app.acl_users
    user = acl_users.getUser(username)
    if user:
        typer.echo(f"There is an user {username} already.", err=True)
    else:
        typer.echo(f"Create a new manager user {username} - {password}")
        with transaction.manager as tm:
            if "users" in acl_users.objectIds():
                # Add user
                acl_users.users.addUser(username, username, password)
                # Add user to Role Manager
                acl_users.roles.assignRoleToPrincipal("Manager", username)
            else:
                # Old user folder
                roles = [
                    "Manager",
                ]
                domains = []
                acl_users._doAddUser(username, password, roles, domains)
            tm.note(f"Created new Manager: {username}")
        app._p_jar.sync()
