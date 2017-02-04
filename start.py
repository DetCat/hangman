import yaml
from hangman.game import Game


def get_config():
    with open("words.yml", "r", encoding="utf8") as file:
        return yaml.load(file.read())


def main():
    Game(7, get_config()["Words"])
    return 0


if __name__ == "__main__":
    exit(main())
