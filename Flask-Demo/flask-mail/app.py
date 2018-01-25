from flask import Flask,render_template
from flask_mail import Mail, Message

app =Flask(__name__)
mail=Mail(app)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'dma.rssoftware@gmail.com'
app.config['MAIL_PASSWORD'] = 'Ayan_Nivedita_Rajesh'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

@app.route("/")
def index():
   msg = Message('Hello World', sender = 'nivedita.mondal92@gmail.com', recipients = ['niveditamondal92@gmail.com'],cc=['rajeshpyne@gmail.com'])
   #msg.body = "How are you ?"
   #mail.send(msg)
   msg.html = render_template('test.html')
   mail.send(msg)
   print("okkk")
   return "Sent"

if __name__ == '__main__':
   app.run(debug = True)