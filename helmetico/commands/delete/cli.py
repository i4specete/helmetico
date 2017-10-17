import click


@click.group(help="Delete secure AWS commands")
@click.pass_context
def delete(ctx, **kwargs):
    pass


@delete.command(help="Delete a secure IAM group")
@click.pass_context
@click.argument("TBD")
def iam(ctx, **kwargs):
    print("TBD")


@delete.command(help="Delete a secure networks")
@click.pass_context
@click.argument("TBD")
def network(ctx, **kwargs):
    print("TBD")


@delete.command(help="Delete a monitoring infraestructure")
@click.pass_context
@click.argument("TBD")
def monitor(ctx, **kwargs):
    print("TBD")
