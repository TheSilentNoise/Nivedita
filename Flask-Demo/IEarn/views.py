from flask import render_template,redirect,url_for,session,request
from app import app
from models import *
import datetime
from app import db
from forms import Loginform,Registrationform
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import LoginManager,login_user,login_required,logout_user,current_user


#### login_manager

login_manager = LoginManager()
login_manager.session_protection = "strong"
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))




############ login ,registration ###############


@app.route('/')
def index():
    if current_user.is_authenticated:
      return render_template('index.html',name=current_user.user_name)
    return render_template('index.html')


@app.route('/login',methods=['GET','POST'])
def login():
     if not current_user.is_authenticated:
        form = Loginform()
        if form.validate_on_submit():
            user = User.query.filter_by(user_email=form.email.data).first()
            print(user)
            if user:
                #session['username'] = form.username.data
                if check_password_hash(user.user_password,form.password.data):
                    login_user(user,remember=form.remember.data)
                    return redirect(url_for('index'))
            return render_template('login.html',form=form,message="Incorrect username or password")
        return render_template('login.html',form=form)
     return redirect((url_for('index')))



@app.route('/signup',methods=['GET','POST'])
def signup():
        form = Registrationform()
        if form.validate_on_submit():
            try:
                # session['username'] = form.username.data
                hashed_password = generate_password_hash(form.user_password.data, method='sha256')
                date_created = datetime.datetime.now()
                new_user = User(
                    user_name=form.user_name.data,
                    user_email=form.user_email.data,
                    user_phoneno=form.user_phoneno.data,
                    user_password=hashed_password,
                    date_created=date_created)
                db.session.add(new_user)
                db.session.commit()
                return redirect( url_for('login'))
            except Exception as e:
                return render_template('signup.html', form=form, error_msg="Username already exists!!")
        return render_template('signup.html',form=form)



@app.route('/logout')
@login_required
def logout():
    logout_user()
    session.pop('username', None)
    return redirect(url_for('index'))


@app.route('/enroll-now',methods=['GET','POST'])
def enroll_now():
    if current_user.is_authenticated:
        course_id = request.args.get('course_id', type=int)
        user_id = current_user.id
        date_created = datetime.datetime.now()
        user_course = User_Course(user_id=user_id,
                                  course_id=course_id,
                                  date_created=date_created)
        db.session.add(user_course)
        db.session.commit()
        return redirect(url_for('mycourses'))
    return redirect(url_for('login'))



############## courses ############



@login_required
@app.route('/mycourses')
def mycourses():
    if current_user.is_authenticated:
      no_of_course = User_Course.query.with_entities(User_Course.course_id).filter_by(user_id=current_user.id).count()
      if no_of_course == 0:
          return render_template('mycourses.html',name=current_user.user_name,message=True)
      else:
         try:
             courseqry = Courses.query\
                        .join(User_Course, Courses.id == User_Course.course_id)\
                        .with_entities(Courses.course_name,Courses.course_url)\
                        .filter_by(user_id=current_user.id).distinct().all()

             user_courseList =[]
             for usr_course in courseqry:
                 user_courseList.append(usr_course)
             return render_template("mycourses.html", user_courseList=user_courseList,name=current_user.user_name )

         except Exception:
             return render_template('mycourses.html', name=current_user.user_name)
    return redirect(url_for('courses'))




@app.route('/courses')
def courses():
    if current_user.is_authenticated:
      return render_template('courses.html',name=current_user.user_name)
    return render_template('courses.html')



@app.route('/courses/data-engineering-fundamentals')
def course_data_engineering():
    if current_user.is_authenticated:
      return render_template('courses/data-engineering-course.html',name=current_user.user_name)
    return render_template('courses/data-engineering-course.html')



############ blogs #############


@app.route('/blogs')
def blogs():
    if current_user.is_authenticated:
      return render_template('blogs.html',name=current_user.user_name)
    return render_template('blogs.html')


@app.route('/api-concepts')
def api_concepts():
    if current_user.is_authenticated:
      return render_template('blogs/api-concepts.html',name=current_user.user_name)
    return render_template('blogs/api-concepts.html')


@app.route('/java-collection-cheatsheet')
def java_collection_cheatsheet():
    if current_user.is_authenticated:
       return render_template('blogs/java-collection-cheatsheet.html',name=current_user.user_name)
    return render_template('blogs/java-collection-cheatsheet.html')



####### user profile ########

@login_required
@app.route('/profile')
def profile():
    if current_user.is_authenticated:
       return render_template('profile.html',name=current_user.user_name)
    return redirect(url_for('index'))



####### student course #######


@login_required
@app.route('/data-engineering-tutorial')
def data_engineering_tutorial():
    if current_user.is_authenticated:
       return render_template('student-course/de.html',name=current_user.user_name)
    return redirect(url_for('courses'))







