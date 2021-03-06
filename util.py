import json
import csv

class Util:



    def __init__(self):
        self.__fighter_file = open('data/fighter.json')
        self.__fighter_json = json.load(self.__fighter_file)
        self.fighter_list = []
        for phase in self.__fighter_json.values():
            for team in phase.values():
                for fighter in team.values():
                    self.fighter_list.append(fighter)
    
    def get_total_score(self):
        read_file = open('data/score.csv',encoding='utf8')

        reader = csv.reader(read_file)
        red_score = 0
        blue_score = 0

        for info in reader:
            if info[1] == 'red':
                red_score += int(info[3])
            elif info[1] == 'blue':
                blue_score += int(info[3])
        read_file.close()
        return [red_score,blue_score]

    def save_score(self,phase,red_score,blue_score):
        red_info = self.make_score_format(phase,'red',red_score)
        blue_info = self.make_score_format(phase,'blue',blue_score)
        writer = csv.writer(open('data/score.csv', mode='a',encoding='utf8',newline=""))
        writer.writerow(red_info)
        writer.writerow(blue_info)
    
    def get_fighter_info(self,phase,team):
        for fighter in self.fighter_list:
            if fighter['phase'] == phase and fighter['team'] == team:
                return fighter.values()

    def get_fighter_name(self,phase,team):
        for fighter in self.fighter_list:
            if fighter['phase'] == phase and fighter['team'] == team:
                return fighter['name']

    def get_team(self,name):
        for fighter in self.fighter_list:
            if fighter['name'] == name:
                return fighter['team']

    def get_phase(self,name):
        for fighter in self.fighter_list:
            if fighter['name'] == name:
                return fighter['phase']

    def close(self):
        self.__fighter_file.close()


    def make_score_format(self,phase,team,score):
        return [phase,team,self.get_fighter_name(phase,team),score]

    
