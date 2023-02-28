init:
	pip install -r requirements.txt

run:
	newrelic-admin run-program python main.py
