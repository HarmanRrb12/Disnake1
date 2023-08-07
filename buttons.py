import disnake

button1 = disnake.ui.Button(label="Кнопка", style=disnake.ButtonStyle.primary, custom_id="button1")
button2 = disnake.ui.Button(label="Кнопка", style=disnake.ButtonStyle.success, custom_id="button2",
                            emoji="<:hypesquadminecraft:679123600107896862")
button3 = disnake.ui.Button(label="Кнопка", style=disnake.ButtonStyle.danger, custom_id="button3")
button4 = disnake.ui.Button(label="Кнопка", style=disnake.ButtonStyle.secondary, custom_id="button4")
button5 = disnake.ui.Button(label="Кнопка", style=disnake.ButtonStyle.link, url="https://www.iqgaming.site/")

action_row = disnake.ui.ActionRow(button1, button2, button3, button4, button5)