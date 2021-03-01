from job_posting import JobPostingCollectionSampleFile
from seek_au import SeekAusTransformer
from skill_extractor import SkillEndingPatternExtractor
import logging

logging.basicConfig(level=logging.INFO)

if __name__ == '__main__':
    # Use the simplest possible input:
    # 1. 50 pre-downloaded job postings
    job_postings = JobPostingCollectionSampleFile()

    # 2. A skill extractor to retrieve noun phrases ending in 'skill' or 'skills'.
    # VT job postings do not include line breaks, so the bulleted-line filter
    # will remove all possible matches. Let's turn it off
    pattern_extractor = SkillEndingPatternExtractor(only_bulleted_lines=False)

    skill_counts = Counter()
    for job_posting in job_postings:
        skill_counts += pattern_extractor.document_skill_counts(job_posting)

    logging.info('10 Most Common Skills in job descriptions:\n %s', pformat(skill_counts.most_common(10)))
    print('10 Most Common Skills in job descriptions:\n %s', pformat(skill_counts.most_common(10)))