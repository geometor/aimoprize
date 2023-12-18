"""
run the main app
"""
from .aimoprize import Aimoprize


def run() -> None:
    reply = Aimoprize().run()
    print(reply)
