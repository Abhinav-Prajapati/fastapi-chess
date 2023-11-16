from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from Chess.engine import Engine 
from player.player import engine_move ,  new_computer_game , Ongoing_bot_game

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Hello World"}
 
@app.get("/computer/new-game")
def new_game():
    game_uuid = new_computer_game()
    return {'game_uuid':game_uuid} 

@app.post("/computer/{game_uuid}/move")
def computer_move(data:dict,game_uuid:str):
    Board = Ongoing_bot_game[game_uuid]
    is_move_valid = Board.move(data['move'])
    state = Board.game_state()
    response={"is_valid_move":is_move_valid}
    return response

@app.get("/computer/{game_uuid}/engine-move")
def get_engine_move(game_uuid:str):
    board = Ongoing_bot_game[game_uuid]
    move = engine_move(board.Board) 
    print(f"engine move {move}")
    is_move_valid = board.move(str(move))
    state = board.game_state()
    return {"is_valid_move":True}

@app.get("/computer/{game_uuid}/game-state")
def get_game_state(game_uuid:str):
    board = Ongoing_bot_game[game_uuid]
    return board.game_state()
