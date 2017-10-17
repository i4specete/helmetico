import click

@click.group("update", help="Update secure AWS commands")
@click.pass_context
def update(ctx, **kwargs):
    pass


@update.command(help="Update a secure IAM group")
@click.pass_context
@click.argument("TBD")
def iam(ctx, **kwargs):
    print("TBD")


@update.command(help="Update a secure networks")
@click.pass_context
@click.argument("TBD")
def network(ctx, **kwargs):
    print("TBD")


@update.command(help="Update a monitoring infraestructure")
@click.pass_context
@click.argument("TBD")
def monitor(ctx, **kwargs):
    print("TBD")
