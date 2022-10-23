# Hack_The_Valley_2022_Fake_News_Detector
**Credable**

# About
A Google Chrome extension that detects is a certain news article is reliable. Our goal with this project is to let people identify fake news easier and faster, therefore creating a better and more credible world. Future changes that we can make include: hosting the api on our website credability.tech, refining and creating a better UI/UX, and potentially create ad space.

# How it works
We first scrape the url from the current site and send it to our backend API which is made using Flask. The API will then determine if it is a news article by checking it exists under the news tab in Google News. If the current article is a news article, we will then summarize it, take key words and find related links. We will also feed it through our machine learning model which will give us if the article is real or not. After that, we package all the data and send it to our chrome extension for the user to see.

# Website
Link to project github can be found through our website credability.tech until October 2023. The website is also in the same repository, except it is hosted under a different branch.

# Requirements
- Python 3.9+ to run API
Python Modules needed:
- Requests
- Beautiful Soup 4
- Newspaper3
- Flask
- Google
- Pandas
- Sklearn

# Made by:
Zein Sleiman
Weiming Quan
Omar Jaljoulli
Kevin Ni