from bs4 import BeautifulSoup
import pandas as pd


with open("html_pages/html_page.html","r", encoding="utf-8") as f:
    html= f.read()

soup= BeautifulSoup(html,"html.parser")

'''Insert your all BeautifulSoup Commands here!'''