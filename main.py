from datetime import datetime

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
