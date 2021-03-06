import logging
from datetime import datetime
from os import walk

log = logging.getLogger(__name__)

headline_counter = 0


def get_files(path):
    news_files = list()
    for root, dirs, files in walk(path):
        news_files.extend(map(lambda x: root + "/" + x, filter(lambda x : x[0] != ".", files)))

    return news_files


def extract_content_from_file(file_path, news_source):

    global headline_counter
    try:
        with open(file_path) as file:
            all_lines = file.read()

        all_lines = "\n" + all_lines
        all_lines_split = all_lines.split("\n--")
        article_dict = dict()
        article_dict['id'] = headline_counter
        headline_counter += 1
        article_dict['headline'] = all_lines_split[1].strip()
        article_dict['publish_date'] = parse_date(all_lines_split[3].strip(), news_source)
        article_dict['article_text'] = all_lines_split[4].strip()
        article_dict['file_path'] = file_path

        return article_dict

    except Exception as e:
        log.error("Skipped a headline " + str(file_path))
        log.error(e)


def parse_date(date_string, news_source):
    if news_source == 'reuters':
        return datetime.strptime(date_string, '%a %b %d, %Y %I:%M%p %Z').date()
    elif news_source == 'bloomberg':
        return datetime.strptime(date_string, "%Y-%m-%dT%H:%M:%SZ").date()
    else:
        log.error("no news source selected " + str(news_source))
        exit(0)
