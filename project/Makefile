init:
	pip install -r ../requirements.txt

serve:
	uvicorn app.main:app --host 0.0.0.0 --port 8080 --reload

run:
	python -m gui.main

build:
	sudo docker build -t cdio ..

deploy:
	sudo docker login
	sudo docker build -t martinmaartensson/cdio ..
	sudo docker push martinmaartensson/cdio

test-game:
	python -m unittest tests.test_game > test_output.txt

test-core:
	python -m unittest tests.test_core > test_output.txt
