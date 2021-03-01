from skills_utils.io import stream_json_file
from skills_utils.job_posting_import import JobPostingImportBase
from skills_utils.time import overlaps, quarter_to_daterange
from typing import Dict, Text, Any, Generator
from typing import List, Set, Generator, Dict, Pattern, Tuple
from seek_au import SeekAusTransformer
import json

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
        #full_filename = os.path.join(os.path.dirname(__file__), '/seek_au-jobs_listing__20190901_20191231_sample.ldjson')
        #f = gzip.GzipFile(filename=full_filename)
        full_filename = '/workspace/C3L-SEEK-Project/Script/data_2.ldjson'
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


def retry_if_io_error(exception):
    return isinstance(exception, IOError)