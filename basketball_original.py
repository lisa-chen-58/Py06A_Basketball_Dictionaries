from pprint import pprint 

players = [
        {
        "name": "Kevin Durant", 
        "age":34, 
        "position": "small forward", 
        "team": "Brooklyn Nets"
        },
        {
        "name": "Jason Tatum", 
        "age":24, 
        "position": "small forward", 
        "team": "Boston Celtics"
        },
        {
        "name": "Kyrie Irving", 
        "age":32, "position": "Point Guard", 
        "team": "Brooklyn Nets"
        },
        {
        "name": "Damian Lillard", 
        "age":33, "position": "Point Guard", 
        "team": "Portland Trailblazers"
        },
        {
        "name": "Joel Embiid", 
        "age":32, "position": "Power Foward", 
        "team": "Philidelphia 76ers"
        },
        {
        "name": "", 
        "age":16, 
        "position": "P", 
        "team": "en"
        }
]


kevin = {
        "name": "Kevin Durant", 
        "age":34, 
        "position": "small forward", 
        "team": "Brooklyn Nets"
}
jason = {
        "name": "Jason Tatum", 
        "age":24, 
        "position": "small forward", 
        "team": "Boston Celtics"
}
kyrie = {
        "name": "Kyrie Irving", 
        "age":32, "position": "Point Guard", 
        "team": "Brooklyn Nets"
}



# Challenge 1: Update the Constructor
class Player:
        def __init__(self, data):
                self.name = data['name']
                self.age = data['age']
                self.position = data['position']
                self.team = data['team']
                # Player.new_team.append(self)

        def __repr__(self):
                return (f"Player: {self.name} \n Age: {self.age} \n Position: {self.position} \n Team: {self.team}")
                

        @classmethod
        def get_team(cls, list_of_dict):
                team_list=[]
                for member in list_of_dict:
                        team_list.append(member)
                return team_list;

# Challenge 2: Create instances using individual player dictionaries.

# Create your Player instances here!
player_kevin = Player(kevin)
player_jason = Player(jason)
player_kyrie = Player(kyrie)

# ... (class definition and large list of players here)
new_team = []

# Write your for loop here to populate the new_team variable with Player objects.
for player in players:
        new_player = Player(player)
        new_team.append(new_player)
        pprint(new_team)

# Add an @class method called get_team(cls, team_list) that, given a list of dictionaries populates and returns a new list of Player objects. Be sure to test your method!
# print(Player.get_team(new_team))

