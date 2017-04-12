#!/usr/bin/env bash

CODEDIR=$(dirname "$0")"/../"


STOCK_FILE_PATH="/home/v2john/Projects/financial-news-dataset/ReutersNews106521/"

/usr/bin/python3 "$CODEDIR"/stock_news_analyzer.py \
--stock_news_path "$STOCK_FILE_PATH"


#STOCK_FILE_PATH="/home/v2john/Projects/financial-news-dataset/20061020_20131126_bloomberg_news/"
#
#/usr/bin/python3 "$CODEDIR"/stock_news_analyzer.py \
#--stock_news_path "$STOCK_FILE_PATH"
