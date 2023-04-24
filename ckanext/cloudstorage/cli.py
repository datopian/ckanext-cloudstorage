import click
from typing import Union

from ckanext.cloudstorage import utils


def get_commands():
    return [cloudstorage]


@click.group()
def cloudstorage():
    """
    Integrates with cloud providers
    """
    pass


@cloudstorage.command()
def initdb():
    utils.initdb()


@cloudstorage.command()
@click.option(
    "-o",
    "--output",
    default=None,
    help="The output file path.",
)
def list_unlinked_uploads(output: Union[str, None]):
    utils.list_linked_uploads(output)


@cloudstorage.command()
def remove_unlinked_uploads():
    utils.remove_unlinked_uploads()


@cloudstorage.command()
@click.option(
    "-o",
    "--output",
    default=None,
    help="The output file path.",
)
def list_missing_uploads(output: Union[str, None]):
    utils.list_missing_uploads(output)


@cloudstorage.command()
@click.option(
    "-o",
    "--output",
    default=None,
    help="The output file path.",
)
def list_linked_uploads(output: Union[str, None]):
    utils.list_linked_uploads(output)
