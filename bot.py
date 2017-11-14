#!/usr/bin/python3
import telebot, ast, re, requests, time

# Cria um bot com a API key disponibilizada pelo BotFather
bot = telebot.TeleBot('token')


@bot.message_handler(commands=['ajuda', 'help'])
def comando_help(message):
    bot.reply_to(message,'''
/link    - Exibe o Link de convite para acesso ao grupo
/regras  - Exibe as regras vigentes no grupo
/ctf     - Exibe o Link do Capture The Flag.
''')        

@bot.message_handler(commands=['regras', 'rules'])
def comando_regras(message):
    bot.reply_to(message,'''

[*] Grupo de discussão sobre Security, Hacks e Afins do Sucuri Hacker Club

## REGRAS ##

======================
[X] NÃO HÁ REGRAS:
Punição: USE O BOM SENSO ;-)

[x] SE APRESENTE AO PESSOAL NOVATOS!!!


''')

@bot.message_handler(commands=['link'])
def comando_link(message):
    bot.reply_to(message,'https://telegram.me/joinchat/BSN28wEk-Ffp2yEXjYgx6Q')
    
@bot.message_handler(commands=['ctf'])
def comando_link(message):
    bot.reply_to(message,'http://ctf.sucurihc.org')

@bot.message_handler(func=lambda mensagem: True, content_types=['new_chat_participant'])
def mensagem(mensagem):
    bot.reply_to(mensagem, '''
Bem Vindo ao Grupo Sucuri Hacker Club no Telegram
Leia as regras antes de postar, envie /regras!!! 
''')    

print('Bot Iniciado')        
bot.polling()
