from typing import Final
import os

import discord
from dotenv import load_dotenv
from discord import Intents, Client, Message, app_commands
from discord.ext import commands
from responses import get_response

#load token
load_dotenv()
TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')
print(TOKEN)

bot = commands.Bot(command_prefix="!", intents=Intents.default())

#startup
@bot.event
async def on_ready() -> None:
    print(f'{bot.user} is now running!')
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} command(s)")
    except Exception as e:
        print(e)

@bot.tree.command(name="hi")
async def hi(interaction: discord.Interaction):
    await interaction.response.send_message(f"hi {interaction.user.mention}", ephemeral=True)

@bot.tree.command(name="song")
@app_commands.describe(song_to_compare = "What song would you like me to compare")
async def song(interaction: discord.Interaction, song_to_compare: str):
    await interaction.response.send_message(f'{interaction.user.mention} ... No song quite compares to {song_to_compare}')

#main entrypoint
def main() -> None:
    bot.run(token=TOKEN)

if __name__ == '__main__':
    main()