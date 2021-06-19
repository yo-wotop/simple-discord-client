from discordrestclient import DiscordRestClient


def main():
    endpoint = 'http://[YOUR_ENDPOINT_HERE]'
    file = 'discord_info.json'
    disc = DiscordRestClient(endpoint, file)

    guild = disc.guilds['[YOUR_GUILD_HERE]']  # Guild name is based on the key in 'discord_info.json'
    channel = guild.channels['[YOUR_CHANNEL_HERE]']  # Channel name is based on the key in 'discord_info.json'
    message = 'Hello Channel World'
    disc.send(guild, channel, message)

    me = disc.users['[YOUR_USERNAME_HERE]']  # User name is based on the key in 'discord_info.json'
    message = 'Hello DM World'
    disc.dm(me, message)



if __name__ == '__main__':
    main()
