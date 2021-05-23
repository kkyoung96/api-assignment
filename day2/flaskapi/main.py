from flask import Flask, request
import mysql.connector
import env

app = Flask(__name__)

@app.get("/")
def root():
    return { "hello": "this is index" }

@app.route('/userinfo')
def userinfo():
    parameter_dict = request.args.to_dict()
    if len(parameter_dict) == 0:
        return "전달된 파라미터가 없습니다."

    parameters = ''
    for key in parameter_dict.keys():
        try:
            mydb = mysql.connector.connect(
            host=(env.MYSQL_HOST),
            user=(env.MYSQL_USER),
            passwd=(env.MYSQL_ROOT_PASSWORD),
            database=(env.MYSQL_DATABASE)
        )
            mycursor = mydb.cursor()
            mycursor.execute("SELECT * FROM userinfo where name='" + key + "'")
            myresult = mycursor.fetchall()
        except mysql.connector.errors.InterfaceError as err:
            return "DB 연결 확인 필요"
        except mysql.connector.errors.ProgrammingError as err:
            return "테이블 확인 필요"
        if str(len(myresult)) == str(0)  :
            return "해당 사용자는 없습니다."
        return str(myresult)

@app.get("/healthcheck")
def healthcheck():
    return {"health":"green"}

if __name__ == '__main__':
    app.run(host='0.0.0.0')
#    app.run(host='0.0.0.0',debug=True)
