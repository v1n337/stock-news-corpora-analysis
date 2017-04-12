from processors.processor import Processor
from utils import log_helper

log = log_helper.get_logger(__name__)


class NewsAnalysisProcessor(Processor):

    def process(self):
        log.info("NewsAnalysisProcessor begun")

        log.info("NewsAnalysisProcessor completed")
