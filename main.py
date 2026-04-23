from datetime import datetime
from flask import request, redirect, url_for

def new_news_item(title, body):
    new_id = max(news_items.keys()) + 1
    return {
        'id': new_id,
        'title': title,
        'body': body
    }

@app.route('/news/create/', methods=['POST'])
def create_news_item():
    item = new_news_item(
        request.form['title'],
        request.form['body']
    )
    news_items[item['id']] = item
    return redirect(url_for('index'))
news_items = {
    1: {'id': 1, 'title': 'News 1', 'body': 'Detail 1'},
    2: {'id': 2, 'title': 'News 2', 'body': 'Detail 2'},
}

@app.route("/")
def index():
    return render_template(
        "index.html",
        name="Somchai",
        time=datetime.now(),
        news_items=news_items.values()
    )
@app.route('/news/<int:id>/')
def show_news_item(id):
    item = news_items[id]
    return render_template(
        'news_item.html',
        title=item['title'],
        body=item['body']
    )
