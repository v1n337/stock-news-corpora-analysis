from argparse import ArgumentParser

import sys

import logging

from processors.news_analysis_processor import NewsAnalysisProcessor
from utils.options import Options

logging.basicConfig(
    level=logging.INFO,
    stream=sys.stdout,
    format='[%(asctime)s]: %(name)s : %(levelname)s : %(message)s'
)
log = logging.getLogger(__name__)


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
    parser.add_argument('--output_file', metavar='Output File',
                        type=str, required=True)

    return parser.parse_args(argv, namespace=Options())


if __name__ == "__main__":
    main(sys.argv[1:])
