class Song(object):
	"""docstring for Song"""
	def __init__(self, lyrics):
		super(Song, self).__init__()
		self.lyrics = lyrics
	
	def sing_me_a_song(self):
		for line in self.lyrics:
			print line

happy_bday=Song(["Happy birthday to you",
				 "I dont want to get sued"])

bulls_on_parade=Song(["They rally around tha family"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()