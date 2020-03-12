#imports
from flask import Flask
import csv
import json

#open csv and create list
with open("CBB Data.csv", newline="") as f:
    reader = csv.DictReader(f)
    myList = list(reader)

#set up flask routes
app = Flask("app")


#original list
@app.route("/")
def allStats():
    return json.dumps(myList)


#sort by team's ppg
@app.route("/team-ppg")
def teamPPG():
    sortedList = sorted(
        myList, key=lambda i: i["Team Points per Game"], reverse=True)
    return json.dumps(sortedList)


#filter by whatever conference
@app.route("/get-conference/<conference>")
def getConference(conference):
    filteredList = []
    for i in myList:
        if (i["Conference"]) == conference:
            filteredList.append(i)
    return json.dumps(filteredList)


#top 20 scorers
@app.route("/top-20-scorers")
def topTwenty():
    sortedList = sorted(
        myList, key=lambda i: i["Points per Game"], reverse=True)
    return json.dumps(sortedList[:20])


#get conference and sort in order of teams with highest PPG leader
@app.route("/leading-scorers/<conference>")
def leadScorers(conference):
    filteredList = []
    for i in myList:
        if (i["Conference"]) == conference:
            filteredList.append(i)
    sortedList = sorted(
        filteredList, key=lambda i: i["Points per Game"], reverse=True)
    return json.dumps(sortedList)


#search for individual players, will only return player if they lead team in ppg, rebounds, and/or assists
@app.route("/find-player/<player>")
def getPlayer(player):
    filteredList = []
    for i in myList:
        if (i["Scoring Leader"]) == player:
            filteredList.append(i)
        elif (i["Rebounds Leader"]) == player:
            filteredList.append(i)
        elif (i["Assists Leader"]) == player:
            filteredList.append(i)
    return json.dumps(filteredList)


#search for individual teams
@app.route("/find-team/<team>")
def getTeam(team):
    filteredList = []
    for i in myList:
        if (i["School"]) == team:
            filteredList.append(i)
    return json.dumps(filteredList)


#top 10 offensive rating
@app.route("/top-10-ORtg")
def topTen():
    sortedList = sorted(
        myList, key=lambda i: i["Offensive Rating"], reverse=True)
    return json.dumps(sortedList[:10])


#starts host
app.run(host="0.0.0.0", port=8080)
