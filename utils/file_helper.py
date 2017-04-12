from datetime import datetime
from os import walk
import logging

from utils.options import Options

log = logging.getLogger(__name__)


def get_files(path):
    news_files = list()
    for root, dirs, files in walk(path):
        news_files.extend(map(lambda x: root + "/" + x, filter(lambda x : x[0] != ".", files)))

    return news_files


def extract_headline_from_file(file_path, news_source):
    try:
        with open(file_path) as file:
            all_lines = file.read()

        all_lines_split = all_lines.split("\n--")
        article_dict = dict()
        article_dict['headline'] = all_lines_split[0].strip()
        article_dict['publish_date'] = parse_date(all_lines_split[2].strip(), news_source)
        article_dict['article_text'] = all_lines[3].strip()
        article_dict['file_path'] = file_path

        if article_dict['headline'] and article_dict['publish_date'] and article_dict['article_text']:
            return article_dict

    except Exception as e:
        log.error("Skipped a headline " + str(file_path))
        log.error(e)

def parse_date(date_string, news_source):
    if news_source == 'reuters':
        return datetime.strptime(date_string, '%a %b %d, %Y %I:%M%p %Z').timestamp()
    elif news_source == 'bloomberg':
        datetime.strptime(date_string, "%Y-%m-%dT%H:%M:%SZ").timestamp()
    else:
        log.error("no news source selected " + str(news_source))
        exit(0)
