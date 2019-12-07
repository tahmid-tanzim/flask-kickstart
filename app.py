from flask import Flask, render_template, url_for
app = Flask(__name__)

posts = [{
    'author': 'Tahmid Tanzim Lupin',
    'date_posted': '25th March, 2019',
    'title': 'Lorem Ipsum',
    'content': 'Lorem Ipsum Lorem Ipsum Lorem Ipsum Lorem Ipsum'
},{
    'author': 'Tahmid Tanzim Lupin',
    'date_posted': '25th March, 2019',
    'title': 'Lorem Ipsum',
    'content': 'Lorem Ipsum Lorem Ipsum Lorem Ipsum Lorem Ipsum'
}]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)


@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == "__main__":
    app.run(debug=True)
