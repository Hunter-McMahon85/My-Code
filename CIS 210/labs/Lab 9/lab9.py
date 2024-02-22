# DO not code in here
# code in your workspace
import re

#  Style 1
# res_list=[]
# with open('w22.txt','r') as file:
#     for line in file:
#         res=re.findall(r'some pattern',line)
#         res_list.extend(res)

# Style 2 (recommended in this case)
with open('w22.txt', 'r') as file:
    text = file.read()
# 1A solution
res_list = re.findall(r'CIS \d{3}[A-z]?', text, flags=re.MULTILINE)
print(res_list)

# 1B solution
res_listB = re.flags = re.MULTILINE
dict_1b = dict(res_listB)[re.findall(r'(CIS \d{3}[A-z]?)\s+(.*)\t.*', text)]

# 1E solution
res_listE = re.findall(r'[\d B]{0,2}\d\d [A-Z]{3,4}', text, flags=re.MULTILINE)
print(res_listE)
