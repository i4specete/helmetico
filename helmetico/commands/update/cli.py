import click
from helmetico.commons.aws_helpers import *
@click.group("update", help="Update secure AWS commands")
@click.pass_context
def update(ctx, **kwargs):
    pass

@update.command(help="Update AWS Credentials")
@click.pass_context
@click.option("--profile","-p",help="Profile AWS",required=True)
@click.option("--accesskey","-a",help="Access Key to access to AWS account",required=True)
@click.option("--secretkey","-s",help="Secret Key to access to AWS account",required=True)
def credentials(ctx, **kwargs):
    update_credentials_aws(kwargs["profile"],kwargs["accesskey"],kwargs["secretkey"])


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
