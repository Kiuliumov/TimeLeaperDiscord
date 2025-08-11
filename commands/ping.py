import discord
from discord import app_commands
from discord.ext import commands

class Ping(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

    @app_commands.command(name="ping", description="Pong!")
    async def ping(self, interaction: discord.Interaction):
        latency_ms = round(self.client.latency * 1000)
        await interaction.response.send_message(f"Pong! {latency_ms}ms")

async def setup(client):
    await client.add_cog(Ping(client))

