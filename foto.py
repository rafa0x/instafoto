import instaloader

#Carrega a classe principal da lib
bot = instaloader.Instaloader()

#Define perfil do insta que deseja baixar a foto
username = "instagram"

#Baixa os dados do perfil do insta
print(bot.download_profile(username, profile_pic_only=True))