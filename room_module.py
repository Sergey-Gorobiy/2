class WinDoor:
	"""This class creates a window or door"""
	def __init__(self, w, h):
		"""The constructor takes the width and height of the widow/door"""
		self.square = w * h

class Room:
	"""This class creates a room that must be wallpapered"""
	def __init__(self, w, l, h):
		"""The constructor takes the width, lenght, and height of the room"""
		self.width = float (w)
		self.lenght = float (l)
		self.height = float (h)
		self.wd = []

	def addWD(self, w, h):
		"""The method adds an object of WinDoor (window/door)"""
		self.wd.append(WinDoor(w, h))

	def fullSquare (self):
		"""The method calculates the full square of walls"""
		return 2 * self.height * (self.width + self.lenght)

	def workSurface(self):
		"""The method calculates the square of the walls that will be processed"""
		workSurface_square = self.fullSquare()
		for i in self.wd:
			workSurface_square -= i.square
		return workSurface_square

	def numberOfwallpapers (self, w, l):
		"""The method calculates the needed number of wallpapers"""
		return int (self.workSurface() / (w * l)) + 1