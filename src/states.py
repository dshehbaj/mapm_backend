import pymysql
from flask import Blueprint, render_template, jsonify, request
from database import mysqlconnect

states = Blueprint("states", __name__)

@states.route("/states/", methods=["GET"])
def get_all_states():
    output = None
    conn = mysqlconnect()
    cur = conn.cursor()
    cur.execute("select * from States")
    output = cur.fetchall()
    conn.close()
    return jsonify(output)

@states.route("/states/realty/", methods=["GET"])
@states.route("/states/realty/<state_code>/", methods=["GET"])
def get_state_realty(state_code=None):
    output = None
    conn = mysqlconnect()
    codes = request.args.get("states")
    if (state_code):
        cur = conn.cursor()
        query = f"select * from State_real_estate where state='{state_code}';"
        cur.execute(query)
        output = cur.fetchall()
    elif (codes):
        cur = conn.cursor()
        query = f"select * from State_real_estate where state in ({codes});"
        cur.execute(query)
        output = cur.fetchall()
    else:
        cur = conn.cursor()
        query = f"select * from State_real_estate;"
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
    if (state_code):
        cur = conn.cursor()
        query = f"select * from State_life_expec where state='{state_code}';"
        cur.execute(query)
        output = cur.fetchall()
    elif (codes):
        cur = conn.cursor()
        query = f"select * from State_life_expec where state in ({codes});"
        cur.execute(query)
        output = cur.fetchall()
    else:
        cur = conn.cursor()
        query = f"select * from State_life_expec;"
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
