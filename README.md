#LOL

`lol` is a command line utility with the intent of creating easy alternatives
for everyday commands.

For instance, creating a tarball for a directory requires several command line
arguments which almost always require a google search prior to running.  Or
starting an HTTP server to serve the current directory over localhost.

`lol` is written with Python3.4, it hasn't been tested on anything else.


#Quick Start

```
$ pip install git+https://github.com/tshauck/lol.git
$ lol --help
```

##`lol --help`

    Usage: lol [OPTIONS] COMMAND [ARGS]...

    Options:
      --help  Show this message and exit.

    Commands:
      random  Generate `n` random samples from the...
      serve   Start a server to serve a directory to...
      stats   Compute descriptive statistics on stream.
      tar     Create or extract a tar.

##Examples

    $ lol random --dist lognormal --location 10 --scale 1 3
    52200.70883183378
    45648.794092405995
    19868.651309040968

    $ lol random --dist uuid 2 | cut -d- -f1
    fe7a1fd6
    5da14713

    $ lol random --dist int --location 10 --scale 100 50 | lol stats
    mean    56.12
    median  58.5
    mode    97.0
