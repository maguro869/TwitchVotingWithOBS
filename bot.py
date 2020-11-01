from twitchio.ext import commands
from obswebsocket import obsws
from util import Util
from config import MASTER_ID


class Bot(commands.Bot):

    def __init__(self,token,client_id,bot_nick,bot_prefix,channel,obs:obsws):
        super().__init__(
            irc_token=token,
            client_id=client_id,
            nick=bot_nick,
            prefix=bot_prefix,
            initial_channels=channel,
            )

        # 引数で受け取るobsの操作を行う為のオブジェクト
        self.obs = obs

        self.vote_flag = False
        self.red_score_list = []
        self.blue_score_list = []
        self.red_score = 0
        self.blue_score = 0
        self.phase = 1
        self.ADD_SCORE = 5
        self.util = Util()

    async def initalize(self) -> None:
        print('initalize')
        self.red_score = 0
        self.blue_score = 0
        self.obs.reset_score()

    async def result_match(self):
        self.red_score_list.append(self.red_score)
        self.blue_score_list.append(self.blue_score)
        print(f'redscore_list:{self.red_score_list}')
        print(f'bluescore_list:{self.blue_score_list}')

    async def event_ready(self):
        print(f'ONLINE | {self.nick}')

    @commands.command(name='red')
    async def red(self, ctx):
        print('red')
        if self.vote_flag:
            print(f'red_score:{self.red_score}')
            self.red_score += self.ADD_SCORE
            self.obs.display_score('red',self.red_score)
            

    @commands.command(name='blue')
    async def blue(self, ctx):
        print('blue')
        if self.vote_flag:
            self.blue_score += self.ADD_SCORE
            self.obs.display_score('blue',self.blue_score)
            
    
    @commands.command(name='ready')
    async def ready(self, ctx):
        print('ready')
        print(f'ctx.author.name {ctx.author.name}')
        if ctx.author.name == MASTER_ID:
            self.vote_flag = True
            await self.initalize()
    
    @commands.command(name='timeup')
    async def timeup(self, ctx):
        print('timeup')
        if ctx.author.name == MASTER_ID:
            self.vote_flag = False
            await self.result_match()
            self.util.save_score(self.phase, self.red_score, self.blue_score)
            self.phase += 1
            print(self.phase)

    @commands.command(name='total')
    async def total(self, ctx):
        print('total')
        if ctx.author.name == MASTER_ID:
            red_total_score, blue_total_score = self.util.get_total_score()
            self.obs.display_score('red',red_total_score)
            self.obs.display_score('blue',blue_total_score)
            
    
    @commands.command(name='dc')
    async def dc(self, ctx):
        if ctx.author.name == MASTER_ID:
            self.obs.disconnect()
            self.disconnest()
