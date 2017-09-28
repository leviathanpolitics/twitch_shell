from cmd import Cmd
from twitchcmd import TwitchCalls

class Prompts(Cmd):

	def __init__(self):
		Cmd.__init__(self)
		self.prompt = '> '
		self.intro = 'welcome'

	def do_user_stat(self, user='ktimekiller'):
		"""shows a users stat. defaults to me"""
		response = TwitchCalls()
		print response.get_user_stat(user)

	def do_my_online_follows(self, args):
		"""shows my online follows"""
		response = TwitchCalls()
		print response.get_my_online_follows()

	def do_exit(self, args):
		"""exits"""
		return -1

prompt = Prompts()
prompt.cmdloop()