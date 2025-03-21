class MiniMax:
	def __init__(self, maxDepth, maximizingPlayer):
		self.maxDepth = maxDepth
		self.maximizingPlayer = maximizingPlayer

	def getMove(self, worldState, depth, maximizingPlayer):
		if depth == 0 or worldState.isTerminal():
			return worldState.getUtility(maximizingPlayer)
		if maximizingPlayer == self.maximizingPlayer:
			return self.__getValue(worldState, depth, float('-inf'), max)
		else:
			return self.__getValue(worldState, depth, float('inf'), min)

	def __getValue(self, worldState, depth, value, function):
		for move in worldState.getLegalMoves():
			newState = worldState.getNewState(move)
			value = function(value, self.getMove(worldState, depth - 1, worldState.getPlayer()))
		return value

