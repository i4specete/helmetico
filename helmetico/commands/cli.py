import logging

import click

from helmetico.commons import shared_cmd_options
from .create.cli import create
from .delete.cli import delete
from .update.cli import update
from .configure.cli import configure


log = logging.getLogger('helmetico')


@shared_cmd_options.global_options()
@click.pass_context
def cli(ctx, **kwargs):
    ctx.obj = kwargs

cli.add_command(delete)
cli.add_command(create)
cli.add_command(update)
cli.add_command(configure)



if __name__ == "__main__" and __package__ is None:  # pragma no cover
    cli()
