import logging

from processors.processor import Processor

log = logging.getLogger(__name__)


class NewsAnalysisProcessor(Processor):

    def process(self):
        log.info("NewsAnalysisProcessor begun")

        log.info("NewsAnalysisProcessor completed")
