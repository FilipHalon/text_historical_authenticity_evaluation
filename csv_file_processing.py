import csv


def to_csv(dictionary, filename, total_count):
    with open(filename, 'w') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=['ngram', 'frequency'])
        writer.writeheader()
        for key in dictionary.keys():
            writer.writerow({'ngram': key, 'frequency': (dictionary[key]/total_count)*100})
            # writer.writerow({'ngram': key, 'frequency': dictionary[key]})
