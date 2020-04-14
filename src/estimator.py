import math
import pprint

data = {"region": {"name": {"Africa"},                             #input details
                             "avgAge": "19.7",
                             "avgDailyIncomeInUSD": "5",
                             "avgDailyIncomePopulation": "0.71"
                              },
                    "periodType": "days",     #subject to modification
                    "timetoElapse": "58",
                    "reportedCases": "674",
                    "population": "66622705",
                    "totalHospitalBeds": "1380614"
                    }

def estimator(data):
    data = {"name": {input()},  # input details
                       "avgAge": input(),
                       "avgDailyIncomeInUSD": input(),
                       "avgDailyIncomePopulation": input(),

            "periodType": input(),
            "timetoElapse": input(),
            "reportedCases": input(),
            "population": input(),
            "totalHospitalBeds": input()
            }

    return data


def impactEstimator():
    timeToElapse = int(estimator(data)["timetoElapse"])
    severityFactor = int(timeToElapse) / 3
    impactFactor = int(timeToElapse / 3)
    reportedCases = int(estimator(data)['reportedCases'])
    currentlyInfected = int(reportedCases * 10)
    infectionsRequest = int(currentlyInfected) * (2 * math.pow(2, severityFactor))
    severeCasesRequest = int(infectionsRequest) * 0.15
    availableBeds = int(estimator(data)["totalHospitalBeds"]) * 0.35

    impact= {
        "currentlyInfected": str(currentlyInfected),   #subject to change
        "infectionsByRequestTime": str(currentlyInfected * (2 * math.pow(2,impactFactor))),
        "severeCasesByRequestedTime":  str(severeCasesRequest),
        "hospitalBedsByRequestTime":str(availableBeds - severeCasesRequest),
        "casesForICUByRequestTime":  str(infectionsRequest * 0.05),
        "casesForVentilatorsByRequestTime":str(infectionsRequest * 0.02),
        "dollarsInFlight": str(int(infectionsRequest) * int(estimator(data)["avgDailyIncomePopulation"]) * int(estimator(data)["avgDailyIncomeInUSD"]))
    }

    return impact

def severityEstimator():
    timeToElapse = int(estimator(data)["timetoElapse"])
    severityFactor = int(timeToElapse)/3
    availableBeds = int(estimator(data)["totalHospitalBeds"]) * 0.35
    reportedCases = int(estimator(data)['reportedCases'])
    currentlyInfected = int(reportedCases * 50)
    infectionsRequest = int(currentlyInfected) * (2 * math.pow(2, severityFactor))
    severeCasesRequest = int(infectionsRequest) * 0.15

    severeImpact = {
        "currentlyInfected": str(currentlyInfected),
        "infectionsByRequestedTime": str(infectionsRequest),
        "severeCasesByRequestedTime": str(severeCasesRequest) ,
        "hospitalBedsByRequestTime": str(availableBeds - severeCasesRequest),
        "casesForICUByRequestTime": str(infectionsRequest * 0.05),
        "casesForVentilatorsByRequestTime": str(infectionsRequest * 0.02),
        "dollarsInFlight": str(int(infectionsRequest) * int(estimator(data)["avgDailyIncomePopulation"]) * int(estimator(data)["avgDailyIncomeInUSD"]))
    }

    return severeImpact

def convert():
    if data["periodType"] == "weeks": #SUBJECT TO CHANGE
        weeksToDays()
    elif data["periodType"] == "months": #subject to change
        monthsToDays()

def weeksToDays():
    estimator(data)
    data["periodType"].set(int(data["periodType"].get())*7)

def monthsToDays():
    estimator(data)
    data["periodType"].set(int(data["periodType"].get())*30)

def display():
    from pprint import pprint as pp
    print("input data in the following order:")
    print(data)
    pp(estimator(data))
    pp(severityEstimator())
    pp(impactEstimator())

if __name__=='__main__':
    display()
