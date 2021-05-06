import csv, json, uuid

def csvtojson():
    data = {}
    data['patients'] = []
    with open('glio_data_proj.csv', 'r') as csvfile:
        csvreader = csv.DictReader(csvfile)
        for rows in csvreader: 
            data['patients'].append(rows)

        for p in data['patients']: 
            p['id'] = str(uuid.uuid4())
            if p['Scan 1'] == '0':
                p['Scan 1'] = None
            if p['Scan 2'] == '0':
                p['Scan 2'] = None
            if p['Scan 3'] == '0':
                p['Scan 3'] = None
            if p['Scan 4'] == '0':
                p['Scan 4'] = None
            if p['Scan 5'] == '0':
                p['Scan 5'] = None
            if p['Scan 6'] == '0':
                p['Scan 6'] = None
            if p['Scan 7'] == '0':
                p['Scan 7'] = None
            if p['Scan 8'] == '0':
                p['Scan 8'] = None
            if p['Scan 9'] == '0':
                p['Scan 9'] = None
            if p['Scan 10'] == '0':
                p['Scan 10'] = None


    with open('data.json', 'w') as jsonfile:
        jsonfile.write(json.dumps(data, indent=2))


#if __name__ == '__main__':
#    main()
