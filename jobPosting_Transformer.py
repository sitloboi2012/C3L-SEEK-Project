from datetime import datetime
import logging
import tempfile


from skills_utils.io import stream_json_file
from skills_ultis.job_posting_import import JobPostingImportBase
from skills_utils.time import overlaps, quarter_to_daterange


def flatten(list_post):
    if type(list_post) is list:
        return(",".join(list_post))
    else:
        return list_post

class AUSJobPosting(JobPostingImportBase):
    """
    Transformed Job Posting from original to the correct format (schema)
    """
    date_format = '%Y-%b-%d'
    

    def __init__(self):
        super(AUSJobPosting, self)
        pass

    
    def id(self, document: dict or list):
        """
        Given a raw job posting and return its id unique id

        Args:
            document (dict or list): An instance contains job posting information

        """
        return document["uniq_id"]


    def transform(self, document: list or dict):
        """
        Transform a raw job posting into a specific schema

        Args:
            document (list or dict): contains information about job posting
        
        Returns:
            Return a transformed document that has been converted into a schema
        """

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
            transformed[target_key] = flatten(document.get(source_key))


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