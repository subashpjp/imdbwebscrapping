
from unicodedata import name
from flask import Flask, render_template, redirect,url_for,request

import requests


from bs4 import BeautifulSoup


  
app = Flask(__name__)


@app.route('/')
def land_page():  
    return render_template('imdbindex.html')

@app.route('/result', methods = ['POST'])
def result():
    if request.method == 'POST':
      user = request.form['moviesearch']
      inUrl = "https://www.imdb.com/search/title/?title_type=feature&sort=num_votes,desc&count="+user
      unparsed_response = requests.get(inUrl)
      parsed_response = BeautifulSoup(unparsed_response.text, 'html.parser')
      required_item = parsed_response.find_all('div', class_ = "lister-item mode-advanced")
      return render_template('result.html',  details = required_item)
    

if __name__ == '__main__':
    app.run()

