# To run the micro-service:
docker build --tag dolphina .  
docker run -d -p 5000:5000 dolphina

--> Then open browser and visit: http://localhost:5000/picture  <--

# To run test
pipenv run python3 -m pytest