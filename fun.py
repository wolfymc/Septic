import discord
from discord.ext import commands

class Fun:
	def __init__(self, client):
		self.client = client
		
	async def on_message_delete(self, message):
		await self.client.send_message(message.channel, 'Message deleted.')
	
	@commands.command()
	async def ping(self):
		await self.client.say('Pong!')

    @commands.command()
    async def joined(self, member : discord.Member):
        """Says when a member joined."""
        await self.client.say('{0.name} joined in {0.joined_at}'.format(member))

def setup(client):
	client.add_cog(Fun(client))