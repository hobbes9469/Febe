import discord
from charnames import characters
from charmoves import charFrames, charNames

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
                lowerName = msgList[CHARA].lower()
                if lowerName in namelist:
                    character = namelist[0]     #First name in namelist is the regular name
                    moveName = " ".join(msgList[MOVE:])  #The rest of the string is the move name
                    await client.send_message(message.channel, character) #Do not delete
                    await client.send_message(message.channel, moveName)
                    fdText = get_frame_data(character, moveName)
                    await client.send_message(message.channel, fdText)

def get_frame_data(character, moveName):
    if character in charNames:
        if moveName in charFrames[character]:
            frameData = charFrames[character][moveName.lower()]
            print(frameData)
            return frameData

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

if __name__ == "__main__":
    tokenFile = open("bt.txt")
    botToken = tokenFile.read()
    client.run(botToken)