from cmd import Cmd
from twitchcmd import TwitchCalls

class Prompts(Cmd):

	def __init__(self):
		Cmd.__init__(self)
		self.prompt = '> '
		self.intro = 'welcome'

	def do_user_stat(self, user):
		"""shows a users stat."""
		response = TwitchCalls()
		result = response.get_user_stat(user)
		for user_dict in result:
			for stat_key in user_dict:
				print stat_key + ': ' + str(user_dict[stat_key]) + '\n'

	def do_my_online_follows(self, args):
		"""shows my online follows"""
		response = TwitchCalls()
		result = response.get_my_online_follows()
		for user in result:
			print user + '\n'

	def do_exit(self, args):
		"""exits"""
		return -1

prompt = Prompts()
prompt.cmdloop()