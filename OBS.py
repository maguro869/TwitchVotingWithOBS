from obswebsocket import obsws
import obswebsocket.requests as obsRequests
from config import Config

class OBS(obsws):

    RED_SCORE_SOURCE_NAME = 'RED_SCORE'
    BLUE_SCORE_SOURCE_NAME = 'BLUE_SCORE'

    def __init__(self,host,port,password):

        super.__init__(host, port, password)
        self.connect()
        
        red_score_source = self.call(
            obsRequests.GetSourceSettings(
                RED_SCORE_SOURCE_NAME))

        blue_score_source =self.call(
            obsRequests.GetSourceSettings(
                BLUE_SCORE_SOURCE_NAME))

    # teamに得点を追加、描画
    def add_score(self,mteam) -> None:
        pass

    # 試合終了後の両チームScoreリセット
    def reset_score(self) -> None:
        pass
