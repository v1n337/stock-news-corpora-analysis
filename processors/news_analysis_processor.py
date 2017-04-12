import json
import logging

from processors.processor import Processor
from utils import file_helper

log = logging.getLogger(__name__)


class NewsAnalysisProcessor(Processor):

    def process(self):
        log.info("NewsAnalysisProcessor begun")

        news_files = file_helper.get_files(self.options.stock_news_path)
        news_objects = map(file_helper.extract_headline_from_file, news_files)

        with open(self.options.output_file, 'w') as output_file:
            for news_object in news_objects:
                output_file.write(json.dumps(news_object) + "\n")

        log.info("NewsAnalysisProcessor completed")
