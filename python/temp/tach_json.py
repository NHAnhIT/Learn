import json

with open('tree.json', 'r', encoding='utf-8') as file:
    tree_report = file.read()
tree_report_dict = json.loads(tree_report)
print(tree_report_dict[0]['children'][0]['children'][7]['attr']['name'])