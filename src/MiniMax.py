class MiniMax:
	def __init__(self, worldLogic, maxDepth, maximizingPlayer):
		self.worldLogic = worldLogic
		self.maxDepth = maxDepth
		self.maximizingPlayer = maximizingPlayer

	def getBestMove(self, worldState):
		if worldState.getPlayer() != self.maximizingPlayer:
			raise Exception("Invalid player")
		candidate = None
		legalMoves = self.worldLogic.getLegalMoves(worldState)
		for move in legalMoves:
			newState = self.worldLogic.getNewState(worldState, move)
			value = self.__getValue(newState, self.maxDepth, newState.getPlayer())
			if candidate is None or value > candidate[0]:
				candidate = (value, move)
		return candidate[1]

	def __getValue(self, worldState, depth, maximizingPlayer):
		if depth == 0 or self.worldLogic.isTerminal(worldState):
			return worldState.getUtility(self.maximizingPlayer)
		if maximizingPlayer == self.maximizingPlayer:
			value = float('-inf')
			for move in self.worldLogic.getLegalMoves(worldState):
				newState = self.worldLogic.getNewState(worldState, move)
				assert newState.getPlayer() != worldState.getPlayer()
				value = max(value, self.__getValue(newState, depth - 1, newState.getPlayer()))
			return value
		else:
			value = float('inf')
			for move in self.worldLogic.getLegalMoves(worldState):
				newState = self.worldLogic.getNewState(worldState, move)
				assert newState.getPlayer() != worldState.getPlayer()
				value = min(value, self.__getValue(newState, depth - 1, newState.getPlayer()))
			return value

