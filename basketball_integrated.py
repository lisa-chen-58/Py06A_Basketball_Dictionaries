from pprint import pprint 

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
        new_team=[]
        def __init__(self, data):
                self.name = data['name']
                self.age = data['age']
                self.position = data['position']
                self.team = data['team']
                Player.new_team.append(self)

        @classmethod
        def get_team(cls):
                team_list=[]
                for member in Player.new_team:
                        team_list.append({"name":member.name, "age":member.age, "position":member.position, "team":member.team})
                return team_list;

# Challenge 2: Create instances using individual player dictionaries.

# Create your Player instances here!
player_kevin = Player(kevin)
player_jason = Player(jason)
player_kyrie = Player(kyrie)

# Add an @class method called get_team(cls, team_list) that, given a list of dictionaries populates and returns a new list of Player objects. Be sure to test your method!
pprint(Player.get_team())