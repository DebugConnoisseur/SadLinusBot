import discord
import logging
import asyncio
client=discord.Client()

class MyClient(discord.Client):
     async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')

@client.event
async def on_message(message):
    ...
    if message.content == "!help":
        embed = discord.Embed(title="Help on BOT", description="Some useful commands")
        embed.add_field(name="!hello", value="Greets the user")
        embed.add_field(name="!users", value="Prints number of users")
        await message.channel.send(content=None, embed=embed)
    ...

client.run('NzQ5MTM5OTg0MzIxMzQ3Njc0.X0no-g.WJJEz4_WPowJygXDeAoVcMwbH1o')
