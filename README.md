# 2019-2020 NCAA Men's Basketball Web Service
This web service provides access to data on the 2019-2020 NCAA men's basketball season. 

## All Teams

#### Description
Retrieve all data about every team

#### API Call
https://i101-project-2--natepeters.repl.co/

#### Parameters
None

#### Example
https://i101-project-2--natepeters.repl.co/


## Team Points per Game

#### Description
Retrieve all data of every team sorted by how many points they score per game

#### API Call
https://i101-project-2--natepeters.repl.co/team-ppg

#### Parameters
None

#### Example
https://i101-project-2--natepeters.repl.co/team-ppg


## Teams by Conference

#### Description
Retrieve all data about teams from particular conferences

#### API Call
https://i101-project-2--natepeters.repl.co/get-conference/{conference}

#### Parameters
**conference**
The conference to search by

#### Examples
https://i101-project-2--natepeters.repl.co/get-conference/Big_Ten
https://i101-project-2--natepeters.repl.co/get-conference/ACC 


## Top 20 Scorers

#### Description
Retrieve all data about the 20 teams who have the scoring leaders with the highest points per game 

#### API Call
https://i101-project-2--natepeters.repl.co/top-20-scorers

#### Parameters
None

#### Example
https://i101-project-2--natepeters.repl.co/top-20-scorers


## Scoring Leaders in Conference

#### Description
Retrieve all data about teams from particular conferences and sort by leading scorer's points per game

#### API Call
https://i101-project-2--natepeters.repl.co/leading-scorers/{conference}

#### Parameters
**conference**
The conference to search by

#### Example
https://i101-project-2--natepeters.repl.co/leading-scorers/ACC


## Find Player

#### Description
Retrieve all data about a specific team based on a player to search for

#### API Call
https://i101-project-2--natepeters.repl.co/find-player/{player}

#### Parameters
**player**
The player to search by (will only pull a certain team if they are a team's leader in points, rebounds, or assists)

#### Example
https://i101-project-2--natepeters.repl.co/find-player/Cassius%20Winston
(can put space between first and last name or put %20)


## Find Team

#### Description
Retrieve all data about a specific team searched for

#### API Call
https://i101-project-2--natepeters.repl.co/find-team/{team}

#### Parameters
**team**
The team to search for (if it doesn't work, try acronym or longer version of school)

#### Example
https://i101-project-2--natepeters.repl.co/find-team/Michigan%20State
(can put space between words or put %20)


## Top 10 Offensive Ratings

#### Description
Retrieve all data about the teams who have the top 10 offensive ratings

#### API Call
https://i101-project-2--natepeters.repl.co/top-10-ORtg

#### Parameters
None

#### Example
https://i101-project-2--natepeters.repl.co/top-10-ORtg
