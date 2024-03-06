#%%
from pydoc_data import topics
from altair import Cursor
from click import group
from sympy import limit, per
from wikirate4py import API
api = API('')
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
metric
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
api = API('')
company = api.get_company(7217) # returns company given company's numeric identifier
company.name
cursor = Cursor(api.get_metrics, wikirate_topic=["SDG5: Gender Equality"], metric_type="Researched", per_page=100) # returns metric given metric's numeric identifier
metrics = []
while cursor.has_next():
    metrics.extend(cursor.next())
metrics
# %%
answers =[]
for metric in metrics:
    answers.extend(api.get_answers(metric.id, company_id=7217, year=2021)) # returns answers given metric's numeric identifier
answers
# %%
