from configparser import ConfigParser
from pathlib import Path
from datetime import datetime
import sys

class ArkSession:
    def __init__(self, path: str):
        self.parser = ConfigParser()
        self.configpath = path
        self.map = "TheIsland"
        self.servertitle = "Ark Private Server"
        self.gameclientport = "7777"
        self.queryport = "27015"
        self.rconport = "27020"
        self.adminpass = "changethispassword"
        self.password = "changethispassword"
        self.playercount = "25"
        self.difficulty = "1.0"
        self.officialdifficulty = "5.0"
        self.enabled = "False"
        self.difficultyperday = "0.5"
        self.timescalar = "1.0"
        self.difficultystart = "1.0"
        self.difficultymax = "10.0"
        self.reset = "False"
        self.startdate = datetime.now().strftime('%Y-%m-%d %I:%M:%S')

    def save(self):
        self.resetParser()
        self.parser.add_section('session')
        self.parser.set('session', 'map', str(self.map))
        self.parser.set('session', 'servertitle', str(self.servertitle))
        self.parser.set('session', 'gameclientport', str(self.gameclientport))
        self.parser.set('session', 'queryport', str(self.queryport))
        self.parser.set('session', 'rconport', str(self.rconport))
        self.parser.set('session', 'adminpass', str(self.adminpass))
        self.parser.set('session', 'password', str(self.password))
        self.parser.set('session', 'playercount', str(self.playercount))

        self.parser.add_section('difficulty')
        self.parser.set('difficulty', 'difficulty', str(self.difficulty))
        self.parser.set('difficulty', 'officialdifficulty', str(self.officialdifficulty))

        self.parser.add_section('dynamicdifficulty')
        self.parser.set('dynamicdifficulty', 'enabled', str(self.enabled))
        self.parser.set('dynamicdifficulty', 'difficultyperday', str(self.difficultyperday))
        self.parser.set('dynamicdifficulty', 'timescalar', str(self.timescalar))
        self.parser.set('dynamicdifficulty', 'difficultystart', str(self.difficultystart))
        self.parser.set('dynamicdifficulty', 'difficultymax', str(self.difficultymax))
        
        self.parser.add_section('date')
        self.parser.set('date', 'reset', str(self.reset))
        self.parser.set('date', 'startdate', str(self.startdate))

        Path(self.configpath).touch()

        with open(self.configpath, 'w') as configfile:
            self.parser.write(configfile)

    def load(self):
        if Path(self.configpath).is_file():
            self.parser.read(self.configpath)
            self.map = self.parser.get('session', 'map')
            self.servertitle = self.parser.get('session', 'servertitle')
            self.gameclientport = self.parser.get('session', 'gameclientport')
            self.queryport = self.parser.get('session', 'queryport')
            self.rconport = self.parser.get('session', 'rconport')
            self.adminpass = self.parser.get('session', 'adminpass')
            self.password = self.parser.get('session', 'password')
            self.playercount = self.parser.get('session', 'playercount')
            self.difficulty = self.parser.get('difficulty', 'difficulty')
            self.officialdifficulty = self.parser.get('difficulty', 'officialdifficulty')
            self.enabled = self.parser.get('dynamicdifficulty', 'enabled')
            self.difficultyperday = self.parser.get('dynamicdifficulty', 'difficultyperday')
            self.timescalar = self.parser.get('dynamicdifficulty', 'timescalar')
            self.difficultystart = self.parser.get('dynamicdifficulty', 'difficultystart')
            self.difficultymax = self.parser.get('dynamicdifficulty', 'difficultymax')
            self.reset = self.parser.get('date', 'reset')
            self.startdate = self.parser.get('date', 'startdate')

        else:
            print("Configuration file doesn't exist or is unreadable. Creating one now. Modify it before running this script again.")
            self.save()
            sys.exit(0)

    def resetParser(self):
        for section in self.parser.sections():
            for option in self.parser.options(section):
                self.parser.remove_option(section, option)
            self.parser.remove_section(section)

