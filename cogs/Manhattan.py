import os, sys

import discord
from discord.ext import flags, commands
# using relative import to import a module from a parent directory
from tesco import search
from portfolio import Portfolio

current_dir = os.path.dirname(os.path.realpath((__file__)))
root_dir = os.path.dirname(current_dir)
sys.path.append(root_dir)

EMBED_COLOUR = 0xff9416


class Manhattan(commands.Cog):
    """
    Manhattan bot
    -------------

    The main object for all subcommands of the Manhattan bot
     a.k.a "Bitcoin's Eye"
    ....

    Attributes:
    -----------
    manhattan
        Used as "$manhattan".
        Does not provide a response to the user

    price
        Used as "$manhattan price `<ticker>`". 
        Responds with the price of the asset given

    pft: Portfolio
        Used as "$manhattan pft <ticker> <entry> <target(optional)>".
        Creates a portfolio for the user
    """
    def __init__(self, client):
        self.client = client

    @commands.group(name='manhattan', aliases=["m"],  invoke_without_command=False)
    async def manhattan(self, ctx):
        # await ctx.channel.send("Base group for the Manhattan bot")
        pass


    @flags.add_flag('-c')
    @flags.add_flag('-g')
    @manhattan.command(name='price', cls=flags.FlagCommand)
    async def price(self, ctx, **flags):
        await ctx.channel.send(search.refresh_data())

    @manhattan.command(name='pft')
    async def pft(self, ctx, ticker: str, entry: int, *, arg):
        """
        Shows the portfolio only

        Parameters
        ----------
        ticker: str
            The ticker symbol
        
        entry: int
            The entry price of the asset specified
        """
        embed = discord.Embed(
            title = f"{ctx.message.author.name}'s portfolio",
            description = "This is what your portfolio looks like",
            colour = discord.Colour(EMBED_COLOUR),
            icon_url = ctx.message.author.avatar_url
            )



        self.pft = Portfolio()
        self.pft.update_portfolio(ticker, entry, target=arg)
        print(self.pft.portfolio)

        # embed.set_thumbnail(url="https://i.imgur.com/axLm3p6.jpeg")
        embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
        embed.add_field(name="Ticker", value=self.pft.portfolio["tick_name"], inline=True)
        embed.add_field(name="Entry", value=self.pft.portfolio["entry"], inline=True)
        embed.add_field(name="Target/Exit", value=self.pft.portfolio["target"], inline=True)
        embed.set_footer(text="Bitcoin's Eye. Powered by ThePyLord.")
        await ctx.send(embed=embed)

    @manhattan.command()
    async def ping(self, ctx, invoke_without_command=True):
        await ctx.send(f"Pong {round(self.client.latency, 3)}")


def setup(client):
    client.add_cog(Manhattan(client))