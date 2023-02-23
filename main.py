import json
file = open('name.txt','w')
names = ['zhangsan', 'lisi', 'wangwu', 'jerry', 'henry', 'merry', 'chris']

result = json.dumps(names)

file.write(result)

file.close()
#000
