"""
Python script for generating .sql files from cleaned .csv files
"""

import csv
from database import mysqlconnect

def func_1():
    rows = []
    state_file = csv.reader(open("../data/states.csv", "r"))
    fields = next(state_file)
    for row in state_file:
        rows.append(row)

    query = "insert into States (code, name) values "
    values = ""
    for row in rows:
        values += f'("{row[0]}", "{row[1]}"),'
    query += values
    query = query[:len(query) - 1] + ";"
    with open("../sql/states_fill.sql", "w") as ofile:
        ofile.write("use mapm;")
        ofile.write(query)

def func_2():
    rows = []
    state_file = csv.reader(open("../data/counties.csv", "r"))
    fields = next(state_file)
    for row in state_file:
        rows.append(row)

    query = "insert into Counties (id, name, state, lat, lng) values "
    values = ""
    for row in rows:
        values += f'("{row[0]}", "{row[1]}", "{row[2]}", "{row[3]}", "{row[4]}"),'
    query += values
    query = query[:len(query) - 1] + ";"
    with open("../sql/counties_fill.sql", "w") as ofile:
        ofile.write("use mapm;")
        ofile.write(query)

def func_3():
    rows = []
    state_file = csv.reader(open("../data/real_estate/county_prices.csv", "r"))
    fields = next(state_file)
    for row in state_file:
        rows.append(row)

    query = "insert into County_real_estate (cnty, price) values "
    values = ""
    for row in rows:
        values += f'("{row[0]}", "{row[2]}"),'
    query += values
    query = query[:len(query) - 1] + ";"
    with open("../sql/counties_realty_fill.sql", "w") as ofile:
        ofile.write("use mapm;")
        ofile.write(query)

def func_4():
    rows = []
    state_file = csv.reader(open("../data/real_estate/state_prices.csv", "r"))
    fields = next(state_file)
    for row in state_file:
        rows.append(row)

    query = "insert into State_real_estate (state, price) values "
    values = ""
    for row in rows:
        values += f'("{row[0]}", "{row[1]}"),'
    query += values
    query = query[:len(query) - 1] + ";"
    with open("../sql/state_realty_fill.sql", "w") as ofile:
        ofile.write("use mapm;")
        ofile.write(query)

def func_5():
    rows = []
    state_file = csv.reader(
        open("../data/life_expectancy/county_life_expectancy.csv", "r"))
    fields = next(state_file)
    for row in state_file:
        rows.append(row)

    query = "insert into County_life_expec (cnty, age) values "
    values = ""
    for row in rows:
        values += f'("{row[0]}", "{row[3]}"),'
    query += values
    query = query[:len(query) - 1] + ";"
    with open("../sql/county_life_expec.sql", "w") as ofile:
        ofile.write("use mapm;")
        ofile.write(query)

def func_6():
    rows = []
    state_file = csv.reader(
        open("../data/life_expectancy/states_life_expectancy.csv", "r"))
    fields = next(state_file)
    for row in state_file:
        rows.append(row)

    query = "insert into State_life_expec (state, age) values "
    values = ""
    for row in rows:
        values += f'("{row[0]}", "{row[1]}"),'
    query += values
    query = query[:len(query) - 1] + ";"
    with open("../sql/state_life_expec.sql", "w") as ofile:
        ofile.write("use mapm;")
        ofile.write(query)

def func_7():
    rows = []
    state_file = csv.reader(open("../data/covid/vaccinations.csv", "r"))
    fields = next(state_file)
    for row in state_file:
        rows.append(row)

    query = "insert into State_vaccinations \
        (state, total_vaccinations, total_distributed, people_vaccinated, \
        people_fully_vaccinated_per_hundred, total_vaccinations_per_hundred, \
        people_fully_vaccinated, people_vaccinated_per_hundred, \
        distributed_per_hundred, daily_vaccinations_raw, \
        daily_vaccinations, daily_vaccinations_per_million, \
        share_doses_used) values "

    values = ""
    for row in rows:
        values += \
            f'("{row[0]}", "{row[3]}", "{row[4]}", \
            "{row[5]}", "{row[6]}", "{row[7]}", \
            "{row[8]}", "{row[9]}", "{row[10]}", \
            "{row[11]}", "{row[12]}", "{row[13]}", \
            "{row[14]}"),'
    query += values
    query = query[:len(query) - 1] + ";"
    with open("../sql/state_covid_vacc.sql", "w") as ofile:
        ofile.write("use mapm;")
        ofile.write(query)

if __name__ == "__main__":
    func_1()
    func_2()
    func_3()
    func_4()
    func_5()
    func_6()
    func_7()
