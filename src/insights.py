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
    """Checks if a given salary is in the salary range of a given job

    Parameters
    ----------
    job : dict
        The job with `min_salary` and `max_salary` keys
    salary : int
        The salary to check if matches with salary range of the job

    Returns
    -------
    bool
        True if the salary is in the salary range of the job, False otherwise

    Raises
    ------
    ValueError
        If `job["min_salary"]` or `job["max_salary"]` doesn't exists
        If `job["min_salary"]` or `job["max_salary"]` aren't valid integers
        If `job["min_salary"]` is greather than `job["max_salary"]`
        If `salary` isn't a valid integer
    """
    pass


def filter_by_salary_range(jobs, salary):
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    return []


if __name__ == '__main__':
    print(get_unique_job_types("src/jobs.csv"))
    print(get_unique_industries("src/jobs.csv"))
    print(get_max_salary("src/jobs.csv"))
    print(get_min_salary("src/jobs.csv"))
    print(filter_by_job_type())
