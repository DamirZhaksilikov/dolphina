# To run the micro-service:
docker build --tag dolphina .  
docker run -d -p 5000:5000 dolphina

--> Then open browser and visit: http://localhost:5000/picture  <--

# To run test
pipenv shell
pip install -r requirements.txt   
python3 -m pytest