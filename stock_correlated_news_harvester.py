from argparse import ArgumentParser

import sys

from processors.news_analysis_processor import NewsAnalysisProcessor
from utils import log_helper
from utils.options import Options

log = log_helper.get_logger(__name__)


def main(argv):
    """
    Main function to kick start execution
    :param argv:
    :return: null
    """
    options = parse_args(argv)
    log.info("options: " + str(options))

    processor = NewsAnalysisProcessor(options)
    processor.process()


def parse_args(argv):
    """
    Parses command line arguments form an options object
    :param argv:
    :return:
    """
    parser = ArgumentParser(prog="stock-news-corpora-analysis")
    parser.add_argument('--stock_news_path', metavar='Stock News Path',
                        type=str, required=True)

    return parser.parse_args(argv, namespace=Options())


if __name__ == "__main__":
    main(sys.argv[1:])
