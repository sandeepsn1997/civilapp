from flask import Flask

import calculate

app = Flask(__name__)

@app.route("/")
def index():
    important_facility_data = [["site office", 10, 0, 500, 500, 0, 0], ["labour shed", 5, 0, 10000, 500, 0, 0],
                               ["security shed", 5, 0, 200, 0, 0, 0], ["Batching plant", 10, 100, 20000, 1000, 2, 2],
                               ["Warehouse", 10, 500, 10000, 1000, 7, 1], ["QC lab", 10, 0, 500, 500, 0, 0]]
    less_important_facility_data = [("site canteen", 5, 0, 10000, 0, 0, 0), ("Toilets", 5, 0, 200, 0, 0, 0),
                                    ("watertank", 2, 100, 5000, 200, 1, 2), ("Power house", 1, 0, 1000, 1000, 0, 0),
                                    ("Parking", 3, 0, 200, 0, 0, 0)]

    return str(calculate.main(important_facility_data,less_important_facility_data))


app.run()



