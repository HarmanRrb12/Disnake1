import disnake

test_embed = disnake.Embed(
    title="Embed",
    description="Тестовый ембед",
    colour=disnake.Colour.from_rgb(48, 227, 20))
test_embed.set_author(
    name="HarmanRrb12",
    icon_url="https://cdn.discordapp.com/avatars/925746440163172373/26f89a374fd1faa905c58b689cdfda91.png?size=1024",
    url="https://youtube.com/@harmanrrb12")

test_embed.set_thumbnail(
    url="https://cdn.discordapp.com/attachments/1137625198124875929/1137627440815030342/a8ecc41ca2de8b53.jpg")
test_embed.set_footer(
    text="06/08/2023 9:03")
test_embed.set_image(
    url="https://cdn.discordapp.com/attachments/1137625198124875929/1138007285801689138/64043b1697f0ea29.jpg")
test_embed.add_field(
    name="Field 1",
    value="Value 1",
    inline=True)
test_embed.add_field(
    name="Field 2",
    value="Value 2",
    inline=True)
test_embed.add_field(
    name="Field 3",
    value="Value 3",
    inline=False)