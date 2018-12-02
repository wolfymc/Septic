import discord
from discord.ext import commands

TOKEN = 'NTE4OTExOTMzMzk5OTU3NTA1.DuXqNg._SMERP59XVVHSvhtmOiz_L5desk'
client = commands.Bot(command_prefix = 's!')

extensions = ['fun','member']

@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name='s!help'))
    print('Bot is ready')
	
@client.command()
async def load(extension):
	try:
		client.load_extension(extension)
		print('Loaded {}'.format(extension))
	except Exception as error:
		print('{} cannot be loaded. [{}]'.format(extension, error))
		
@client.command()
async def unload(extension):
	try:
		client.unload_extension(extension)
		print('Unloaded {}'.format(extension))
	except Exception as error:
		print('{} cannot be unloaded. [{}]'.format(extension, error))
	
if __name__ == '__main__':
	for extension in extensions:
		try:
			client.load_extension(extension)
		except Exception as error:
			print('{} cannot be loaded. [{}]'.format(extension, error))
	
	client.run(TOKEN)
