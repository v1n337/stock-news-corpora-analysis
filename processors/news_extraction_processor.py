import json
import logging

from gensim.models import Doc2Vec
from gensim.models.doc2vec import TaggedDocument

from processors.processor import Processor
from utils import file_helper

log = logging.getLogger(__name__)


class NewsExtractionProcessor(Processor):

    def process(self):
        log.info("NewsExtractionProcessor begun")

        log.info("Getting file list")
        news_files = file_helper.get_files(self.options.stock_news_path)

        log.info("Parsing news from files")
        news_objects = \
            list(map(lambda x:
                     file_helper.extract_content_from_file(x, self.options.news_source),
                     news_files))
        news_objects = list(filter(lambda x: x, news_objects))
        log.info(str(len(news_objects)) + " news objects")

        log.info("Filtering stock news from all news")
        stock_news_objects = list(filter(file_helper.is_stock_article, news_objects))

        log.info("Training doc2vec model")
        tagged_news_objects = \
            list(map(lambda x: TaggedDocument(x['article_text'].split(), [x['id']]),
                     news_objects))
        model = Doc2Vec(tagged_news_objects, iter=50, workers=8, min_count=100)

        with open(self.options.output_file, 'w') as output_file:
            for news_object in stock_news_objects:
                output_file.write("original: " + json.dumps(news_object) + "\n")
                output_file.write("most-similar: " +
                                  json.dumps(
                                      model.most_similar(str(news_object['id']))
                                  ) + "\n")

        log.info("NewsExtractionProcessor completed")
