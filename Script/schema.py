import logging
import json
import os
import gzip

from typing import Dict, Text, Any, Generator
from io import BytesIO
from itertools import chain, islice
from jobPosting_Transformer import AUSJobPosting
from skills_ml.job_postings.raw.virginia import ViriginiaTransformer

JobPostingType = Dict[Text, Any]
JobPostingGeneratorType = Generator[JobPostingType, None, None]
MetadataType = Dict[Text, Dict[Text,Any]]


class JobPostingCollection(object):

    def __init__(self, num_records: int= 100, filePath: str="/Dataset/data.ldjson"):
        self.filePath = filePath
        if num_records > 200:
            logging.warning("'Cannot provide %s records as a maximum of 200 are available', num_records")
            num_records = 200
        #file_name = "/content/data.ldjson"
        f = open(self.filePath)
        self.lines = f.read().split("\n")
        self.transformer = AUSJobPosting(partner_id="VA")
    
    def __iter__(self) -> JobPostingGeneratorType:
        for line in self.lines:
            if line:
                yield self.transformer._transform(json.loads(line))
    
    @property
    def metadata(self) -> MetadataType:
        return {'job postings': {
            'downloaded_from': 'http://opendata.cs.vt.edu/dataset/openjobs-jobpostings',
            'month': '2016-07',
            'purpose': 'testing'
        }}


def retry_if_io_error(exception):
    return isinstance(exception, IOError)

    