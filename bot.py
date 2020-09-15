from twitchio.ext import commands
from obswebsocket import obsws
from config import Config

class Bot(commands.Bot):

    def __init__(self,obs:obsws):
        super().__init__(
            irc_token='...', 
            client_id='...', 
            nick='...', 
            prefix='/',
            initial_channels=['...'],
            )

        # 引数で受け取るobsの操作を行う為のオブジェクト
        self.obs = obs

        self.vote_flag = False
        self.red_score_list = []
        self.blue_scpre_list = []
        self.red_score = 0
        self.blue_score = 0

    def initalize(self) -> None:
        self.red_score = 0
        self.blue_score = 0
        self.obs.reset_score()

    def result_match(self):
        self.red_score_list.append(self.red_score)
        self.blue_score_list.append(self.blue_score)

    async def event_ready(self):
        print(f'ONLINE | {self.nick}')

    @commands.command(name='red')
    async def red(self, ctx):
        if vote_flag:
            self.red_score += 1
            self.obs.add_score('red')
            pass

    @commands.command(name='blue')
    async def blue(self, ctx):
        if vote_flag:
            self.blue_score += 1
            self.obs.add_score('blue')
            pass
    
    @commands.comand(name='ready')
    async def ready(self, ctx):
        if ctx.author.id == Config.MASTER_ID:
            vote_flag = True
            self.initalize()
    
    @commands.command(name='timeup')
    async def timeup(self, ctx):
        if ctx.author.id == Config.MASTER_ID:
            vote_flag = False
            self.result_match()
    