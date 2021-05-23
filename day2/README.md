cd flaskapi

docker build -t myflaskapi:v2 .

docker run -d -it --rm -p 5000:5000 --name flaskapi myflaskapi:v2
