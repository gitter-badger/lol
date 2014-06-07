#LOL

`lol` is a command line utility with the intent of creating easy alternatives
for everyday commands.

For instance, creating a tarball for a directory requires several command line
arguments which almost always require a google search prior to running.  Or
starting an HTTP server to serve the current directory over localhost.

`lol` is written with Python3.4, it hasn't been testing on anything else.


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
      tar     Create a tar.
