from flask import Flask,render_template,request,session,redirect,Response,flash,url_for
from newsapi import NewsApiClient
from datetime import timedelta

app = Flask(__name__)
app.permanent_session_lifetime = timedelta(hours=5)
app.secret_key = "worldNews" 


@app.route('/')
def Index():
    #client = NewsApiClient(api_key='481da55037f840f0880f83c5ab158dec')
    client = NewsApiClient(api_key='6a0342412e9a4ea7ac5dd621b9f8ffa6')
    sources = client.get_sources()
    categories = list(set(source.get('category') for source in sources.get('sources', [])))
    gradient_colors = [
        "linear-gradient(135deg, #ff9966, #ff5e62)",
        "linear-gradient(135deg, #56CCF2, #2F80ED)",
        "linear-gradient(135deg, #f79d00, #64f38c)",
        "linear-gradient(135deg, #8E2DE2, #4A00E0)",
        "linear-gradient(135deg, #00C9FF, #92FE9D)",
        "linear-gradient(135deg, #ff6a00, #ee0979)",
        "linear-gradient(135deg, #FDC830, #F37335)"
    ]

    category_colors = {category: gradient_colors[i % len(gradient_colors)] for i, category in enumerate(categories)}
    return render_template('index.html', categories=category_colors, navbar_items=categories)

@app.route('/category/<category_name>')
def category_page(category_name):
    client = NewsApiClient(api_key='6a0342412e9a4ea7ac5dd621b9f8ffa6')
    articles = client.get_top_headlines(category=category_name, country="us")
    return render_template('category.html', category=category_name, articles=articles.get("articles", []))

@app.route('/about')
def about():
    return "Developed by Mukesh :)"



if __name__ == "__main__":
    app.run(debug=True,port='5001')
