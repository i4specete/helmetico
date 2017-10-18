import click
from helmetico.commons.aws_helpers import *

@click.group(help="Create secure AWS commands ")
@click.pass_context
def create(ctx, **kwargs):
    pass

@create.command(help="Create AWS Credentials")
@click.pass_context
@click.option("--profile","-p",help="Profile AWS",required=True)
@click.option("--accesskey","-a",help="Access Key to access to AWS account",required=True)
@click.option("--secretkey","-s",help="Secret Key to access to AWS account",required=True)
def credentials(ctx, **kwargs):
    store_credentials_aws(kwargs["profile"],kwargs["accesskey"],kwargs["secretkey"])


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


