import discord
from discord.ext import commands


class Client(commands.Bot):
    def __init__(self):
        intents = discord.Intents.all()
        super().__init__(
            command_prefix='!',
            case_insensitive=True,
            help_command=commands.DefaultHelpCommand(),
            intents=intents
        )

    async def on_ready(self):
        print("=" * 40)
        print(f"✅ TimeLeaper is online!")
        print(f"🤖 Logged in as: {self.user} (ID: {self.user.id})")
        print(f"📂 Connected to {len(self.guilds)} servers:")
        for guild in self.guilds:
            print(f"   - {guild.name} (ID: {guild.id}, Members: {guild.member_count})")
        print(f"🕒 Latency: {round(self.latency * 1000)} ms")
        print("=" * 40)