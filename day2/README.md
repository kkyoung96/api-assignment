cd flaskapi

docker build -t myflaskapi:v2 .

docker run -d -it --rm -p 5000:5000 --name flaskapi myflaskapi:v2



[ mysql 임시 ]

docker build -t cent7-mysql:v5.7 .

docker run -it -d --rm --name mysql -e MYSQL_ROOT_PASSWORD=1234 -p 3306:3306 cent7-mysql:v5.7
