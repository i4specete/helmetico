import click


@click.group(help="Create secure AWS commands ")
@click.pass_context
def create(ctx, **kwargs):
    pass


@create.command(help="Create a secure IAM group")
@click.pass_context
@click.argument("TBD")
def iam(ctx, **kwargs):
    print("TBD")


@create.command(help="Create a secure networks")
@click.pass_context
@click.argument("TBD")
def network(ctx, **kwargs):
    print("TBD")


@create.command(help="Create a monitoring infraestructure")
@click.pass_context
@click.argument("TBD")
def monitor(ctx, **kwargs):
    print("TBD")


