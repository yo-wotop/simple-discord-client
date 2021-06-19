class Guild:
    def __init__(self, name, info):
        self.name = name
        self.id = info['id']

        if info.get('channels'):
            self.channels = dict()
            for channel_name, channel_id in info['channels'].items():
                self.channels[channel_name] = channel_id
