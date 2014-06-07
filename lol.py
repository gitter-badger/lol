import click

import file_ops
import server
import random_numbers

@click.group()
def cli():
    pass

@cli.command()
@click.argument("infile")
def tar(infile):
    """Create a tar.gz or extract from one.

    Checks if the infile ends in .tar.gz, if it does, it extracts, otherwise
    it will create.
    """

    if infile.endswith(".tar.gz"):
        file_ops.extract_targz(infile)
    else:
        file_ops.create_targz(infile)

@cli.command()
@click.argument("port", type=int, required=False, default=8000)
def serve(port):
    """Start a server to serve a directory to localhost."""

    server.serve(port)

@cli.command()
@click.option("--dist", type=click.Choice(['normal', 'uniform']),
              default='normal', help="Samplign Distribution.")
@click.argument("n", type=int, required=False, default=1)
def random(dist, n):
    """Generate `n` random samples from the distribution."""

    for _ in range(n):
        rand_n = random_numbers.generate(dist)
        click.echo(rand_n)
