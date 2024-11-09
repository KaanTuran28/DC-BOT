import discord
from discord.ext import commands

# Botunuzun token'ını buraya yapıştırın
TOKEN = 'token'

# Intents'i tanımlayın ve gerekli intents'leri etkinleştirin
intents = discord.Intents.default()
intents.members = True  # Sunucu üyeleriyle ilgili olayları alabilmek için

# Botun komut prefix'ini belirleyin (örneğin, ! veya ?)
bot = commands.Bot(command_prefix='!', intents=intents)

# Bot başlatıldığında çalışacak olay
@bot.event
async def on_ready():
    print(f'{bot.user.name} olarak giriş yapıldı!')
    await bot.change_presence(activity=discord.Game(name="Müzik Botu"))

    # Sunucu ID'sini girin
    guild_id =id
    # Kullanıcı adını girin
    username = "name"
    # Verilecek rol adını girin
    role_name = "rol"

    # Sunucuyu alın
    guild = bot.get_guild(guild_id)
    if guild is None:
        print(f"Sunucu {guild_id} bulunamadı.")
        return

    # Kullanıcıyı bul
    user = discord.utils.find(lambda m: m.name == username, guild.members)
    if user is None:
        print(f"Kullanıcı {username} bulunamadı.")
        return

    # Rolü bulun
    role = discord.utils.get(guild.roles, name=role_name)
    if role is None:
        print(f"Rol {role_name} bulunamadı.")
        return

    # Kullanıcıya rolü ekle
    await user.add_roles(role)
    print(f"{role_name} rolü {user.name} kullanıcısına verildi.")

# Botu çalıştır
bot.run(TOKEN)
