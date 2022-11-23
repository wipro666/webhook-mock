import re

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db_name = "flow_results"
db = client.get_database(db_name)
flow_collections = ["flow_3734761528_sample"]
metrics_regex = r'_metrics$'
non_metrics_collections  = [col for col in flow_collections if not (re.search(metrics_regex, col)) and (col.startswith("flow_"))]
for each in non_metrics_collections:
    reduced_name = "reduced_"+each
    if reduced_name in flow_collections:
        continue
    else:
        db.get_collection(each).aggregate([{ "$project": {
            "_id": 1,
            "flow.products.product.strategy": 1,
            "success": 1, "createdAt":1, "flow.products.product.action":1
        }},{"$out":reduced_name}])

# use slate_db
# db.deployment_collection_meta.createIndex({"collectionName":1})
