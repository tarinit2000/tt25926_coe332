import json
with open("data.json", "r") as f:
    patients_dict = json.load(f)

#start = request.args.get('start')
#end = request.args.get('end')

start = 'Scan 1'
end = 'Scan 10'

keys = []
first = int(start[-2:]) # first scan number
last = int(end[-2:]) # last scan number
for x in range(first, last+1):
    key = 'Scan ' + str(x)
    keys.append(key) # range of keys (aka scans) the user wants to plot

output = {}
output['x'] = []
output['y'] = []

x_iter = range(0,72+8,8) # 10 scans every 8 weeks over 72 week period
count = 0
#patients_dict = get_data()
for i in keys:
    for x in patients_dict['patients']:
        if x[i] != None:
            output['y'].append(x[i])
            output['x'].append(x_iter[count])
    count = count + 1

print('X')
print(output['x'])
print('\n')
print('Y')
print(output['y'])

print(len(output['x']))
print(len(output['y']))
