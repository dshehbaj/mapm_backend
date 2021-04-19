import pymysql
from flask import Blueprint, render_template, jsonify, request
from flask_cors import CORS
from database import mysqlconnect

risk = Blueprint("risk", __name__)
CORS(risk)

@risk.route("/risk/", methods=["GET"])
@risk.route("/risk/<state_code>/", methods=["GET"])
def get_risk(state_code=None):
    conn = mysqlconnect()
    level = request.args.get("level")
    codes = request.args.get("states")
    #risk = request.args.get("risk")
    realty_range = request.args.get("range")
    realty_range = realty_range.split(",")
    map(lambda x: int(x), realty_range)

    cur = conn.cursor()

    if (codes):
        if (not level):
            risks = {}
            query_1 = \
                f"select * from State_real_estate where \
                price >= {realty_range[0]} && price <= \
                {realty_range[1]} && state in ({codes})"
            query_2 = \
                f"select * from State_life_expec where state in \
                    (select state from State_real_estate \
                    where price >= {realty_range[0]} \
                    && price <= {realty_range[1]} && state in ({codes}))"
            query_3 = \
                f"select * from State_vaccinations where state in \
                    (select state from State_real_estate \
                    where price >= {realty_range[0]} \
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

            conn.close()
            return jsonify(merge)

        else:
            merge = []
            risks = {}
            covid_score_state = {}
            query_1 = \
                f"select id, name, state, price, age from Counties inner join \
                County_life_expec on Counties.id = County_life_expec.cnty \
                inner join County_real_estate on \
                County_life_expec.cnty = County_real_estate.cnty \
                where state in ({codes}) && \
                price >= {realty_range[0]} && price <= {realty_range[1]}"
            query_2 = \
                f"select * from State_vaccinations where state in \
                (select state from Counties inner join \
                County_real_estate on id = cnty where state in ({codes}) \
                && price >= {realty_range[0]} && price <= {realty_range[1]})"


            cur.execute(query_1)
            data = cur.fetchall()

            cur.execute(query_2)
            state_covid = cur.fetchall()

            for state in state_covid:
                num = state["total_vaccinations_per_hundred"] * \
                    state["daily_vaccinations_per_million"]
                dem = (state["people_vaccinated_per_hundred"] - \
                     state["people_fully_vaccinated_per_hundred"])
                covid_score_state[state["state"]] = dem / num

            for cnty in data:
                cnty["risk"] = (covid_score_state[cnty["state"]] / cnty["age"]) * 10000000

            conn.close()
            return jsonify(data)

    else:
        if (not level):
            print("\n\n\n\n\n here \n\n\n\n\n\n")
            risks = {}
            query_1 = \
                f"select * from State_real_estate where \
                price >= {realty_range[0]} && price <= {realty_range[1]}"
            query_2 = \
                f"select * from State_life_expec where state in \
                    (select state from State_real_estate \
                    where price >= {realty_range[0]} \
                    && price <= {realty_range[1]})"
            query_3 = \
                f"select * from State_vaccinations where state in \
                    (select state from State_real_estate \
                    where price >= {realty_range[0]} \
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

            conn.close()
            return jsonify(merge)

        else:
            merge = []
            risks = {}
            covid_score_state = {}
            query_1 = \
                f"select id, name, state, price, age from Counties inner join \
                County_life_expec on Counties.id = County_life_expec.cnty \
                inner join County_real_estate on \
                County_life_expec.cnty = County_real_estate.cnty \
                where price >= {realty_range[0]} && price <= {realty_range[1]}"
            query_2 = \
                f"select * from State_vaccinations where state in \
                (select state from Counties inner join \
                County_real_estate on id = cnty \
                where price >= {realty_range[0]} && price <= {realty_range[1]})"


            cur.execute(query_1)
            data = cur.fetchall()

            cur.execute(query_2)
            state_covid = cur.fetchall()

            for state in state_covid:
                num = state["total_vaccinations_per_hundred"] * \
                    state["daily_vaccinations_per_million"]
                dem = (state["people_vaccinated_per_hundred"] - \
                     state["people_fully_vaccinated_per_hundred"])
                covid_score_state[state["state"]] = dem / num

            for cnty in data:
                cnty["risk"] = (covid_score_state[cnty["state"]] / cnty["age"]) * 10000000

            conn.close()
            return jsonify(data)
