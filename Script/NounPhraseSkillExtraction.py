from collections import Counter
import logging
from pprint import pformat
from schema import JobPostingCollection
from skills_ml.algorithms.skill_extractors.noun_phrase_ending import SkillEndingPatternExtractor, AbilityEndingPatternExtractor

logging.basicConfig(level=logging.INFO)

if __name__ == "main":
    job_postings = JobPostingCollection()

    pattern_extractor = SkillEndingPatternExtractor(only_bulleted_lines=False)

    skill_counts = Counter()
    for job_posting in job_postings:
        skill_counts += pattern_extractor.document_skill_counts(job_postinng)

    logging.info("50 Most Common Skills in Job Description:\n {}".format(pformat(skill_counts.most_common(50))))
    