import time
from io import StringIO
from urllib.parse import urlparse

import pandas as pd
import requests
from sklearn.linear_model import SGDClassifier
from sklearn.tree import DecisionTreeClassifier




def load_data():
    data_url = "https://abnormalsecurity-public.s3.us-east-1.amazonaws.com/url_interview_cleaned.csv"
    content = requests.get(data_url).content.decode('utf-8')
    container = StringIO(content)
    urldata = pd.read_csv(container, sep='\t', names=['label', 'url'])
    urldata = urldata[urldata['url'].notna()]
    return urldata


def enrich_with_features(urldata):
    # Length of URL
    urldata['url_length'] = urldata['url'].apply(lambda i: len(str(i)))
    # Hostname Length
    urldata['hostname_length'] = urldata['url'].apply(lambda i: len(urlparse(i).netloc))
    # Path Length
    urldata['path_length'] = urldata['url'].apply(lambda i: len(urlparse(i).path))

    # First Directory Length
    def fd_length(url):
        urlpath = urlparse(url).path
        try:
            return len(urlpath.split('/')[1])
        except:
            return 0

    urldata['fd_length'] = urldata['url'].apply(lambda i: fd_length(i))
    urldata['count-'] = urldata['url'].apply(lambda i: i.count('-'))
    urldata['count@'] = urldata['url'].apply(lambda i: i.count('@'))
    urldata['count?'] = urldata['url'].apply(lambda i: i.count('?'))
    urldata['count%'] = urldata['url'].apply(lambda i: i.count('%'))
    urldata['count.'] = urldata['url'].apply(lambda i: i.count('.'))
    urldata['count='] = urldata['url'].apply(lambda i: i.count('='))
    urldata['count-http'] = urldata['url'].apply(lambda i: i.count('http'))
    urldata['count-https'] = urldata['url'].apply(lambda i: i.count('https'))
    urldata['count-www'] = urldata['url'].apply(lambda i: i.count('www'))

    def digit_count(url):
        digits = 0
        for i in url:
            if i.isnumeric():
                digits = digits + 1
        return digits

    urldata['count-digits'] = urldata['url'].apply(lambda i: digit_count(i))

    def letter_count(url):
        letters = 0
        for i in url:
            if i.isalpha():
                letters = letters + 1
        return letters

    urldata['count-letters'] = urldata['url'].apply(lambda i: letter_count(i))

    def no_of_dir(url):
        urldir = urlparse(url).path
        return urldir.count('/')

    urldata['count_dir'] = urldata['url'].apply(lambda i: no_of_dir(i))


urldata = load_data()
enrich_with_features(urldata)

# Predictor Variables
features = ['hostname_length',
            'path_length', 'fd_length', 'count-', 'count@', 'count?',
            'count%', 'count.', 'count=', 'count-http', 'count-https', 'count-www', 'count-digits',
            'count-letters', 'count_dir']
x = urldata[features]

# Target Variable
y = urldata['label']
# Decision Tree
s=time.time()
dt_model = SGDClassifier()
dt_model.fit(x, y)
print("model built")
s=time.time()

def classify_url(url):
    sample_df = pd.DataFrame({'url': url}, index=[0])
    enrich_with_features(sample_df)
    return dt_model.predict(sample_df[features])[0] == '1'


print(classify_url("http://go.pardot.com/e/45492/mail-utm-content-fivess-201807/5tfzsv/1306746875"))
