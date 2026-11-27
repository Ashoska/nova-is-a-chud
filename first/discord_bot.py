import discord
from discord.ext import commands
from discord import app_commands
import modules1 as m1
import random
import os
from dotenv import load_dotenv

#discord bot needs
intents = discord.Intents.default()
intents.message_content = True


#discord bot
class Novabot(commands.Bot):
    async def on_ready(self):
        guild = discord.Object(id=1506072468639711324)
        self.tree.copy_global_to(guild=guild)
        await self.tree.sync(guild=guild)
        print(f'Logged in as {self.user} (ID: {self.user.id})')

bot = Novabot(command_prefix='', intents=intents)












#looking for job
@bot.tree.command(name="looking_jobs", description="look for jobs")
async def looking_jobs(interaction: discord.Interaction, job_title: str, city: str, state: str, region: str):
    print(f"looking_jobs with job_title='{job_title}' and location='{city}, {state}, {region}'")
    await interaction.response.defer(thinking=True, ephemeral=True)
    discord_file_send = m1.analyze_job_results(job_title, city, state, region)
    await interaction.followup.send(file=discord_file_send, ephemeral=True)
















#bot randomly tell you to get a job
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    else:
        random_timing = random.randint(1, 2)
        if random_timing == 1:
            await message.channel.send(f"GET A JOB\nyou can find one with /looking_jobs")
            await message.channel.send(file=discord.File("jobs_files/GET_A_JOB.jpg"))
            print("jump in")
        else:
            return
    await bot.process_commands(message)















#time
time_group = app_commands.Group(name="time", description="to tell the time :3")

@time_group.command(name="check_time", description="to check the time")
async def check_time(interaction: discord.Interaction, timezone: str):
    print(f"time")
    await interaction.response.send_message(f"{m1.get_time(timezone)}", ephemeral=True)

@time_group.command(name="timezones_types", description="to see all timezones types")
async def timezones_types(interaction: discord.Interaction):
    print("time 2")
    await interaction.response.send_message(file=discord.File("time.txt"), ephemeral=True)

bot.tree.add_command(time_group)












#weather
@bot.tree.command(name="weather", description="get your weather")
async def weather(interaction: discord.Interaction, city: str):
    print(f"loading weather for city='{city}'")
    await interaction.response.defer(thinking=True, ephemeral=True)
    result = m1.get_weather(city)
    await interaction.followup.send(result, ephemeral=True)

#get
load_dotenv()
bot.run(os.getenv("discord_key"))