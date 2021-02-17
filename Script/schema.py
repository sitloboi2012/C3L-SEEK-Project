"""A variety of common-schema job posting collections.

Each class in this module should implement a generator that yields job postings (in the common schema, as a JSON string), and has a 'metadata' attribute so any users of the job postings can inspect meaningful metadata about the postings.
"""
import logging
from retrying import Retrying
from io import BytesIO
from itertools import chain, islice

from skills_utils.s3 import split_s3_path
from skills_utils.s3 import log_download_progress
from skills_ml.job_postings.raw.virginia import VirginiaTransformer
from Script.jobPosting_Transformer import SeekAusTransformer

import json
import os
import gzip

from typing import Dict, Text, Any, Generator

JobPostingType = Dict[Text, Any]
JobPostingGeneratorType = Generator[JobPostingType, None, None]
MetadataType = Dict[Text, Dict[Text, Any]]


class JobPostingCollectionSampleFile(object):
    """Stream a finite number of job postings stored within the library.

    Example:
    ```
    import json

    job_postings = JobPostingCollectionSample()
    for job_posting in job_postings:
        print(json.loads(job_posting)['title'])

    Meant to provide a dependency-less example of common schema job postings
    for introduction to the library

    Args:
        num_records (int): The maximum number of records to return. Defaults to 50 (all postings available)
    """
    def __init__(self, num_records:int=50):
        if num_records > 50:
            logging.warning('Cannot provide %s records as a maximum of 50 are available', num_records)
            num_records = 50
        full_filename = 'data.ldjson'
        print(full_filename)
        f = open(full_filename)
        self.lines = f.read().split('\n')
        self.transformer = SeekAusTransformer(partner_id='VA')

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