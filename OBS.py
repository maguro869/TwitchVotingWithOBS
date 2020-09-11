from obswebsocket import obsws
import obswebsocket.requests as obsRequests
from setting import Setting

class OBS(obsws):

    RED_SCORE_SOURCE_NAME = 'RED_SCORE'
    BLUE_SCORE_SOURCE_NAME = 'BLUE_SCORE'

    def __init__(self,host,port,password):

        super.__init__(host, port, password)
        self.connect()
        
        # red_score_source = self.call(obsRequests.テキストのソース)
        # blue_score_source = self.call(obsRequests.テキストのソース)

    # teamに得点を追加、描画
    def addScore(team) -> None:
        pass

    # 試合終了後の両チームScoreリセット
    def resetScore() -> None:
        pass