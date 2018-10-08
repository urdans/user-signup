from flask import Flask, render_template, url_for, request, redirect
from users import Users

app = Flask(__name__)
app.config['DEBUG'] = True

user_list = Users()
session = 0


@app.route('/', methods=['POST', 'GET'])
def signup():
    global session
    if request.method == 'GET':
        return render_template("signup.html", document_title="Sign Up")
    elif request.method == 'POST':
        un = request.form['username']
        ps = request.form['psw']
        em = request.form['email']
        rps = request.form['repsw']
        if ps != rps:
            print('\n---------------Registered users:', len(user_list.user_list))
            return render_template("signup.html", document_title="Sign Up", badpassword="Password mismatch!",
                                   username_value=un, email_value=em)

        newuser = user_list.add_user(un, ps, em)

        if newuser:
            session = hash(un)

            return redirect('/{}'.format(un))
        else:
            print('\n---------------Registered users:', len(user_list.user_list))
            return render_template("signup.html", document_title="Sign Up",
                                   baduser=user_list.get_username_error(), bademail=user_list.get_email_error(),
                                   badpassword=user_list.get_password_error(),
                                   username_value=un, email_value=em)
    else:
        return "Sinelectra - Not found."


@app.route('/<username>', methods=['POST', 'GET'])
def usersession(username):
    if session != hash(username):
        return render_template("welcome.html", message="Please log in!")
    else:
        users = []
        for user in user_list.user_list:
            users.append(user["user_name"])
        return render_template("welcome.html", message="Welcome {}!".format(username), users=users)


app.run()
