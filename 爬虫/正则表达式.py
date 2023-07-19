import re

str = 'aabaabababbba'
k = re.compile('aa.*b.a(.*)a')
arr = re.findall(k, str)
print(arr)