import settings
import characters
import discord
from discord.ext import commands
from discord import app_commands


logger = settings.logging.getLogger("bot")

def run():
    intents = discord.Intents.all()

    bot = commands.Bot(command_prefix="!", intents=intents)
    
    @bot.event
    async def on_ready():
        logger.info(f"User: {bot.user} (ID: {bot.user.id})")
        logger.info(f"Guild ID: {bot.guilds[0].id}")

        bot.tree.copy_global_to(guild=settings.GUILD_ID)
        await bot.tree.sync(guild=settings.GUILD_ID)

    @bot.tree.command(name='sync', description='dev testing')
    async def sync(interaction: discord.Interaction):
        if interaction.user.id == 269601375715983380:
            await bot.tree.sync(guild=settings.GUILD_ID)
            print('Command tree synced')
        else:
            await interaction.response.send_message('dev testing')

           
    @bot.tree.command(name="glyph", description="glyph optimization")
    @app_commands.choices(slot=[
        app_commands.Choice(name="1", value="1"),
        app_commands.Choice(name="2", value="2"),
        app_commands.Choice(name="3", value="3"),
        app_commands.Choice(name="4", value="4"),
        app_commands.Choice(name="5", value="5"),
        app_commands.Choice(name="6", value="6")
    ])
    @app_commands.choices(primary=[
        app_commands.Choice(name="Health", value="health"),        
        app_commands.Choice(name="Damage", value="damage"),
        app_commands.Choice(name="Focus", value="focus"),
        app_commands.Choice(name="Armor", value="armor"),
        app_commands.Choice(name="Resistance", value="resistance"),
    ])
    @app_commands.choices(stat1=[
        app_commands.Choice(name="Health", value="hp"),
        app_commands.Choice(name="Damage", value="dmg"),
        app_commands.Choice(name="Speed", value="spd"),
        app_commands.Choice(name="Armor", value="arm"),
        app_commands.Choice(name="Focus", value="foc"),
        app_commands.Choice(name="Resistance", value="res"),
        app_commands.Choice(name="Crit Chance", value="cc"),
        app_commands.Choice(name="Crit Damage", value="cd"),
        app_commands.Choice(name="Block Chance", value="bc"),
        app_commands.Choice(name="Block Mitigation", value="bm"),
    ])
    @app_commands.choices(stat2=[
        app_commands.Choice(name="Health", value="hp"),
        app_commands.Choice(name="Damage", value="dmg"),
        app_commands.Choice(name="Speed", value="spd"),
        app_commands.Choice(name="Armor", value="arm"),
        app_commands.Choice(name="Focus", value="foc"),
        app_commands.Choice(name="Resistance", value="res"),
        app_commands.Choice(name="Crit Chance", value="cc"),
        app_commands.Choice(name="Crit Damage", value="cd"),
        app_commands.Choice(name="Block Chance", value="bc"),
        app_commands.Choice(name="Block Mitigation", value="bm"),
    ])
    @app_commands.choices(stat3=[
        app_commands.Choice(name="Health", value="hp"),
        app_commands.Choice(name="Damage", value="dmg"),
        app_commands.Choice(name="Speed", value="spd"),
        app_commands.Choice(name="Armor", value="arm"),
        app_commands.Choice(name="Focus", value="foc"),
        app_commands.Choice(name="Resistance", value="res"),
        app_commands.Choice(name="Crit Chance", value="cc"),
        app_commands.Choice(name="Crit Damage", value="cd"),
        app_commands.Choice(name="Block Chance", value="bc"),
        app_commands.Choice(name="Block Mitigation", value="bm"),
    ])
    @app_commands.choices(stat4=[
        app_commands.Choice(name="Health", value="hp"),
        app_commands.Choice(name="Damage", value="dmg"),
        app_commands.Choice(name="Speed", value="spd"),
        app_commands.Choice(name="Armor", value="arm"),
        app_commands.Choice(name="Focus", value="foc"),
        app_commands.Choice(name="Resistance", value="res"),
        app_commands.Choice(name="Crit Chance", value="cc"),
        app_commands.Choice(name="Crit Damage", value="cd"),
        app_commands.Choice(name="Block Chance", value="bc"),
        app_commands.Choice(name="Block Mitigation", value="bm"),
    ])
    async def glyph(interaction:discord.Interaction, slot:app_commands.Choice[str], primary:app_commands.Choice[str], stat1:app_commands.Choice[str], stat2:app_commands.Choice[str], stat3:app_commands.Choice[str], stat4:app_commands.Choice[str]):
        
        good = []
        best = []
        input_stat_list = [ stat1.value,stat2.value,stat3.value,stat4.value ]

        for names in characters.dataBox:
            stat_count = 0
            char_stat_list = [names.sec1, names.sec2, names.sec3, names.sec4 ]
            
            if int(slot.value) <=3:
                for stat in input_stat_list:
                    if char_stat_list.count(stat) == 1:
                        stat_count += 1
           
                if stat_count == 4:
                    best.append(names.name.title())
                elif stat_count == 3:
                    good.append(names.name.title())
            elif int(slot.value) >= 4:
                if primary.value in (names.pri1, names.pri2, names.pri3):
                    for stat in input_stat_list:
                        if char_stat_list.count(stat) == 1:
                            stat_count += 1
                    if stat_count == 3:
                        good.append(names.name.title())
                    if stat_count == 4:
                        best.append(names.name.title())
        
        message = (f"Slot {slot.name}, {primary.name} primary, {stat1.value}/{stat2.value}/{stat3.value}/{stat4.value}\n____________________________________\n")
        if len(best) > 0:
            message += (f"\nBest match: {", ".join(best)}\n ")
        if len(good) > 0:
            message += (f"\nBest of 3 stats: {", ".join(good)}")

        else:
            message += ("\nNo matches") 

        await interaction.response.send_message(message, ephemeral=True)

    
        

    bot.run(settings.BOT_SECRET, root_logger=True)

if __name__ == "__main__":    
    run()