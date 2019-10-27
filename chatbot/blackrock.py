'''
get risk score
'''

import requests

"""
For the examples we are using 'requests' which is a popular minimalistic python library for making HTTP requests.
Please use 'pip install requests' to add it to your python libraries.
"""

def getRiskScore(pairs):
    positions = ""
    for key in pairs:
        if key != "USD":
            positions += key + "~" + str(pairs[key]) + "|"
    positions = positions[0: len(positions) - 1]
    portfolioAnalysisRequest = requests.get("https://www.blackrock.com/tools/hackathon/portfolio-analysis?calculateRisk=true", params={'positions' : positions, "calculateExposures" :  "true",
"calculatePerformance" :  "false"} )
    if "riskData" not in portfolioAnalysisRequest.json()["resultMap"]["PORTFOLIOS"][0]["portfolios"][0]:
            return 0
    else:
            return portfolioAnalysisRequest.json()["resultMap"]["PORTFOLIOS"][0]["portfolios"][0]["riskData"]["totalRisk"]
