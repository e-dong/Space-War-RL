
.PHONY: game dev prod

# User CLI Targets
# Default target
game:
	venv/bin/python -m game.main

########################################################
# Dependencies
########################################################

dev: venv/dev_installed
prod: venv/wheel_installed

# venv setup and requirements.txt installed
venv/venv_created: requirements.txt
	test -d venv || python -m venv venv
	touch venv/venv_created

# Install requirements.txt to venv
venv/dev_installed: venv/venv_created requirements-dev.txt setup.py
	venv/bin/pip install -e .[dev]
	touch venv/dev_installed

# Install the wheel in "production"
venv/wheel_installed: venv/venv_created setup.py game/**.py game/assets/**
	venv/bin/pip install .[build]
	touch venv/wheel_installed
	
clean:
	git clean -fdx

########################################################
# Development
########################################################
format: dev
	venv/bin/black --line-length 80 game/**.py

lint: dev
	venv/bin/pylint game/**.py
	venv/bin/flake8 game/**.py
	venv/bin/isort game/**.py
