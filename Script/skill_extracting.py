from job_posting import JobPostingCollectionSampleFile
from seek_au import SeekAusTransformer
from skill_extractor import SkillEndingPatternExtractor
import logging

logging.basicConfig(level=logging.INFO)

if __name__ == '__main__':
    skill = []
    context = []
    job_postings = JobPostingCollectionSampleFile() #CHANGE THIS ONE TO THE FILENAME THAT IS USE (MUST BE LDJSON)
    skill_extractor = SkillEndingPatternExtractor(only_bulleted_lines=False)

      

    for job_posting in job_postings:
      #print(job_posting)
      skill_per_doc = []
      text_per_doc = []
      text = skill_extractor.candidate_skills(job_posting)
      for i in text:
        skill.append(i.skill_name)
        context.append(i.context)

logging.info(skill)