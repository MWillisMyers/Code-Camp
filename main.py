


music = {
	'song1': 0,
	'song2': 0,
	'song3': 0,
	'song4': 0,
	'song5': 0,
	'song6': 0,
	'song7': 0,
	'song8': 0,
	'song9': 0,
}

def upVote():
	user = raw_input("What song would you like to up vote? ").lower()
	if user in music:
		music[user] += 1
		print music[user]
	else:
		print "That song doesn't exist"

def downVote():
	user = raw_input("What song would you like to down vote? ").lower()
	if user in music:
		music[user] -= 1
		print music[user]
	else:
		print "That song doesn't exist"

def checkSong():
	user = raw_input("What song would you like to check? ").lower()
	if user in music:
		print music[user]
	else:
		print "That song doesn't exist"

def listSong():
	songs = list(music)
	for s in songs:
		print s

def addSong():
	user = raw_input("What song would you like to add? ").lower()
	music.update({user: 0})

choices = {
	'up vote': upVote,
	'down vote': downVote,
	'check song': checkSong,
	'add song': addSong,
	'list songs': listSong,
}

def action():
	user = raw_input("What would you like to do? ").lower()
	if user in choices:
		choices[user]()
	else:
		print "That is not a valid choice"
		print ''

while True:
	action()