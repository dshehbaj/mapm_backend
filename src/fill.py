import csv

def func_1():
    fields = []
    rows = []
    state_file = csv.reader(open("../data/states.csv", "r"))
    fields = next(state_file)
    for row in state_file:
        rows.append(row)
    #print(fields)
    #print(rows)

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
    fields = []
    rows = []
    state_file = csv.reader(open("../data/counties.csv", "r"))
    fields = next(state_file)
    for row in state_file:
        rows.append(row)
    #print(fields)
    #print(rows)

    query = "insert into Counties (id, name, state) values "
    values = ""
    for row in rows:
        values += f'("{row[0]}", "{row[1]}", "{row[2]}"),'
    query += values
    query = query[:len(query) - 1] + ";"
    with open("../sql/counties_fill.sql", "w") as ofile:
        ofile.write("use mapm;")
        ofile.write(query)

def func_3():
    fields = []
    rows = []
    state_file = csv.reader(open("../data/real_estate/county_prices.csv", "r"))
    fields = next(state_file)
    for row in state_file:
        rows.append(row)
    #print(fields)
    #print(rows)

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
    fields = []
    rows = []
    state_file = csv.reader(open("../data/real_estate/state_prices.csv", "r"))
    fields = next(state_file)
    for row in state_file:
        rows.append(row)
    #print(fields)
    #print(rows)

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
    fields = []
    rows = []
    state_file = csv.reader(open("../data/life_expectancy/county_life_expectancy.csv", "r"))
    fields = next(state_file)
    for row in state_file:
        rows.append(row)
    #print(fields)
    #print(rows)

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
    fields = []
    rows = []
    state_file = csv.reader(open("../data/life_expectancy/states_life_expectancy.csv", "r"))
    fields = next(state_file)
    for row in state_file:
        rows.append(row)
    #print(fields)
    #print(rows)

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
    fields = []
    rows = []
    state_file = csv.reader(open("../data/covid/vaccinations.csv", "r"))
    fields = next(state_file)
    for row in state_file:
        rows.append(row)
    #print(fields)
    #print(rows)

    query = "insert into State_vaccinations \
        (state, total_vaccinations, total_distributed, people_vaccinated, \
        people_fully_vaccinated, daily_vaccinations) values "
    values = ""
    for row in rows:
        values += \
            f'("{row[0]}", "{row[3]}", "{row[4]}", \
            "{row[5]}", "{row[8]}", "{row[12]}"),'
    query += values
    query = query[:len(query) - 1] + ";"
    with open("../sql/state_covid_vacc.sql", "w") as ofile:
        ofile.write("use mapm;")
        ofile.write(query)

func_1()
func_2()
func_3()
func_4()
func_5()
func_6()
func_7()
