import click
from helmetico.commons.aws_helpers import *


@click.group(help="Delete secure AWS commands")
@click.pass_context
def delete(ctx, **kwargs):
    pass

@delete.command(help="Create AWS Credentials")
@click.pass_context
@click.option("--profile","-p",help="Profile AWS",required=True)
def credentials(ctx, **kwargs):
    delete_credentials_aws(kwargs["profile"])

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
