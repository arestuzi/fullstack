#!/usr/bin/env python
# Author: Binglin Ji

username = input("username: ")
password = input("password: ")
age = input("age: ")
job = input("job: ")
salary = input("salary: ")

info = '''
--------- info of %s ---------
Name: %s
Age: %s
Job: %s
Salary: %s
''' % (username, age, password, job, salary)

print(info)

info2 = '''
--------- info of {_name} ---------
Name: {_name}
Age: {_age}
Job: {_job}
Salary: {_salary}
'''.format(_name=username,
           _age=age,
           _job=job,
           _salary=salary)

print(info2)

info3 = '''
--------- info of {0} ---------
Name: {0}
Age: {1}
Job: {2}
Salary: {3}
'''.format(username,age,job,salary)
print(info3)