all: build run run_tests

build:
	bash setup.sh

activate:
	bash venv/bin/activate

run: activate
	python3 dice_game.py

run_tests: activate
	python3 -m unittest test.test_game

run_api: activate
	python3 dice_game_api.py

run_api_tests: activate
	python3 -m unittest test.test_game_api


run_extras: activate
	python3 extras.py
