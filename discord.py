import discord
from discord.ext import commads
from korcen import korcen

@bot.event
async def on_message(message):
    print(korcen.check(message.content))
    if korcen.check(message.content):
        await message.delete()
        embed = nextcord.Embed(title = "메세지 삭제함", description = "", color=0xFF2424)
        embed.set_footer(text = "© Korcen")
        await message.channel.send(embed=embed)
