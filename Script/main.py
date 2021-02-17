try:
    from pip import main as pipmain
except:
    from pip._internal import main as pipmain

pipmain(["install","skills-ml"])
pipmain(["uninstall","pandas"])
pipmain(["install","pandas"])
pipmain(["install","boto"])
pipmain(["install","nltk"])
pipmain(["install","matplotlib"])



import numpy as np
import pandas as pd
import nltk
import matplotlib.pyplot as plt
import spacy
import nltk
import skills_ml
import sklearn
import logging
import re

from collections import Counter
from pprint import pformat
from Script.schema import JobPostingCollectionSampleFile
from sklearn.metrics.pairwise import cosine_similarity, euclidean_distances
from gensim.models.doc2vec import Doc2Vec, TaggedDocument
from Script.jobPosting_Transformer import SeekAusTransformer
from skills_ml.algorithms.skill_extractors import ExactMatchSkillExtractor
from skills_ml.algorithms.skill_extractors.noun_phrase_ending import AbilityEndingPatternExtractor, SkillEndingPatternExtractor
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity, euclidean_distances
from sklearn.cluster import KMeans
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import punkt, word_tokenize


