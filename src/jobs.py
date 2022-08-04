import csv
from functools import lru_cache


@lru_cache
def read(path):
    dict_jobs = []
    with open(path) as file:
        jobs_data = csv.DictReader(file)
        for job in jobs_data:
            dict_jobs.append(dict(job))
    return dict_jobs

# sobre o DictReader = https://linuxhint.com/use-python-csv-dictreader/


if __name__ == '__main__':
    print(read("src/jobs.csv"))
