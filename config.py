import json

# create file if not already created with twilio credentials
with open('/etc/etfconfig.json') as config_file:
    config = json.load(config_file)


class Config:

    BOT_TOKEN = config.get('BOT_TOKEN')
