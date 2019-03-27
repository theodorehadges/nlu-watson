from __future__ import print_function
import json
from watson_developer_cloud import NaturalLanguageUnderstandingV1
from watson_developer_cloud.natural_language_understanding_v1 import Features, EntitiesOptions, KeywordsOptions

# authenticate 
service = NaturalLanguageUnderstandingV1(version='2018-03-16',url='https://gateway-wdc.watsonplatform.net/natural-language-understanding/api', iam_apikey='RkGLclK8A--N0Lhyl9Kmq_dsqxb7v5er-c-u55wDJ6jM')

orwell_book = open("shooting_an_elephant_george_orwell",'r')
response = service.analyze(
    text=orwell_book.read(),
    features=Features(entities=EntitiesOptions(),
        keywords=KeywordsOptions())).get_result()


print(json.dumps(response, indent=2))
