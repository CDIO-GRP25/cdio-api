run:
    uvicorn app.main:app --host 0.0.0.0 --port 8080

build:
    sudo docker build -t cdio .

deploy:
    sudo docker build -t martinmaartensson/cdio .

test:
    python -m unittest tests.test_core > test_output.txt