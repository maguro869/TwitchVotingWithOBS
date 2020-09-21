import json
import csv

class Util():

    def __init__(self):
        self.fighter_file = open('data/fighter.json')
        self.fighter_info = json.load(self.fighter_file)
        self.score_file = open('data/score.csv', mode='a',encoding='utf8')
    


    def save_score(self,red,blue):
        writer = csv.writer(self.score_file)
        writer.writerow(red.append('red'))
        writer.writerow(blue.append('blue'))


    def get_fighter_name(self,phase,team):
        return self.fighter_info['phase'][str(phase)][team]['name']

    def get_team(self,name):
        for phase in self.fighter_info.values():
            for team in phase.values():
                for fighter in team.values():
                    if fighter['name'] == name:
                        return fighter['team']

    def get_phase(self,name):
        for phase in self.fighter_info.values():
            for team in phase.values():
                for fighter in team.values():
                    if fighter['name'] == name:
                        return int(fighter['phase'])

    def close(self):
        self.fighter_file.close()
        self.score_file.close()


    def make_score_format(self,phase,team,score):
        return [phase,team,score,get_fighter_name(phase,team)]
