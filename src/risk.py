import pymysql
from flask import Blueprint, render_template, jsonify, request
from database import mysqlconnect

risk = Blueprint("risk", __name__)

@risk.route("/risk/", methods=["GET"])
@risk.route("/risk/<state_code>/", methods=["GET"])
def get_risk(state_code=None):
    output = None
    conn = mysqlconnect()
    level = request.args.get("level")
    codes = request.args.get("states")
    risk = request.args.get("risk")
    realty_range = request.args.get("range")
    realty_range = realty_range.split(",")
    map(lambda x: int(x), realty_range)

    cur = conn.cursor()

    if (codes):
        if (not level):
            risks = {}
            query_1 = \
                f"select * from State_real_estate where \
                price >= {realty_range[0]} && price <= {realty_range[1]} && state in ({codes})"
            query_2 = \
                f"select * from State_life_expec where state in \
                    (select state from State_real_estate where price >= {realty_range[0]} \
                    && price <= {realty_range[1]} && state in ({codes}))"
            query_3 = \
                f"select * from State_vaccinations where state in \
                    (select state from State_real_estate where price >= {realty_range[0]} \
                    && price <= {realty_range[1]} && state in ({codes}))"
            cur.execute(query_1)
            realty = cur.fetchall()

            cur.execute(query_2)
            age = cur.fetchall()

            cur.execute(query_3)
            vacc = cur.fetchall()

            merge = []
            for i in range(len(realty)):
                data = {}
                data.update(realty[i])
                data.update(age[i])
                data.update(vacc[i])
                merge.append(data)

            for state in merge:
                num = state["total_vaccinations_per_hundred"] * \
                    state["age"] * \
                    state["daily_vaccinations_per_million"]
                #dem = state["price"] * \
                dem = (state["people_vaccinated_per_hundred"] - \
                     state["people_fully_vaccinated_per_hundred"])
                state["risk"] = (dem / num) * 10000000
                risks[state["state"]] = state["risk"]

            return jsonify(merge)

        else:
            pass
    else:
        if (not level):
            print("\n\n\n\n\n here \n\n\n\n\n\n")
            risks = {}
            query_1 = \
                f"select * from State_real_estate where \
                price >= {realty_range[0]} && price <= {realty_range[1]}"
            query_2 = \
                f"select * from State_life_expec where state in \
                    (select state from State_real_estate where price >= {realty_range[0]} \
                    && price <= {realty_range[1]})"
            query_3 = \
                f"select * from State_vaccinations where state in \
                    (select state from State_real_estate where price >= {realty_range[0]} \
                    && price <= {realty_range[1]})"
            cur.execute(query_1)
            realty = cur.fetchall()

            cur.execute(query_2)
            age = cur.fetchall()

            cur.execute(query_3)
            vacc = cur.fetchall()

            merge = []
            for i in range(len(realty)):
                data = {}
                data.update(realty[i])
                data.update(age[i])
                data.update(vacc[i])
                merge.append(data)

            for state in merge:
                num = state["total_vaccinations_per_hundred"] * \
                    state["age"] * \
                    state["daily_vaccinations_per_million"]
                #dem = state["price"] * \
                dem = (state["people_vaccinated_per_hundred"] - \
                     state["people_fully_vaccinated_per_hundred"])
                state["risk"] = (dem / num) * 10000000
                risks[state["state"]] = state["risk"]

            return jsonify(merge)

        else:
            pass

    conn.close()
    return jsonify(output)
