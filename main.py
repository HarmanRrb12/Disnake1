from config import bot_token
import disnake
from disnake.ext import commands
import embeds
import buttons

bot = commands.Bot(command_prefix="!")

@bot.slash_command(name="embed", description="Отправляет Embed с кнопками")
async def embed(inter: disnake.ApplicationCommandInteraction):
    await inter.response.send_message(embed=embeds.test_embed, components=[buttons.action_row])

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}({bot.user.id})\n-----------------------------')

@bot.event
async def on_button_click(inter: disnake.MessageInteraction):
    if inter.component.custom_id == 'button1':
        await inter.response.send_message('Вы нажали на первую кнопку!', ephemeral=True)
    elif inter.component.custom_id == 'button2':
        await inter.response.send_message('Вы нажали на вторую кнопку!', ephemeral=True)
    elif inter.component.custom_id == 'button3':
        await inter.response.send_message('Вы нажали на третью кнопку!', ephemeral=True)
    elif inter.component.custom_id == 'button4':
        await inter.response.send_message('Вы нажали на четвёртую кнопку!', ephemeral=True)

bot.run(bot_token)