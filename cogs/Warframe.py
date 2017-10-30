from discord.ext import commands
import discord
import sqlite3


class Warframe:
    def __init__(self, bot):
        self.bot = bot

    @commands.group(pass_context=True)
    async def warframe(self, ctx):
        if ctx.invoked_subcommand is None:
            await self.bot.say("add a subcommand : show, add, remove")

    @warframe.command(name="show", hidden=False)
    async def show_list(self, target: discord.Member=None):
        if target is None:
            await self.bot.say("no member given.")
        else:
            conn = sqlite3.connect("discord.db")
            args = (target.id, )
            msgembed = discord.Embed(name="{} Missing Items".format(target.id))
            msgembed.description = "Missing Items for {}".format(target.name)
            msgembed.color = target.color
            cur = conn.cursor()
            cur.execute("SELECT item, components FROM Wishlists WHERE ID=?",
                        args)
            queryret = cur.fetchall()
            prev = None
            gather = {}
            for row in queryret:
                if prev != row[0]:
                    gather[row[0]] = []
                    prev = row[0]
                gather[row[0]].append(row[1])
            for item in gather.keys():
                msgembed.add_field(
                    name="{}".format(item),
                    value=", ".join(gather[item]),
                    inline=False)
            conn.close()
            await self.bot.say(embed=msgembed)

    @warframe.command(name="add", pass_context=True)
    async def add_to_list(self,
                          ctx,
                          item: str=None,
                          component: str=None):
        if item is None or component is None:
            await self.bot.say("An element is missing for the item")
            return
        conn = sqlite3.connect("discord.db")
        cur = conn.cursor()
        try:
            cur.execute("INSERT INTO Wishlists VALUES (?,?,?)",
                        (ctx.message.author.id, item, component))
            conn.commit()
            conn.close()
            await self.bot.say("{}, {}, {} was added to the database".format(
                ctx.message.author.name, item, component))
        except:
            await self.bot.say("could not add the item to the database.")
        return

    @warframe.command(name="remove", pass_context=True)
    async def remove_from_list(self, ctx, item: str=None, component: str=None):
        conn = sqlite3.connect("discord.db")
        cur = conn.cursor()
        try:
            cur.execute(
                "DELETE FROM Wishlists WHERE ID=? AND ITEM=? AND COMPONENTS=?",
                (ctx.message.author.id, item, component))
            conn.commit()
            conn.close()
            await self.bot.say("Removed {0.name},{1},{2} from the database".
                               format(ctx.message.author, item, component))
        except:
            await self.bot.say("There is some information missing")
        return


def setup(bot):
    bot.add_cog(Warframe(bot))