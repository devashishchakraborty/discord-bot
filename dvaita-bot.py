import discord
from discord.ext import commands
import random
from twitter_api import Posts

client = commands.Bot(command_prefix=";")


@ client.event
async def on_ready():
    print("Bot is Ready")


@ client.command()
async def ping(ctx):
    await ctx.send("Pong!")


@ client.command(aliases=["8ball", "test"])
async def _8ball(ctx, *, question):
    responses = ['It is certain', 'It is decidedly so', 'Without a doubt', 'Yes – definitely', 'You may rely on it', 'As I see it, yes', 'Most likely', 'Outlook good', 'Yes Signs point to yes', 'Reply hazy',
                 'try again', 'Ask again later', 'Better not tell you now', 'Cannot predict now', 'Concentrate and ask again', 'Dont count on it', 'My reply is no', 'My sources say no', 'Outlook not so good', 'Very doubtful']
    await ctx.send(f"\nQuestion: {question}\n Answer: {random.choice(responses)}")


@ client.command()
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount)


@ client.command()
async def cows(ctx):
    posts = Posts()
    embed = discord.Embed(title="Dakshin Vrindavan", description=posts.text,
                          color=discord.Colour.orange())
    embed.set_image(url=posts.image_url)
    await ctx.send(embed=embed)


client.run("DISCORD BOT TOKEN")
