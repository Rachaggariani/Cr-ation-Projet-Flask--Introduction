from flask import Flask , render_template
app=Flask(__name__)
@app.route('/')
def accueil():
    return render_template('home.html')

@app.route('/contact')
def contact():
    return render_template('contact.html',message='Vous pouvez nous contacter par email à contact@monsite.com')

if __name__ == '__main__':
    app.run(debug=True,port=5001)