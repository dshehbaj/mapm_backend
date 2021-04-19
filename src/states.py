import pymysql
from flask import Blueprint, render_template, jsonify, request
from flask_cors import CORS
from database import mysqlconnect

states = Blueprint("states", __name__)
CORS(states)

@states.route("/states/", methods=["GET"])
@states.route("/states/<state_code>/", methods=["GET"])
def get_states(state_code=None):
    output = None
    conn = mysqlconnect()
    codes = request.args.get("states")
    if (state_code):
        cur = conn.cursor()
        query = f"select * from States where code='{state_code}';"
        cur.execute(query)
        output = cur.fetchall()
    elif (codes):
        cur = conn.cursor()
        query = f"select * from States where code in ({codes});"
        cur.execute(query)
        output = cur.fetchall()
    else:
        cur = conn.cursor()
        query = f"select * from States;"
        cur.execute(query)
        output = cur.fetchall()
    conn.close()
    print(jsonify(output))
    return jsonify(output)


@states.route("/states/realty/", methods=["GET"])
@states.route("/states/realty/<state_code>/", methods=["GET"])
def get_state_realty(state_code=None):
    output = None
    range_qry = ""
    conn = mysqlconnect()
    codes = request.args.get("states")
    num_range = request.args.get("range")
    if (num_range):
        num_range = num_range.split(",")
        map(lambda x: int(x), num_range)
        range_qry = f"price >= {num_range[0]} && price <= {num_range[1]}"
    if (state_code):
        cur = conn.cursor()
        query = f"select * from State_real_estate where state='{state_code}'"
        if (num_range):
            query += (" && " + range_qry)
        query += ";"
        cur.execute(query)
        output = cur.fetchall()
    elif (codes):
        cur = conn.cursor()
        query = f"select * from State_real_estate where state in ({codes})"
        if (num_range):
            query += (" && " + range_qry)
        query += ";"
        cur.execute(query)
        output = cur.fetchall()
    else:
        cur = conn.cursor()
        query = f"select * from State_real_estate"
        if (num_range):
            query += (" where " + range_qry)
        query += ";"
        cur.execute(query)
        output = cur.fetchall()
    conn.close()
    print(jsonify(output))
    return jsonify(output)


@states.route("/states/expectancy/", methods=["GET"])
@states.route("/states/expectancy/<state_code>/", methods=["GET"])
def get_expectancy(state_code=None):
    output = None
    conn = mysqlconnect()
    codes = request.args.get("states")
    num_range = request.args.get("range")
    if (num_range):
        num_range = num_range.split(",")
        map(lambda x: int(x), num_range)
        range_qry = f"age >= {num_range[0]} && age <= {num_range[1]}"
    if (state_code):
        cur = conn.cursor()
        query = f"select * from State_life_expec where state='{state_code}'"
        if (num_range):
            query += (" && " + range_qry)
        query += ";"
        cur.execute(query)
        output = cur.fetchall()
    elif (codes):
        cur = conn.cursor()
        query = f"select * from State_life_expec where state in ({codes})"
        if (num_range):
            query += (" && " + range_qry)
        query += ";"
        cur.execute(query)
        output = cur.fetchall()
    else:
        cur = conn.cursor()
        query = f"select * from State_life_expec"
        if (num_range):
            query += (" where " + range_qry)
        query += ";"
        cur.execute(query)
        output = cur.fetchall()
    conn.close()
    print(jsonify(output))
    return jsonify(output)


@states.route("/states/vaccinations/", methods=["GET"])
@states.route("/states/vaccinations/<state_code>/", methods=["GET"])
def get_vaccinations(state_code=None):
    output = None
    conn = mysqlconnect()
    codes = request.args.get("states")
    if (state_code):
        cur = conn.cursor()
        query = f"select * from State_vaccinations where state='{state_code}';"
        cur.execute(query)
        output = cur.fetchall()
    elif (codes):
        cur = conn.cursor()
        query = f"select * from State_vaccinations where state in ({codes});"
        cur.execute(query)
        output = cur.fetchall()
    else:
        cur = conn.cursor()
        query = f"select * from State_vaccinations;"
        cur.execute(query)
        output = cur.fetchall()
    conn.close()
    print(jsonify(output))
    return jsonify(output)
