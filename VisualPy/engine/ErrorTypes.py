class NoDialogError(Exception):
	"""
	Occurs when the user has not inputted any dialog.
	"""
	pass

class DialogTooBigError(Exception):
	"""
	Occurs when the user has inputted too big of a dialog.
	"""
	pass
class DiscordRPCFailed(Exception):
	"""
	Occurs when pypresence fails to connect to Discord.
	"""
	pass
class DiscordNotFound(Exception):
	"""
	Occurs when pypresence fails to connect to Discord.
	"""
	pass

class InvalidArgument(Exception):
	"""
	Happens when an invalid argument is fed. Eg: int instead of str and str instead of float
	"""
	pass