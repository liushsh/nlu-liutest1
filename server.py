# coding: utf-8

# In[4]:

import sys
import os
import json
sys.path.append(os.path.join(os.getcwd(),'..'))
import watson_developer_cloud
import watson_developer_cloud.natural_language_understanding.features.v1 as \
    features


# In[3]:

nlu = watson_developer_cloud.NaturalLanguageUnderstandingV1(
    version='2017-02-27',
    username='ddc3ed94-6032-417b-ac2e-ab7faa8ee11f',
    password='4ct36lkd1p4Z')


# In[6]:

response = nlu.analyze(
    text='Bruce Banner is the Hulk and Bruce Wayne is BATMAN! '
         'Superman fears not Banner, but Wayne.',
    features=[features.Entities(), features.Keywords()])

print(json.dumps(response, indent=2))

# In[ ]:

