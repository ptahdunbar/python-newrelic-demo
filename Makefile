init:
	pip install -r requirements.txt
	[ ! -f .env ] && cp .env.example .env

run:
	newrelic-admin run-program python main.py
