from WorldState import WorldState

class WorldLogic:
	def __init__(self):
		pass

	def isTerminal(self, state):
		return state.isTerminal()

	def getLegalMoves(self, state):
		board = state.getBoard()
		legalMoves = []
		for i in range(3):
			for j in range(3):
				if board.get(i, j) is None:
					legalMoves.append((i, j))
		return legalMoves

	def getNewState(self, state, move):
		legalMoves = self.getLegalMoves(state)
		if move not in legalMoves:
			raise Exception(f"Invalid move: {move} on state: {state}")
		newBoard = state.getBoard().copy()
		newBoard.set(move, state.getPlayer())
		return WorldState(newBoard, 0 if state.getPlayer() == 1 else 1, newBoard.getWinner())

