import sys
print(sys.executable)
import discord
class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')
    async def on_message(self, message):
        # we do not want the bot to reply to itself
        if message.author.id == self.user.id:
            return
        if message.content.startswith('!woof'):
            await message.channel.send('Bow Bow'.format(message))
        if message.author.id == self.user.id:
            return
        if message.content.startswith('!hello'):
            await message.channel.send('Hello, I am Doge, a doge bot'.format(message))
        if message.author.id == self.user.id:
            return
        if message.content.startswith('!frisbee'):
            await message.channel.send('Woof woof, throw it, Imma jump and catch the frisbee '.format(message))
        if message.author.id == self.user.id:
            return
        if message.content.startswith('!GooduDoge'):
            await message.channel.send('*happy doge noises'.format(message))
        if message.author.id == self.user.id:
            return
        if message.content.startswith('!wish'):
            await message.channel.send('woof woof! How are you? {0.author.mention}'.format(message))
        if message.author.id == self.user.id:
            return
        if message.content.startswith('!info'):
            await message.channel.send('Hello, I am Doge, A discord bot made by NaziDoge using Python. I am made to serve your needs'.format(message))
        if message.author.id == self.user.id:
            return
        if message.content.startswith('you like cats?'):
            await message.channel.send('Nah, I hate them '.format(message))
        if message.author.id == self.user.id:
            return
        if message.content.startswith('!aim'):
            await message.channel.send('Hands up! You are surrounded '.format(message))
        if message.author.id == self.user.id:
            return
        if message.content.startswith('!realize'):
            await message.channel.send('You left me alone aa?'.format(message))
        
            
client = MyClient()
client.run('token')
        
            
