import json
import csv

class Util:

    __fighter_file = open('data/fighter.json')
    __fighter_json = json.load(__fighter_file)
    __score_file = open('data/score.csv', mode='a',encoding='utf8')
    __writer = csv.writer(self.__score_file)

    def __init__(self):
        
        self.fighter_list = []
        for phase in self.__fighter_json.values():
            for team in phase.values():
                for fighter in team.values():
                    self.fighter_list.append(fighter)
    
    def get_total_score(self):
        reader = csv.reader(self.__score_file)
        red_score = 0
        blue_score = 0

        for info in reader:
            if info[1] == 'red':
                red_score += info[3]
            elif info[1] == 'blue':
                blue_score += info[3]

        return red_score,blue_score 

    def save_score(self,phase,red,blue):
        red_info = get_fighter_info(phase,'red').append(red)
        blue_info = get_fighter_info(phase,'blue').append(blue)
        
        self.__writer.writerow(red_info)
        self.__writer.writerow(blue_info)
    
    def get_fighter_info(self,phase,team):
        for fighter in self.fighter_list:
            if fighter['phase'] == phase and fighter['team'] == team:
                return fighter.values()

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
