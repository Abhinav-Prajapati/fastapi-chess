import chess
import chess.engine
Engine_path='Chess/stockfish-ubuntu-x86-64-avx2'

class Engine():
    def __init__(self,thinking_timeout=0.1):
        self.engine = chess.engine.SimpleEngine.popen_uci(Engine_path)
        self.Think_timeout = thinking_timeout

    def get_engine_move(self,board):
        result = self.engine.play(board, chess.engine.Limit(time= self.Think_timeout))
        return result.move

    def quit(self):
        self.engine.quit()
