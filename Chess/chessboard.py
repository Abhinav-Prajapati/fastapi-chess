import chess

class ChessBoard:
    def __init__(self,game_uid,white,black) -> None:
        self.Game_uid= game_uid
        self.Board = chess.Board()
        self.White = white 
        self.Balck = black 

    def move(self,move):
        move_ = chess.Move.from_uci(move) 
        if move_ in self.Board.legal_moves:
            self.Board.push(move_)
            return True
        return False
        
    def undo_move(self):
        self.Board.pop()  # Unmake the last move

    def game_state(self):
        state = {
            'turn':self.Board.turn,
            'check':self.Board.is_check(),
            'checkmate':self.Board.is_checkmate(),
            'stalemate':self.Board.is_stalemate(),
            'insufficient_material':self.Board.is_insufficient_material(),
            'repetition':self.Board.is_repetition(count = 3),
            'winner': self.Board.outcome().winner if self.Board.outcome() else None,
            'outcome': self.Board.outcome().termination if self.Board.outcome() else None,
            'fen':self.Board.fen()
        }
        return state
        # board.is_attacked_by(chess.WHITE, chess.E8)

    def get_board(self):
        return self.Board

    def log_debug_info(self):
        print(f'White {self.White} Black {self.Balck}')
        print(f'{ "White" if self.Board.turn else "Black" } to move')
        print()
        print(self.Board)
        print()
        print(self.game_state())

    def set_fen(self,fen):
        self.Board=chess.Board(fen)


# game_1 = new_computer_game()
# game_2 = new_computer_game()
# Ongoing_game[game_1].move('e2e4')
# Ongoing_game[game_2].move('e2e3')
# print(Ongoing_game[game_1].get_board())
# print(Ongoing_game[game_2].get_board())


