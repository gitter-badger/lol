import click

import file_ops
import server
import random_numbers
import lol_statistics as ls

@click.group()
def cli():
    pass

@cli.command()
@click.argument("infile")
def tar(infile):
    """Create or extract a tar.gz or extract from one.

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
@click.option("--dist", type=click.Choice(['normal', 'uniform', 'uuid',
              'lognormal', 'int']),
              default='normal', help="Sampling Distribution")
@click.option("--location", type=float, help="Location Parameter", default=0)
@click.option("--scale", type=float, help="Scale Parameter", default=1)
@click.argument("n", type=int, required=False, default=1)
def random(dist, location, scale, n):
    """Generate `n` random samples from the distribution."""

    for _ in range(n):
        rand_n = random_numbers.generate(dist, location, scale)
        click.echo(rand_n)

@cli.command()
@click.option("--mean", is_flag=True)
@click.option("--median", is_flag=True)
@click.option("--mode", is_flag=True)
@click.option("--every/--not-every", default=True)
@click.argument("infile", type=click.File("r"), default='-', required=False)
def stats(mean, median, mode, every, infile):
    """Compute descriptive statistics on stream."""

    def tab_delimit(stat, x):
        click.echo("{}\t{}".format(stat, x))

    total = []
    for line in infile:
        total.append(line)

    input_list = [float(x.strip()) for x in total]

    if mean or every:
        mean_value = ls.mean(input_list)
        tab_delimit("mean", mean_value)
    if median or every:
        median_value = ls.median(input_list)
        tab_delimit("median", median_value)
    if mode or every:
        mode_value = ls.mode(input_list)
        if mode_value:
            tab_delimit("mode", mode_value)
