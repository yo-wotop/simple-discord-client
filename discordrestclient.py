import json
import requests
from guild import Guild


class DiscordRestClient:
    guilds = None
    users = None

    def __init__(self, server, info_file=None):
        self.server = server
        if info_file is not None:
            with open(info_file, 'r') as f:
                self.process_info(json.load(f))

    def process_info(self, info):
        if info.get('guilds'):
            self.guilds = dict()
            for guild_name, guild_info in info['guilds'].items():
                guild = Guild(guild_name, guild_info)
                self.guilds[guild_name] = guild

        if info.get('users'):
            self.users = dict()
            for user_name, user_id in info['users'].items():
                self.users[user_name] = user_id

    def send(self, guild, channel_id, message):
        if type(guild) == Guild:
            guild = guild.id

        url = self.server + '/chat'
        body = {
            'server': guild,
            'channel': channel_id,
            'text': message
        }
        requests.post(url, json=body)

    def dm(self, user_id, message):
        url = self.server + '/dm'
        body = {
            'recipient': user_id,
            'text': message
        }
        requests.post(url, json=body)

