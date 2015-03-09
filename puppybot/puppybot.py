from errbot import BotPlugin, botcmd
from plugins.puppybot.get_puppy import (AVAILABLE_COMMANDS,
                                        PuppyFetch)

class PuppyBot(BotPlugin):

    @property
    def command_list(self):
        return PuppyFetch.get_command_list() 

    @botcmd
    def help(self, msg, args):
        """ Reply with the commands recognized by this bot """
        return ', '.join(self.command_list.keys()) 

    @botcmd(split_args_with=' ')
    def fetch(self, msg, args):
        """ If any words a command, get the command """
        for arg in args:
            if self._is_recognized_cmd(arg):
                return PuppyFetch.get(self.command_list[arg])
            
        return None

    def _is_recognized_cmd(self, arg):
        return arg.lower() in self.command_list.keys()

