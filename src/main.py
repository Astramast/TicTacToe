from WorldState import WorldState
from Board import Board
from MiniMax import MiniMax
from WorldLogic import WorldLogic


def getInput(worldLogic, worldState):
	moves = worldLogic.getLegalMoves(worldState)
	while True:
		move = input("Enter move [0-8]: ")
		if move.isnumeric() and int(move) in range(9):
			move = int(move)
			move = (move // 3, move % 3)
			if move in moves:
				return move
		print("Invalid move.")

def main():
	rules = WorldLogic()
	ai = MiniMax(rules, 5, 1)
	game = WorldState(Board(), 0, None)
	while not game.isTerminal():
		print(game)
		move = None
		if game.getPlayer() == 0:
			move = getInput(rules, game)
		else:
			move = ai.getBestMove(game)
			print(f"AI move: {move}")
		game = rules.getNewState(game, move)
	print(game)
	print(f"Game over. {game.getWinner()} won.")


if __name__ == "__main__":
	main()

