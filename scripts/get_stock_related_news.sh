#!/usr/bin/env bash

CODEDIR=$(dirname "$0")"/../"

# Reuters Dataset
STOCK_FILE_PATH="/home/v2john/Projects/financial-news-dataset-alt/ReutersNews106521/"
OUTPUT_FILE_PATH="/home/v2john/reuters_news.txt"

python3 "$CODEDIR"/stock_news_extractor.py \
--stock_news_path "$STOCK_FILE_PATH" \
--output_file "$OUTPUT_FILE_PATH" \
--news_source reuters

# Bloomberg Dataset
#STOCK_FILE_PATH="/home/v2john/Projects/financial-news-dataset/20061020_20131126_bloomberg_news/"
#OUTPUT_FILE_PATH="/home/v2john/bloomberg_news.txt"
#
#python3 "$CODEDIR"/stock_news_extractor.py \
#--stock_news_path "$STOCK_FILE_PATH" \
#--output_file "$OUTPUT_FILE_PATH" \
#--news_source bloomberg
