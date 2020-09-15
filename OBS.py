from obswebsocket import obsws
import obswebsocket.requests as obsRequests
from config import Config

class OBS(obsws):

    RED_SCORE_SOURCE_NAME = 'RED_SCORE'
    BLUE_SCORE_SOURCE_NAME = 'BLUE_SCORE'

    def __init__(self,host,port,password):

        super.__init__(host, port, password)
        self.connect()
        
        self.red_score_source = self.call(
            obsRequests.GetSourceSettings(
                RED_SCORE_SOURCE_NAME))
        
        self.red_score_settings = red_score_source.getSourcesettings()

        self.blue_score_source =self.call(
            obsRequests.GetSourceSettings(
                BLUE_SCORE_SOURCE_NAME))

        self.blue_score_settings = blue_score_source.getSourcesettings()

    # teamに得点を追加、描画
    def display_score(self,team,score) -> None:
        if team == 'red':
            self.red_score_settings['text'] = str(score)
            self.call(
                obsRequests.SetSourceSettings(
                    RED_SCORE_SOURCE_NAME,
                    sourceSettings=self.red_score_settings))

        if team == 'blue':
            self.blue_score_settings['text'] = str(score)
            self.call(
                obsRequests.SetSourceSettings(
                    BLUE_SCORE_SOURCE_NAME,
                    sourceSettings=self.blue_score_settings))
        

    # 試合終了後の両チームScoreリセット
    def reset_score(self) -> None:
        self.red_score_settings['text'] = '0'
        self.blue_score_settings['text'] = '0'
        self.call(
             obsRequests.SetSourceSettings(
                RED_SCORE_SOURCE_NAME,
                sourceSettings=self.red_score_settings))
        self.call(
            obsRequests.SetSourceSettings(
                BLUE_SCORE_SOURCE_NAME,
                sourceSettings=self.blue_score_settings))
