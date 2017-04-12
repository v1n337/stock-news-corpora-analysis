from os import walk
import logging

log = logging.getLogger(__name__)


def get_files(path):
    news_files = list()
    for root, dirs, files in walk(path):
        news_files.extend(map(lambda x: root + "/" + x, filter(lambda x : x[0] != ".", files)))

    return news_files


def extract_headline_from_file(file_path):
    try:
        with open(file_path) as file:
            all_lines = file.readlines()

        article_dict = dict()
        article_dict['headline'] = all_lines[0].lstrip("-- ").strip()
        article_dict['publish_date'] = all_lines[2].lstrip("-- ").strip()
        article_dict['article_text'] = (" ".join(all_lines[4:])).strip()
        article_dict['file_path'] = file_path

        if article_dict['headline'] and article_dict['publish_date'] and article_dict['article_text']:
            return article_dict

    except Exception as e:
        log.error("Skipped a headline " + str(file_path))
        log.error(e)
