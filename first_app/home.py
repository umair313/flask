from flask import Flask, render_template ,url_for , redirect , flash
from forms import RegistrationForm,LoginForm
app = Flask(__name__)
app.config['SECRET_KEY'] = 'dabf80b14253a3916cfc7084d12d10be'

posts = [
    {
        "title": 'how to download IDM',
        'author':"umair mehmood",
        "date_posted": 'Monaday Aug 10 2020 08:45 PST',
        'content':'this is the content',
    },
    {
        "title": 'how to download IDM',
        'author':"umair mehmood",
        "date_posted": 'Monaday Aug 10 2020 08:45 PST',
        'content':'this is the content',
    },
    {
        "title": 'how to download IDM',
        'author':"umair mehmood",
        "date_posted": 'Monaday Aug 10 2020 08:45 PST',
        'content':'this is the content',
    }
]



@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html',title = 'Welcome',posts = posts)


@app.route('/about')
def About():
    return render_template('about.html',title = 'About')



@app.route('/register',methods = ['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f" Account Created for {form.username.data}!",'success')
        return redirect(url_for('home'))
    return render_template('register.html',title = 'Register',form = form)


@app.route('/login',methods = ['GET','POST'])
def login():
    loginform = LoginForm()
    if loginform.validate():
        if loginform.email.data == "admin@blog.com" and loginform.password.data == "admin":
            flash(f" loged-in  as {loginform.email.data} !",'success')
            return redirect(url_for('home'))
        else:
            flash(f" can't login with {loginform.email.data} !",'danger')
    return render_template('login.html',title = 'Login', form = loginform)



if __name__ == "__main__":
    app.run(debug=True)