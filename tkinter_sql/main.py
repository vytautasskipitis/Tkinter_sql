import sqlite3
from employee_class import Employee
from pagrindines_funkcijos import *

conn = sqlite3.connect(':memory:')
# conn = sqlite3.connect('duomenu_baze.db')

c = conn.cursor()

c.execute("""CREATE TABLE employees (
            first text,
            last text,
            pay integer
            )""")

# demo darbuotojai
emp_1 = [
    Employee('Vytas', 'Skip', 1000),
    Employee('Tomas', 'Stan', 5500),
    Employee('Robert', 'Stepo', 2200),
    Employee('Luna', 'Kame', 800)
]
emp_2 = [
    insert_emp(x)
    for x in emp_1
]

from lenteles_funkcijos import *

conn.close()
