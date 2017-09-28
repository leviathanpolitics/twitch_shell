from twitchapi import TwitchAPI

class TwitchCalls(TwitchAPI):

	def __init__(self):
		super(TwitchCalls, self).__init__()
		self.response = self._request_get
		self.user_id = self._username_to_userid()

	def _username_to_userid(self, users='ktimekiller'):
		response = self.response('kraken/users?login=%s' % users)
		
		user, = response['users']
		user_id = user['_id']

		return user_id

	def _userid_to_username(self, users):
		try:
			users_parsed = ''
			for x in users:
				x = str(x)
				if x == str(users[0]):
					users_parsed = users_parsed + 'id=' + x
				else:
					users_parsed = users_parsed + '&id=' + x
		except:
			users_parsed = users

		response = self.response('helix/users?%s' % users_parsed)
		
		users = response['data']
		usernames = list(map(lambda x: x['display_name'], users))

		return usernames

	def _game_name_to_game_id(self, ):

	def get_user_stat(self, user):
		response = self.response('kraken/users?login=%s' % user)

		user = response['users']

		return user

	def get_streams(self, usernames=None, games=None):
		if usernames:
			usernames_parsed = ''
			for username in usernames:
				usernames_parsed = usernames_parsed + '&user_login=' + username
		if games:
			games_parsed = ''
			for game in games:
				games_parsed = games_parsed + '&game_id'
		response = self.response('helix/streams?first=20%s%s' % usernames % games)


	def get_my_online_follows(self):
		response = self.response('helix/users/follows?from_id= %s' % self.user_id)

		follows_list = response['data']
		follows_ids = list(map(lambda x: x['to_id'], follows_list))
		user = self._userid_to_username(follows_ids)
		return user