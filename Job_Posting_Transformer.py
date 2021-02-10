from datetime import datetime
import logging
import tempfile


from skills_utils.io import stream_json_file
from skills_ultis.job_posting_import import JobPostingImportBase
from skills_utils.time import overlaps, quarter_to_daterange


class AUSJobPosting(JobPostingImportBase):
    date_format = '%Y-%b-%d'
    

    def __init__(self):
        super(AUSJobPosting, self)
        pass


    def transform(self):
        transformed = {
            "@context": "http://schema.org",
            "@type": "JobPosting"
        }


        mapping = {
            "id": "uniq_id",
            "title": "job_title",
            "description": "job_description",
            "employment_type": "job_type",
            "occupation_category": "category",
        }


        for target_key, source_key in mapping:
            transformed[target_key] = document.get(source_key)


        if len(document["post_date"])  == 0 or len(document["postdate_yyyymmdd"]) == 0:
            transformed["post_date"] = None
        else:
            start = datetime.strptime(document["post_date"], self.date_format)
        

        location = document.get("state",[])
        if len(location) > 0:
            transformed["state"] = {
                "@type": "Place",
                "location": {
                    "@type": "PostalAddress",
                    "addressRegion": location[0].get("state","")
                }
            }


        transformed["company"] = {
            "@type": "Organization",
            "name": document.get("company_name")
        }
        

        try:
            transformed["salary"] = {
                "@type": "MonetaryAmount",
                "value": document["salary_offered"]
            }
        except:
            transformed["salary"] = {
                "@type": "MonetaryAmount",
                "value": document["inferred_salary_offered"]
            }
    
        return transformed