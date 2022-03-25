# Write a program that displays the details of a cricket player.
# The details must include his name, match played, run rate, wicket taken, maiden overs
# Overs played, number of centuries and half centuries etc

class Cricket:
    def __init__(self ):
        
        self.name = input('Enter the name of the player : ')
        self.match_played = input('Enter the match played : ')
        self.run_rate = int(input('Enter the run rate : '))
        self.wicket_taken = int(input('Enter the wicket taken : '))
        self.maiden_overs = int(input('Enter the maiden overs : '))
        self.overs = int(input('Enter the overs played : '))
        self.number_of_centuries = int(input('Enter the number of centuries : '))
        self.half_centuries = int(input('Enter the number of half centuries played : '))
    
    def display(self):
        print(f'{self.name}, plays {self.match_played} and has a run rate of {self.run_rate}. {self.name} has taken {self.wicket_taken} wickets. also has {self.maiden_overs} maiden overs with {self.overs} overs in {self.number_of_centuries} centuries and {self.half_centuries} half centuries')
        
c = Cricket()
c.display()
print(c)