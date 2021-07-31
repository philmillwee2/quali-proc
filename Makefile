.ONESHELL:

clean:
	rm -rfv .pytest_cache .venv results.egg-info **/*.pyc **/*.pyo **/__pycache__

ACTIVATE_PATH = .venv/bin/activate
setup:
	virtualenv .venv
	. .venv/bin/activate
	pip install -r requirements.txt
	pip install e .
