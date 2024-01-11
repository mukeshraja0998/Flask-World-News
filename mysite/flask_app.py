from flask import Flask,render_template,request,session,redirect,Response,flash,url_for
from newsapi import NewsApiClient
from datetime import timedelta

app = Flask(__name__)
app.permanent_session_lifetime = timedelta(hours=5)
app.secret_key = "worldNews" 


@app.route('/')
def Index():
    client = NewsApiClient(api_key='481da55037f840f0880f83c5ab158dec')
    sources = client.get_sources()
    names=[]
    for i in sources['sources']:
        names.append(i)
    return render_template('index.html',parent_list=names)

@app.route('/generalRoute', methods=["GET","POST"])
def generalRoute():
    if(request.method=='POST'):
        newsapi = NewsApiClient(api_key="481da55037f840f0880f83c5ab158dec")
        session['sources'] = request.form['sources']
        #print(session['sources'])
        topheadlines = newsapi.get_top_headlines(sources=session['sources'])
        articles = topheadlines['articles']
        desc = []
        news = []
        img = []
        url=[]
        for i in range(len(articles)):
            myarticles = articles[i]
            news.append(myarticles['title'])
            desc.append(myarticles['description'])
            img.append(myarticles['urlToImage'])
            url.append(myarticles['url'])
        mylist = zip(news, desc, img,url)
        return render_template('news.html', context=mylist)
    else:
        return "get request"

@app.route('/tech')
def tech():
    client = NewsApiClient(api_key='481da55037f840f0880f83c5ab158dec')
    sources=client.get_sources(category='technology',language='en')
    names=[]
    for i in sources['sources']:
        names.append(i)
    return render_template('index.html',parent_list=names)

@app.route('/sports')
def sports():
    client = NewsApiClient(api_key='481da55037f840f0880f83c5ab158dec')
    sources=client.get_sources(category='sports',language='en')
    names=[]
    for i in sources['sources']:
        names.append(i)
    return render_template('index.html',parent_list=names)
    

@app.route('/general')
def general():
    client = NewsApiClient(api_key='481da55037f840f0880f83c5ab158dec')
    sources=client.get_sources(category='general',language='en')
    names=[]
    for i in sources['sources']:
        names.append(i)
    return render_template('index.html',parent_list=names)

@app.route('/science')
def science():
    client = NewsApiClient(api_key='481da55037f840f0880f83c5ab158dec')
    sources=client.get_sources(category='science',language='en')
    names=[]
    for i in sources['sources']:
        names.append(i)
    return render_template('index.html',parent_list=names)

@app.route('/business')
def business():
    client = NewsApiClient(api_key='481da55037f840f0880f83c5ab158dec')
    sources=client.get_sources(category='business',language='en')
    names=[]
    for i in sources['sources']:
        names.append(i)
    return render_template('index.html',parent_list=names)

@app.route('/entertainment')
def entertainment():
    client = NewsApiClient(api_key='481da55037f840f0880f83c5ab158dec')
    sources=client.get_sources(category='entertainment',language='en')
    names=[]
    for i in sources['sources']:
        names.append(i)
    return render_template('index.html',parent_list=names)

@app.route('/about')
def about():
    return "Developed by Mukesh :)"



if __name__ == "__main__":
    app.run(debug=True,port='5001')
