import json
import logging
from datetime import datetime, timedelta

from gensim.models import Doc2Vec
from gensim.models.doc2vec import TaggedDocument
from sklearn.metrics.pairwise import cosine_similarity

from processors.processor import Processor
from utils import file_helper

stock_terms = {'stock', 'share'}
trend_terms = {'surge', 'rise', 'shrink', 'jump', 'drop', 'fall', 'plunge', 'gain', 'slump'}
lookback_days = 7

log = logging.getLogger(__name__)


def is_stock_article(article_dict):

    split_headline = set(article_dict['headline'].split())

    return article_dict and article_dict['headline'] \
            and article_dict['publish_date'] and article_dict['article_text'] \
            and split_headline & stock_terms and split_headline & trend_terms


def pair_with_similar_article(news_object, news_objects, docvec_model, date_to_id_map):

    article_pair_dict = dict()
    article_pair_dict['original'] = news_object

    source_vector = docvec_model.infer_vector(news_object['article_text'].split())
    source_date = datetime.fromtimestamp(news_object['publish_date']).date()

    articles_within_range = list()
    for i in range(lookback_days):
        current_date = source_date - timedelta(days=i)
        articles_within_range.extend(date_to_id_map[current_date])

    most_similar_article = None
    best_cosine_similarity = None
    for article_id in articles_within_range:
        current_cosine_similarity = \
            cosine_similarity(
                source_vector,
                docvec_model.infer_vector(news_objects[article_id]['article_text'].split())
            )

        if not most_similar_article or best_cosine_similarity > current_cosine_similarity:
            most_similar_article = news_objects[article_id]
            best_cosine_similarity = current_cosine_similarity

    article_pair_dict['most_similar'] = most_similar_article

    return article_pair_dict


def create_date_to_id_map(news_objects):

    date_to_id_map = dict()
    for news_object in news_objects:
        date = datetime.fromtimestamp(news_object['publish_date']).date()

        if date in date_to_id_map.keys():
            tmp_list = date_to_id_map[date]
            tmp_list.append(news_object['id'])
            date_to_id_map[date] = tmp_list
        else:
            date_to_id_map[date] = [news_object['id']]

    return date_to_id_map


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

        log.info("Creating date-wise map")
        date_to_id_map = create_date_to_id_map(news_objects)

        similar_articles_list = \
            map(lambda x:
                pair_with_similar_article(x, news_objects, model, date_to_id_map),
                stock_news_objects)

        with open(self.options.output_file, 'w') as output_file:
            output_file.write(json.dumps(similar_articles_list, indent=4) + "\n")

        log.info("NewsExtractionProcessor completed")
