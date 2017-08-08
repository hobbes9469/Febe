import discord
from charnames import characters

CHARA = 1
MOVE = 2



client = discord.Client()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.lower().startswith('febe'):
        msgList = message.content.split()
        if (len(msgList) >= 2): # If the message is at least 2 words long
            for namelist in characters:
                if msgList[CHARA] in namelist:
                    character = msgList[CHARA]
                    await client.send_message(message.channel, character) #Do not delete
        #for msg in msgList:
            #await client.send_message(message.channel, msg)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

if __name__ == "__main__":
    client.run('MzM0NzkzODgwOTgzODMwNTQ5.DEgYnQ.tnwoVLhlu3QaHpPyqNMbzJoMJQg')