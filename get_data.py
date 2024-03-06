#%%
#%%
from pydoc_data import topics
from altair import Cursor
from click import group
from sympy import limit, per
from wikirate4py import API
api = API('jkcH51HWiSWnz5BGHTszrwtt')
company = api.get_company(7217) # returns company given company's numeric identifier
company.name
#%%
!pip install git+https://github.com/wikirate/wikirate4py.git
# %%
company
# %%
group = api.get_company_groups
group
# %%
dataset = api.get_dataset(1) # returns dataset given dataset's numeric identifier
# %%
dataset
# %%
metrics = api.get_metrics(topics) # returns metrics given dataset's numeric identifier
metrics
# %%
metrics.save('metrics.csv')
# %%
cursor = Cursor(api.get_metrics)
api.get_metrics(wikirate_topic=["SDG5: Gender Equality"], limit=100) # returns metric given metric's numeric identifier
# %%
for metric in metrics:
    metric_id = api.get_answers(metric.id) # returns answers given metric's numeric identifier
    metric_id

# %%
metric
# %%
for metric in metrics:
    metric_id = api.get_answers(metric.id, company_id=7217) # returns answers given metric's numeric identifier
metric_id
# %%
metric_id
# %%
for metric in metrics:
    metric_id = api.get_answers(metric.id, company_id=7217, year=2021) # returns answers given metric's numeric identifier
metric_id
# %%
metric_id
# %%
from wikirate4py import Cursor
from wikirate4py import API
api = API('jkcH51HWiSWnz5BGHTszrwtt')
company = api.get_company(7217) # returns company given company's numeric identifier
company.name
cursor = Cursor(api.get_metrics, wikirate_topic=["SDG5: Gender Equality"], metric_type="Researched", per_page=100) # returns metric given metric's numeric identifier
metrics = []
while cursor.has_next():
    metrics.extend(cursor.next())
    answers =[]
    for metric in metrics:
        answers.extend(api.get_answers(metric.id, company_id=7217))
# %%
answers.json()
# %%
def metric_item_to_dicts(item):
    return {
        'id': item.id,  # Example attribute
        'metric': item.metric,
        "year": item.year,
    }
for answer in answers:
    print(metric_item_to_dicts(answer))
    with open('answers.json', 'w') as f:
        json.dump(answers, f)
# %%
!pip install bson
# %%
import json
json_docs = []
for metric in metrics:
    json_docs.append(metric)
    with open('metrics.json', 'w') as f:
        json.dump(json_docs, f)

# %%
answers =[]
for metric in metrics:
    answers.extend(api.get_answers(metric.id, company_id=7217)) # returns answers given metric's numeric identifier
answers
# %%
import json

# Assuming api.get_company() and Cursor() are defined elsewhere and work as intended.

# Function to convert MetricItem to a dictionary
# You need to adjust the attributes accessed below according to the actual structure of MetricItem
def metric_item_to_dict(item):
    return {
        'id': item.id,  # Example attribute
        'name': item.name,
    }

company = api.get_company(7217)
print(company.name)

cursor = Cursor(api.get_metrics, wikirate_topic=["SDG5: Gender Equality"], metric_type="Researched", per_page=100)
metrics = []

while cursor.has_next():
    metric_items = cursor.next()
    for item in metric_items:
        metrics.append(metric_item_to_dict(item))  # Convert each MetricItem to a dict before appending

# Now that all MetricItems are converted to dictionaries, we can safely serialize
with open('metrics1.json', 'w') as f:
    json.dump(metrics, f)

# %%
while cursor.has_next():
    metric_items = cursor.next()
    for item in metric_items:
        metrics.append(metric_item_to_dict(item))
# %%
def metric_item_to_dict(item):
    return {
        'id': item.id,  # Example attribute
        'name': item.name,
    }

company = api.get_company(7217)
print(company.name)

cursor = Cursor(api.get_metrics, wikirate_topic=["SDG5: Gender Equality"], metric_type="Researched", per_page=100)
metrics = []

while cursor.has_next():
    metric_items = cursor.next()
    for item in metric_items:
        metrics.append(metric_item_to_dict(item))
        answers =[]
        answers.extend(api.get_answers(entity="Adidas_AG")) # returns answers given metric's numeric identifier

# Now that all MetricItems are converted to dictionaries, we can safely serialize
with open('metrics1.json', 'w') as f:
    json.dump(metrics, f)
# %%
