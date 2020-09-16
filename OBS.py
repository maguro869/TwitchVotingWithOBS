from obswebsocket import obsws
import obswebsocket.requests as obsRequests

class OBS(obsws):

    

    def __init__(self,host,port,password):

        super().__init__(host, port, password)
        self.connect()
        
        self.RED_SCORE_SOURCE_NAME = 'RED_SCORE'
        self.BLUE_SCORE_SOURCE_NAME = 'BLUE_SCORE'

        self.red_score_source = self.call(
            obsRequests.GetSourceSettings(
                self.RED_SCORE_SOURCE_NAME))
        
        self.red_score_settings = self.red_score_source.getSourcesettings()
        print(f'red_score_settings[text]:{self.red_score_settings["text"]}')

        self.blue_score_source =self.call(
            obsRequests.GetSourceSettings(
                self.BLUE_SCORE_SOURCE_NAME))

        self.blue_score_settings = self.blue_score_source.getSourcesettings()
        print(f'blue_score_settings[text]:{self.blue_score_settings["text"]}')

    # teamに得点を追加、描画
    def display_score(self,team,score) -> None:
        print('obs.display_score')
        if team == 'red':
            print('obs.display_score.red')
            self.red_score_settings['text'] = str(score)
            self.call(
                obsRequests.SetSourceSettings(
                    self.RED_SCORE_SOURCE_NAME,
                    sourceSettings=self.red_score_settings))

        if team == 'blue':
            print('obs.display_score.blue')
            self.blue_score_settings['text'] = str(score)
            self.call(
                obsRequests.SetSourceSettings(
                    self.BLUE_SCORE_SOURCE_NAME,
                    sourceSettings=self.blue_score_settings))
        

    # 試合終了後の両チームScoreリセット
    def reset_score(self) -> None:
        self.red_score_settings['text'] = '0'
        self.blue_score_settings['text'] = '0'
        self.call(
            obsRequests.SetSourceSettings(
                self.RED_SCORE_SOURCE_NAME,
                sourceSettings=self.red_score_settings))
        self.call(
            obsRequests.SetSourceSettings(
                self.BLUE_SCORE_SOURCE_NAME,
                sourceSettings=self.blue_score_settings))
