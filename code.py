# --------------
import yaml

# Read the data of the format .yaml type
with open(path) as f:
     data = yaml.load(f)
# Find data type of the file
type_of_data = type(data)
print(type_of_data)
# In which city, and at which venue the match was played and where was it played ?
city = data['info']['city']
print(city)
venue = data['info']['venue']
print(venue)
# Which are all the teams that played in the tournament ? How many teams participated in total?
teams = data['info']['teams']
print(teams)
print(len(teams))
# Which team won the toss and what was the decision of toss winner ?
toss = data['info']['toss']['winner']
print(toss)
toss_winner = data['info']['toss']['decision']
print(toss_winner)
# Find the first bowler and first batsman who played the first ball of the first inning
first_bowler = data['innings'][0]['1st innings']['deliveries'][0][0.1]['bowler']
first_batsman = data['innings'][0]['1st innings']['deliveries'][0][0.1]['batsman']
print(first_bowler)
print(first_batsman)
# How many deliveries were delivered in first inning ?
first_innings_delieveries = len(data['innings'][0]['1st innings']['deliveries'])
print(first_innings_delieveries)
# How many deliveries were delivered in second inning ?
delieveries_second_innings = len(data['innings'][1]['2nd innings']['deliveries'])
print(delieveries_second_innings)
# Which team won and how ?
winner = data['info']['outcome']['winner']
print(winner)
how_they_won = data['info']['outcome']['by']['runs']
print(how_they_won)


