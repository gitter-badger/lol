import statistics
import sys
import click

def mean(input_list):
    return statistics.mean(input_list)

def median(input_list):
    return statistics.median(input_list)

def mode(input_list):
    try:
        return statistics.mode(input_list)
    except statistics.StatisticsError as e:
        print(e, file=sys.stderr)
        return None
