class Board():
	def __init__(self, matrix=None):
		self.matrix = matrix if matrix is not None else [[None for i in range(3)] for j in range(3)]
		self.winner = None
		self.checkWinner()

	def getWinner(self):
		self.checkWinner()
		return self.winner

	def get(self, x, y):
		return self.matrix[x][y]
	
	def set(self, pos, value):
		self.matrix[pos[0]][pos[1]] = value
		self.checkWinner()

	def copy(self):
		return Board([[self.matrix[i][j] for j in range(3)] for i in range(3)])

	def isFull(self):
		for i in range(3):
			for j in range(3):
				if self.matrix[i][j] is None:
					return False
		return True

	def checkWinner(self):
		for i in range(3):
			if self.matrix[i][0] == self.matrix[i][1] == self.matrix[i][2] and self.matrix[i][0] is not None:
				self.winner = self.matrix[i][0]
		for i in range(3):
			if self.matrix[0][i] == self.matrix[1][i] == self.matrix[2][i] and self.matrix[0][i] is not None:
				self.winner = self.matrix[0][i]
		if self.matrix[0][0] == self.matrix[1][1] == self.matrix[2][2] and self.matrix[0][0] is not None:
			self.winner = self.matrix[0][0]
		if self.matrix[0][2] == self.matrix[1][1] == self.matrix[2][0] and self.matrix[0][2] is not None:
			self.winner = self.matrix[0][2]

	def toString(self, value):
		if value is None:
			return "."
		return str(value)

	def __str__(self):
		stringValues = [[self.toString(self.matrix[i][j]) for j in range(3)] for i in range(3)]
		return f"{stringValues[0][0]}|{stringValues[0][1]}|{stringValues[0][2]}\n-+-+-\n{stringValues[1][0]}|{stringValues[1][1]}|{stringValues[1][2]}\n-+-+-\n{stringValues[2][0]}|{stringValues[2][1]}|{stringValues[2][2]}"

