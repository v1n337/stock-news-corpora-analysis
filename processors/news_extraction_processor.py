import json
import logging

from gensim.models import Doc2Vec
from gensim.models.doc2vec import TaggedDocument

from processors.processor import Processor
from utils import file_helper

stock_terms = {'stock', 'share'}
trend_terms = {'surge', 'rise', 'shrink', 'jump', 'drop', 'fall', 'plunge', 'gain', 'slump'}

log = logging.getLogger(__name__)


def is_stock_article(article_dict):

    split_headline = set(article_dict['headline'].split())

    return article_dict and article_dict['headline'] \
            and article_dict['publish_date'] and article_dict['article_text'] \
            and split_headline & stock_terms and split_headline & trend_terms


def pair_with_similar_article(news_object, news_objects, docvec_model):

    article_pair_dict = dict()
    article_pair_dict['original'] = news_object
    article_pair_dict['most_similar'] = \
        news_objects[docvec_model.docvecs.most_similar(news_object['id'])[0][0]]

    return article_pair_dict


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
        stock_news_objects = list(filter(is_stock_article, news_objects))

        log.info("Training doc2vec model")
        tagged_news_objects = \
            list(map(lambda x: TaggedDocument(x['article_text'].split(), [x['id']]),
                     news_objects))
        model = Doc2Vec(tagged_news_objects, iter=50, workers=8, min_count=10)

        similar_articles_list = \
            map(lambda x: pair_with_similar_article(x, news_objects, model), stock_news_objects)

        with open(self.options.output_file, 'w') as output_file:
            for article_pair in similar_articles_list:
                output_file.write(json.dumps(article_pair, indent=4) + "\n")

        log.info("NewsExtractionProcessor completed")
