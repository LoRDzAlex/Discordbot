# main.py
import datetime
import json
from dotenv import load_dotenv


import nextcord
from nextcord.ext import commands
from config import TOKEN
from nextcord import Interaction, SlashOption, ChannelType
import random
from random import randint

load_dotenv()
agentnames = ["Cypher", "Jett", "Fade", "Killjoy", "Breach", "Brimstone", "Yoru", "Reyna", "Sage", "Kay/O", "Neon", "Omen", "Pheonix", "Raze", "Skye", "Sova", "Viper", "Astra", "Chamber"]



agentpics = ["Agentpics/Astra.png", "Agentpics/Breach.png", "Agentpics/Brimstone.png", "Agentpics/Chamber.png", "Agentpics/Cypher.png", "Agentpics/Fade.png",
             "Agentpics/Jett.png", "Agentpics/KAYO.png", "Agentpics/Killjoy.png", "Agentpics/Neon.png", "Agentpics/Omen.png", "Agentpics/Pheonix.png",
             "Agentpics/Raze.png", "Agentpics/Reyna.png", "Agentpics/Sage.png","Agentpics/Skye.png", "Agentpics/Sova.png", "Agentpics/Viper.png", "Agentpics/yoru.png"]
weaponpics = ["Weapons/bucky.png", "Weapons/bulldog.png", "Weapons/classic.png", "Weapons/frenzy.png", "Weapons/ghost.png", "Weapons/guardian.png", "Weapons/judge.png", "Weapons/knife.png", "Weapons/marshal.png", "Weapons/operator.png", "Weapons/phantom.png", "Weapons/sheriff.png", "Weapons/shorty.png", "Weapons/specter.png", "Weapons/stinger.png", "Weapons/vandal.png"]
agentpicsurl= ["https://images.contentstack.io/v3/assets/bltb6530b271fddd0b1/blt8a627ec10b57f4f2/5eb7cdc16509f3370a5a93b7/V_AGENTS_587x900_sage.png", "https://images.contentstack.io/v3/assets/bltb6530b271fddd0b1/bltf11234f4775729b7/5ebf2c275e73766852c8d5d4/V_AGENTS_587x900_ALL_Sova_2.png", "https://images.contentstack.io/v3/assets/bltb6530b271fddd0b1/bltc825c6589eda7717/5eb7cdc6ee88132a6f6cfc25/V_AGENTS_587x900_Viper.png",
               "https://images.contentstack.io/v3/assets/bltb6530b271fddd0b1/blt158572ec37653cf3/5eb7cdc19df5cf37047009d1/V_AGENTS_587x900_Cypher.png", "https://images.contentstack.io/v3/assets/bltb6530b271fddd0b1/blt6577b1f58530e6b2/5eb7cdc121a5027d77420208/V_AGENTS_587x900_Reyna.png", "https://images.contentstack.io/v3/assets/bltb6530b271fddd0b1/blt53405c26141beff8/5f21fda671ec397ef9bf0894/V_AGENTS_587x900_KillJoy_.png",
               "https://images.contentstack.io/v3/assets/bltb6530b271fddd0b1/blt100d13bfa8286a3d/5eb7cdc11ea0c32e33b95fa2/V_AGENTS_587x900_Breach.png", "https://images.contentstack.io/v3/assets/bltb6530b271fddd0b1/blt4e5af408cc7a87b5/5eb7cdc17bedc8627eff8deb/V_AGENTS_587x900_Omen.png", "https://images.contentstack.io/v3/assets/bltb6530b271fddd0b1/bltceaa6cf20d328bd5/5eb7cdc1b1f2e27c950d2aaa/V_AGENTS_587x900_Jett.png",
               "https://images.contentstack.io/v3/assets/bltb6530b271fddd0b1/blt6fef56a8182d0a81/5ebf2c2798f79d6925dbd6b4/V_AGENTS_587x900_ALL_Raze_2.png", "https://images.contentstack.io/v3/assets/bltb6530b271fddd0b1/blt302fcb2b9628c376/5f7fa6ff8db9ea0f149ece0a/V_AGENTS_587x900_ALL_Skye.png", "https://images.contentstack.io/v3/assets/bltb6530b271fddd0b1/bltd4080f8efb365751/5ff5660bb47cdf7fc7d6c3dc/V_AGENTS_587x900_yoru.png",
               "https://images.contentstack.io/v3/assets/bltb6530b271fddd0b1/blt5599d0d810824279/6036ca30ce4a0d12c3ec1dfa/V_AGENTS_587x900_Astra.png", "https://images.contentstack.io/v3/assets/bltb6530b271fddd0b1/blte5aefeb26bee12c8/60ca5aa30ece0255888d7faa/KAYO_KeyArt_587x900.png", "https://images.contentstack.io/v3/assets/bltb6530b271fddd0b1/blt6f1392b30784e029/618d9da0d380f814d61f001c/WebUpdate_Chamber_KeyArt.png",
               "https://images.contentstack.io/v3/assets/bltb6530b271fddd0b1/blt8093ba7b5e84ed05/61d8a63ddea73a236fc56d12/Neon_KeyArt-Web.png", "https://images.contentstack.io/v3/assets/bltb6530b271fddd0b1/blt516d37c6c84fcda0/625db737c9aa404b76ddd594/Fade_Key_Art_587x900_for_Website.png", "https://images.contentstack.io/v3/assets/bltb6530b271fddd0b1/blt26fcf1b5752514ee/5eb7cdbfc1dc88298d5d3799/V_AGENTS_587x900_Brimstone.png",
               "https://images.contentstack.io/v3/assets/bltb6530b271fddd0b1/bltf0200e1821b5b39f/5eb7cdc144bf8261a04d87f9/V_AGENTS_587x900_Phx.png"]
intents = nextcord.Intents.all()
intents.members = True
command_prefix = ';'

client = commands.Bot(command_prefix=command_prefix, intents=intents)


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    print(command_prefix)

async def on_message(self, message):
    if message.author == client.user:
        return

testServerID= 1021462844803387423

@client.slash_command(name="hello", description="Bot Says Hello")
async def hellocommand(interaction : Interaction):
    await interaction.response.send_message("Helloooo")

@client.slash_command(name="randomagenttest", description="random agent generator", guild_ids=[testServerID])
async def agentrdm(interaction : Interaction):
    await interaction.channel.send("Random Agent", files=[nextcord.File(random.choice(agentpics))])
    await interaction.response.send_message("Hier ist dein Random Agent")

@client.slash_command(name="randomweapon", description="random weapon generator")
async def weaponrdm(interaction: Interaction):
    await interaction.response.send_message("Your random generated Weapon")
    await interaction.channel.send(files=[nextcord.File(random.choice(weaponpics))])


@client.slash_command(name="randomagent", description="random agent generator")
async def agentrdm(interaction : Interaction):
    embed = nextcord.Embed(
        title="Agent",
        colour=randint(0, 16777214),
        timestamp=datetime.datetime.utcnow()
    )
    embed.set_image(url=random.choice(agentpicsurl))
    await interaction.response.send_message("Your random generated Agent")
    await interaction.channel.send(embed=embed)


@client.slash_command(name="randomteam", description="generates random teams, still in development")
async def teamrdm(interaction : Interaction):
    embed = nextcord.Embed(
        title="Agents for Players",
        colour=randint(0, 16777214),
        timestamp=datetime.datetime.utcnow()
    )
    embed.add_field(
        name="Agent 1:",
        value=random.choice(agentnames)
    )
    embed.add_field(
        name="Agent 2:",
        value=random.choice(agentnames)
    )
    embed.add_field(
        name="Agent 3:",
        value=random.choice(agentnames)
    )
    embed.add_field(
        name="Agent 4:",
        value=random.choice(agentnames)
    )
    embed.add_field(
        name="Agent 5:",
        value=random.choice(agentnames)
    )
    await interaction.response.send_message("Your random Team")
    await interaction.channel.send(embed=embed)


@client.slash_command(name="guessmymain", description="the bot guesses your main")
async def agentmainrdm(interaction : Interaction):
    embed = nextcord.Embed(
        title="Agent",
        colour=randint(0, 16777214),
        timestamp=datetime.datetime.utcnow()
    )
    embed.set_image(url=random.choice(agentpicsurl))
    await interaction.response.send_message("You look like you would main: ")
    await interaction.channel.send(embed=embed)


@client.slash_command(name="help", description="overview for the commands")
async def help(interaction : Interaction):
    embed = nextcord.Embed(
        title="Commands",
        colour=randint(0, 16777214),
        timestamp = datetime.datetime.utcnow()
    )
    embed.add_field(
        name="Randomizers: ",
        value="randomagent\n randomteam\n randomweapon"
    )
    embed.add_field(
        name="GuessYour: ",
        value="guessmymain"
    )
    embed.add_field(
        name="Hello: ",
        value="hello"
    )
    await interaction.response.send_message("All the commands i've done so far: ")
    await interaction.channel.send(embed=embed)

client.run(TOKEN)