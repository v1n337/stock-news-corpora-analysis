import argparse


def source(value):
    if value != 'reuters' and value != 'bloomberg':
        raise argparse.ArgumentTypeError("Invalid News source")
    else:
        return value
