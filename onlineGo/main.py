import asyncio
import json
import string

import requests
from websockets.client import connect

from configuration import sessionid

api = {
    "me": "/api/v1/me",
    "mygames": "/api/v1/megames",
    "active_games": "/api/v1/ui/overview",
    "get_game": "/api/v1/games/{}",
    "set_stone": "/api/v1/game/move",
    "get_jwt": "/api/v1/ui/config",
}

cookie = {
    "sessionid": sessionid,
}


def get_games():
    return requests.get("https://online-go.com" + api["active_games"], cookies=cookie).json()["active_games"]


def get_game_stones(id: str):
    game = requests.get("https://online-go.com" + api["get_game"].format(id), cookies=cookie).json()
    return game["gamedata"]["moves"]


def get_jwt():
    return requests.get("https://online-go.com" + api["get_jwt"], cookies=cookie).json()["user_jwt"]


async def set_stone(id: int, move: (int, int), jwt):
    async with connect("wss://online-go.com/") as ws:
        await ws.send(json.dumps(
            ["ui-pushes/subscribe", {"channel": f"game-{id}"}]
        ))
        await ws.send(json.dumps(
            ["game/connect", {"game_id": id, "chat": False}]
        ))
        await ws.send(json.dumps(["authenticate", {"jwt": jwt}]))
        await ws.send(json.dumps(
            ["net/ping", {"client": 1728990454383, "drift": 0, "latency": 0}]
        ))

        while True:
            message = await ws.recv()
            message = json.loads(message)
            if message[0] == "net/pong":
                break

        await ws.send(json.dumps(
            ["game/move", dict(game_id=id, move=string.ascii_lowercase[move[0]] + string.ascii_lowercase[move[1]])]
        ))


async def main():
    jwt = get_jwt()
    print(await set_stone(68661815, (1, 1), jwt))


if __name__ == '__main__':
    asyncio.run(main())
