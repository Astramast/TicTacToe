class WorldState():
	def __init__(self, board, player, winner):
		self.player = player
		self.winner = winner
		self.finished = winner is not None or board.isFull()
		self.board = board

	def getBoard(self):
		return self.board

	def getPlayer(self):
		return self.player

	def getWinner(self):
		return self.winner

	def getUtility(self, player):
		if not self.finished:
			return 0
		if self.winner == None:
			return 0
		if self.winner == player:
			return 1
		return -1

	def isTerminal(self):
		return self.finished

	def __str__(self):
		return f"Current Player : {self.player}\nBoard :\n{self.board}"

