import discord

client = discord.Client()


@client.event
async def on_message(message):
    id = client.get_guild(721629167677865985)

    if message.content.find("!users") !=-1:
        await message.channel.send(f"""Number of Members: {id.member_count}""") 

client.run('token')