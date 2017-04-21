from argparse import ArgumentParser

import sys

import logging

from processors.news_extraction_processor import NewsExtractionProcessor
from utils.options import Options
from data.news_sources import source

logging.basicConfig(
    level=logging.INFO,
    stream=sys.stdout,
    format='[%(asctime)s]: %(name)s : %(levelname)s : %(message)s'
)
log = logging.getLogger(__name__)


def main(argv):
    options = parse_args(argv)
    log.info("options: " + str(options))

    processor = NewsExtractionProcessor(options)
    processor.process()


def parse_args(argv):
    parser = ArgumentParser(prog="news-extraction")
    parser.add_argument('--news_source', metavar='News source',
                        type=source, required=True)
    parser.add_argument('--stock_news_path', metavar='Stock News Path',
                        type=str, required=True)
    parser.add_argument('--output_file', metavar='Output File',
                        type=str, required=True)

    return parser.parse_args(argv, namespace=Options())


if __name__ == "__main__":
    main(sys.argv[1:])
