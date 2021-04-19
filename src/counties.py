import pymysql
from flask import Blueprint, render_template, jsonify, request
from database import mysqlconnect

counties = Blueprint("counties", __name__)

@counties.route("/counties/", methods=["GET"])
@counties.route("/counties/<state_code>/", methods=["GET"])
def get_counties(state_code=None):
    output = None
    conn = mysqlconnect()
    codes = request.args.get("states")
    if (state_code):
        cur = conn.cursor()
        query = f"select * from Counties where state='{state_code}';"
        cur.execute(query)
        output = cur.fetchall()
    elif (codes):
        cur = conn.cursor()
        query = f"select * from Counties where state in ({codes});"
        cur.execute(query)
        output = cur.fetchall()
    else:
        cur = conn.cursor()
        query = f"select * from Counties;"
        cur.execute(query)
        output = cur.fetchall()
    conn.close()
    print(jsonify(output))
    return jsonify(output)


@counties.route("/counties/realty/", methods=["GET"])
@counties.route("/counties/realty/<state_code>/", methods=["GET"])
def get_county_realty(state_code=None):
    output = None
    conn = mysqlconnect()
    codes = request.args.get("states")
    if (state_code):
        cur = conn.cursor()
        query = \
            f"select id, name, state, price from Counties inner join \
            County_real_estate on id = cnty where state='{state_code}';"
        cur.execute(query)
        output = cur.fetchall()
    elif (codes):
        cur = conn.cursor()
        query = \
            f"select id, name, state, price from Counties inner join \
            County_real_estate on id = cnty where state in ({codes});"
        cur.execute(query)
        output = cur.fetchall()
    else:
        cur = conn.cursor()
        query = \
            f"select id, name, state, price from Counties inner join \
            County_real_estate on id = cnty;"
        cur.execute(query)
        output = cur.fetchall()
    conn.close()
    print(jsonify(output))
    return jsonify(output)


@counties.route("/counties/expectancy/", methods=["GET"])
@counties.route("/counties/expectancy/<state_code>/", methods=["GET"])
def get_county_expectancy(state_code=None):
    output = None
    conn = mysqlconnect()
    codes = request.args.get("states")
    if (state_code):
        cur = conn.cursor()
        query = \
            f"select id, name, state, age from Counties inner join \
            County_life_expec on id = cnty where state='{state_code}';"
        cur.execute(query)
        output = cur.fetchall()
    elif (codes):
        cur = conn.cursor()
        query = \
            f"select id, name, state, age from Counties inner join \
            County_life_expec on id = cnty where state in ({codes});"
        cur.execute(query)
        output = cur.fetchall()
    else:
        cur = conn.cursor()
        query = \
            f"select id, name, state, age from Counties inner join \
            County_life_expec on id = cnty;"
        query = \
            f"select id, name, state, price from Counties inner join \
            County_real_estate on id = cnty;"
        cur.execute(query)
        output = cur.fetchall()
    conn.close()
    print(jsonify(output))
    return jsonify(output)
