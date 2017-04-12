class Options(object):
    stock_news_path = None
    output_file = None

    def __repr__(self):
        return \
            "stock_news_path: " + self.stock_news_path + \
            ", output_file: " + self.output_file
