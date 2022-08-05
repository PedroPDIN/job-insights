from src.jobs import read


def get_unique_job_types(path):
    all_info_jobs = read(path)
    all_jobs_tasks = set()

    for job in all_info_jobs:
        all_jobs_tasks.add(job["job_type"])

    return all_jobs_tasks


def filter_by_job_type(jobs, job_type):
    all_jobs_types = []
    for job in jobs:
        if job["job_type"] == job_type:
            all_jobs_types.append(job)
    return all_jobs_types


def get_unique_industries(path):
    all_info_jobs = read(path)
    all_industries = set()

    for job in all_info_jobs:
        if job["industry"] != '':
            all_industries.add(job["industry"])
    return all_industries


def filter_by_industry(jobs, industry):
    all_jobs_industry = []
    for job in jobs:
        if job["industry"] == industry:
            all_jobs_industry.append(job)
    return all_jobs_industry


def get_max_salary(path):
    all_info_jobs = read(path)
    all_salary_string = []
    higher_salary = 0

    for job in all_info_jobs:
        if job["max_salary"] != '' and job["max_salary"].isdigit():
            all_salary_string.append(job["max_salary"])

    all_salary_number = list(map(int, all_salary_string))

    for salary in all_salary_number:
        if salary > higher_salary:
            higher_salary = salary

    return higher_salary


def get_min_salary(path):
    all_info_jobs = read(path)
    all_salary_string = []
    higher_salary = 0

    for job in all_info_jobs:
        if job["min_salary"] != '' and job["min_salary"].isdigit():
            all_salary_string.append(job["min_salary"])

    all_salary_number = list(map(int, all_salary_string))
    higher_salary = all_salary_number[0]

    for salary in all_salary_number:
        if salary < higher_salary:
            higher_salary = salary

    return higher_salary


def matches_salary_range(job, salary):
    if job.get("min_salary") is None or job.get("max_salary") is None:
        raise ValueError("Values does not exist")
    elif type(job["min_salary"]) != int or type(job["max_salary"]) != int:
        raise ValueError("Von-numeric values")
    elif job["min_salary"] > job["max_salary"]:
        raise ValueError("Minimum wage higher than maximum wage")
    elif type(salary) != int:
        raise ValueError("Value is not numeric")
    else:
        return average_wage(job, salary)


def average_wage(salary_average, salary):
    if salary_average["min_salary"] <= salary <= salary_average["max_salary"]:
        return True
    else:
        return False


def filter_by_salary_range(jobs, salary):
    filter_salary = []
    for job in jobs:
        try:
            value_filter_salary = matches_salary_range(job, salary)
            if value_filter_salary is True:
                filter_salary.append(job)
        except ValueError:
            pass
    return filter_salary


if __name__ == '__main__':
    jobs = [
        {"max_salary": 0, "min_salary": 10},
        {"max_salary": 10, "min_salary": 100},
        {"max_salary": 10000, "min_salary": 200},
        {"max_salary": 15000, "min_salary": 0},
        {"max_salary": 1500, "min_salary": 0},
        {"max_salary": -1, "min_salary": 10},
    ]

    print(get_unique_job_types("src/jobs.csv"))
    print(get_unique_industries("src/jobs.csv"))
    print(get_max_salary("src/jobs.csv"))
    print(get_min_salary("src/jobs.csv"))
    print(filter_by_salary_range(jobs, 10000))
