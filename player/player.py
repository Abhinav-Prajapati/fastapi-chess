import uuid
from Chess.engine import Engine
from Chess.chessboard import ChessBoard
import chess.engine

Engine_path='Chess/stockfish-ubuntu-x86-64-avx2'
Ongoing_bot_game = {}

test_engine = chess.engine.SimpleEngine.popen_uci(Engine_path)

def engine_move(board):
    result = test_engine.play(board, chess.engine.Limit(time = 0.1))
    return result.move

def new_computer_game():
    game_uuid = uuid.uuid4()
    Ongoing_bot_game[str(game_uuid)] = ChessBoard(game_uuid,'Player white','Player black')
    return str(game_uuid)

























# engine_noob = Engine(thinking_timeout=0.01)
# engine_pro = Engine(thinking_timeout=1)

# game_1212 = ChessBoard("a8df2392","pro_engine","noob_engine")


# while not game_1212.get_board().is_game_over():

#     noob_move = engine_noob.get_engine_move(game_1212.get_board())

#     game_1212.move(str(noob_move))
#     game_1212.log_debug_info()

#     pro_move = engine_pro.get_engine_move(game_1212.get_board())

#     game_1212.move(str(pro_move))
#     game_1212.log_debug_info()

# engine_noob.quit()
# engine_pro.quit()

# class Player():
#     def __inint__(self):
#         pass