import requests
import json
from pandas import json_normalize

tag_set = set()
data = requests.get("https://codeforces.com/api/problemset.problems").json()
problems = data["result"]["problems"]

df = json_normalize(problems)
print(df)

# getting the tags
# for problem in problems:
#     if "tags" in problem:
#         for tag in problem["tags"]:
#             if not tag in tag_set:
#                 tag_set.add(tag)

#for printing the tags
# with open("output.txt", "w") as out:
#     for tag in tag_set:
#         print(tag, file=out)