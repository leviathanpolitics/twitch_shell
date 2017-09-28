from cmd import Cmd
from twitchapi import TwitchApi

class Prompts(Cmd):

	def __init__(self):
		Cmd.__init__(self)
		self.prompt = '> '
		self.intro = 'welcome'



	def do_exit(self, args):
		"""exits"""
		return -1

prompt = Prompts()
prompt.cmdloop()