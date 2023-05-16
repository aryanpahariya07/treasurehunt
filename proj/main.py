from flask import Flask, render_template, request,session,redirect
from flask_mysqldb import MySQL
import time

app = Flask(__name__)
app.secret_key = 'your_secret_key'
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'mysqllock'
app.config['MYSQL_DB'] = 'datab'
mysql = MySQL(app)

start_times = {}


@app.route('/app/')
def home():
    return render_template('index.html')


@app.route('/app/create')
def create():
    return render_template('create.html')


@app.route('/app/start', methods=['GET', 'POST'])
def start():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        session['username'] = username
        cursor = mysql.connection.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS info_table (
                            username VARCHAR(255) PRIMARY KEY,email VARCHAR(255),password VARCHAR(255))""")
        cursor.execute("INSERT INTO info_table (username, email, password) VALUES (%s, %s, %s)",
                       (username, email, password))
        cursor.execute("""CREATE TABLE IF NOT EXISTS game_stat (
                                    username VARCHAR(255),
                                    gameid INT,
                                    time_taken INT,
                                    unsuccessful_attempt INT,
                                    PRIMARY KEY (username, gameid)
                                )""")
        game_id = 1
        time_taken = 0
        unsuccessful_attempt = 0
        cursor.execute(
            "INSERT INTO game_stat (username, gameid, time_taken, unsuccessful_attempt) "
            "VALUES (%s, %s, %s, %s)",
            (username, game_id, time_taken, unsuccessful_attempt))

        game_id = 2
        time_taken = 0
        unsuccessful_attempt = 0
        cursor.execute(
            "INSERT INTO game_stat (username, gameid, time_taken, unsuccessful_attempt) "
            "VALUES (%s, %s, %s, %s)",
            (username, game_id, time_taken, unsuccessful_attempt))

        game_id = 3
        time_taken = 0
        unsuccessful_attempt = 0
        cursor.execute(
            "INSERT INTO game_stat (username, gameid, time_taken, unsuccessful_attempt) "
            "VALUES (%s, %s, %s, %s)",
            (username, game_id, time_taken, unsuccessful_attempt))

        game_id = 4
        time_taken = 0
        unsuccessful_attempt = 0
        cursor.execute(
            "INSERT INTO game_stat (username, gameid, time_taken, unsuccessful_attempt) "
            "VALUES (%s, %s, %s, %s)",
            (username, game_id, time_taken, unsuccessful_attempt))

        game_id = 5
        time_taken = 0
        unsuccessful_attempt = 0
        cursor.execute(
            "INSERT INTO game_stat (username, gameid, time_taken, unsuccessful_attempt) "
            "VALUES (%s, %s, %s, %s)",
            (username, game_id, time_taken, unsuccessful_attempt))



        mysql.connection.commit()
        cursor.close()
    return render_template('start.html')


@app.route('/app/login')
def login():
    return render_template('login.html')


@app.route('/app/game', methods=['GET', 'POST'])
def game():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        cursor = mysql.connection.cursor()
        cursor.execute("SELECT username FROM info_table WHERE email = %s AND password = %s",
                       (email, password))
        result = cursor.fetchone()

        if result:
            username = result[0]
            session['username'] = username
            return redirect('/app/game')
        else:
            message = "Invalid email or password"
            return render_template('login.html', message=message)
    else:
        username = session.get('username')
        return render_template('game.html', username=username)


@app.route('/app/game1', methods=['GET', 'POST'])
def game1():
    print("check")
    if request.method == 'POST':
        username = session['username']
        end_time = (time.time())
        print("ff")
        time_taken = end_time - session['start_time']
        print(time_taken)
        print(username)

        unsuccessful_attempt = int(request.form['count'])
        print(unsuccessful_attempt)
        cursor = mysql.connection.cursor()
        cursor.execute("UPDATE game_stat SET  unsuccessful_attempt=%s,time_taken = %s "
                       "WHERE username = %s AND gameid = 1",
                       (unsuccessful_attempt, time_taken, username))
        print("done")
        mysql.connection.commit()
        cursor.close()
    else:
        session['start_time'] = (time.time())
        return render_template('game1.html')


@app.route('/app/game2', methods=['GET', 'POST'])
def game2():
    print("check")
    if request.method == 'POST':
        username = session['username']
        end_time = (time.time())
        print("ff")
        time_taken = end_time - session['start_time']
        print(time_taken)
        print(username)

        unsuccessful_attempt = int(request.form['count'])
        print(unsuccessful_attempt)
        cursor = mysql.connection.cursor()
        cursor.execute("UPDATE game_stat SET  unsuccessful_attempt=%s,time_taken = %s "
                       "WHERE username = %s AND gameid = 2",
                       (unsuccessful_attempt, time_taken, username))
        print("done")
        mysql.connection.commit()
        cursor.close()
    else:
        session['start_time'] = int(time.time())

    return render_template('game2.html')


@app.route('/app/game3', methods=['GET', 'POST'])
def game3():
    print("check")
    if request.method == 'POST':
        username = session['username']
        end_time = (time.time())
        print("ff")
        time_taken = end_time - session['start_time']
        print(time_taken)
        print(username)

        unsuccessful_attempt = int(request.form['count'])
        print(unsuccessful_attempt)
        cursor = mysql.connection.cursor()
        cursor.execute("UPDATE game_stat SET  unsuccessful_attempt=%s,time_taken = %s "
                       "WHERE username = %s AND gameid = 3",
                       (unsuccessful_attempt, time_taken, username))
        print("done")
        mysql.connection.commit()
        cursor.close()
    else:
        session['start_time'] = int(time.time())

    return render_template('game3.html')


@app.route('/app/game4', methods=['GET', 'POST'])
def game4():
    print("check")
    if request.method == 'POST':
        username = session['username']
        end_time = (time.time())
        print("ff")
        time_taken = end_time - session['start_time']
        print(time_taken)
        print(username)

        unsuccessful_attempt = int(request.form['count'])
        print(unsuccessful_attempt)
        cursor = mysql.connection.cursor()
        cursor.execute("UPDATE game_stat SET  unsuccessful_attempt=%s,time_taken = %s "
                       "WHERE username = %s AND gameid = 4",
                       (unsuccessful_attempt, time_taken, username))
        print("done")
        mysql.connection.commit()
        cursor.close()
    else:
        session['start_time'] = int(time.time())

    return render_template('game4.html')


@app.route('/app/game5', methods=['GET', 'POST'])
def game5():
    print("check")
    if request.method == 'POST':
        username = session['username']
        end_time = (time.time())
        print("ff")
        time_taken = end_time - session['start_time']
        print(time_taken)
        print(username)

        unsuccessful_attempt = int(request.form['count'])
        print(unsuccessful_attempt)
        cursor = mysql.connection.cursor()
        cursor.execute("UPDATE game_stat SET  unsuccessful_attempt=%s,time_taken = %s "
                       "WHERE username = %s AND gameid = 5",
                       (unsuccessful_attempt, time_taken, username))
        print("done")
        mysql.connection.commit()
        cursor.close()
    else:
        session['start_time'] = int(time.time())

    return render_template('game5.html')


@app.route('/app/wrong')
def wrong():
    return render_template('wrong.html')


@app.route('/app/end')
def end():
    return render_template('end.html')


@app.route('/app/game_complete', methods=['POST'])
def game_complete():
    game_name = request.form['game_name']
    elapsed_time = time.time() - start_times[game_name]
    cur = mysql.connection.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS game_times (id INT AUTO_INCREMENT PRIMARY KEY,game_name VARCHAR(255),
    time_taken INT)""")
    cur.execute("INSERT INTO game_times (game_name, time_taken) VALUES (%s, %s)", (game_name, elapsed_time))
    mysql.connection.commit()
    cur.close()

    return f'{game_name} completed!'



if __name__ == '__main__':
    app.run(debug=True)
