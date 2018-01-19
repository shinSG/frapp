HOST=0.0.0.0
PORT=5000
DEBUG=false
export FLASK_APP=app.py
export FLASK_DEBUG=$(DEBUG)

init:
	pip install -r requirements.txt

runserver: init
	flask run --host=$(HOST) --port=$(PORT)
