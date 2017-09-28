from twitchapi import TwitchAPI

class TwitchCalls(TwitchAPI):

	def __init__(self):
		super(TwitchCalls, self).__init__()
		self.response = self._request_get
		self.user_id = self._get_user_id()

	def _get_user_id(self, users='ktimekiller'):
		response = self.response('kraken/users?login=%s' % users)
		
		user, = response['users']
		user_id = user['_id']

		return user_id

	def _get_user_names(self, users):
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
		return response

	def user_stat(self, user='ktimekiller'):
		response = self.response('kraken/users?login=%s' % user)

		user = response['users']

		return user

	def get_my__online_follows(self):
		response = self.response('helix/users/follows?from_id= %s' % self.user_id)

		follows_list = response['data']
		follows_ids = list(map(lambda x: x['to_id'], follows_list))
		user = self._get_user_names(follows_ids)
		return user

response = TwitchCalls()
print response.get_my__online_follows()