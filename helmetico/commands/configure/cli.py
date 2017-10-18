import click
from .aws_helpers import *

@click.group(help="Configure AWS commands ")
@click.pass_context
def configure(ctx, **kwargs):
    pass


@configure.command(help="Store AWS Credentials")
@click.pass_context
@click.option("--profile","-p",help="Profile AWS",required=True)
@click.option("--accesskey","-a",help="Access Key to access to AWS account",required=True)
@click.option("--secretkey","-s",help="Secret Key to access to AWS account",required=True)

def store(ctx, **kwargs):
    store_credentials_aws(kwargs["profile"],kwargs["accesskey"],kwargs["secretkey"])
    print("Storing AWS profile in ~/.aws/credentials......")

