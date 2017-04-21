import json
import logging

from processors.processor import Processor
from utils import file_helper

log = logging.getLogger(__name__)


class NewsExtractionProcessor(Processor):

    def process(self):
        log.info("NewsExtractionProcessor begun")

        news_files = file_helper.get_files(self.options.stock_news_path)
        news_objects = map(lambda x: file_helper.extract_content_from_file(x, self.options.news_source), news_files)

        with open(self.options.output_file, 'w') as output_file:
            for news_object in news_objects:
                if news_object:
                    output_file.write(json.dumps(news_object) + "\n")

        log.info("NewsExtractionProcessor completed")
