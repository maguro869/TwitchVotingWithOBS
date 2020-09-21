import json
import csv

class Util:

    __fighter_file = open('data/fighter.json')
    __fighter_json = json.load(__fighter_file)
    __score_file = open('data/score.csv', mode='a',encoding='utf8')

    def __init__(self):
        
        self.fighter_list = []
        for phase in self.__fighter_json.values():
            for team in phase.values():
                for fighter in team.values():
                    self.fighter_list.append(fighter)
    


    def save_score(self,red,blue):
        writer = csv.writer(self.score_file)
        writer.writerow(red.append('red'))
        writer.writerow(blue.append('blue'))


    def get_fighter_name(self,phase,team):
        return self.fighter_info['phase'][str(phase)][team]['name']

    def get_team(self,name):
        for fighter in self.fighter_list:
            if fighter['name'] == name:
                return fighter['team']

    def get_phase(self,name):
        for fighter in self.fighter_list:
            if fighter['name'] == name:
                return fighter['phase']

    def close(self):
        __fighter_file.close()
        __score_file.close()


    def make_score_format(self,phase,team,score):
        return [phase,team,score,get_fighter_name(phase,team)]
