import pandas as pd
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return showTable()

def showTable():
    data = {'State': ['Alabama', 'Alakas', 'Arizona', 'Arkansas', 'California', 'Colorado','Connecticut', 'Delaware'],
        'Population': [4779736, 710231, 6392017, 2915918, 37253956, 5029196, 3574097, 897934],
        'Homicide': [5.7,5.6,4.7,5.6,4.4,2.8,2.4,5.8],
        'Abreviature': ['AL','AK','AZ', 'AR', 'CA','CO','CT','DE']}

    df = pd.DataFrame(data=data)

    state = df
    mean = state['Population'].mean()
    median = state['Population'].median()

    print( mean)
    print(median)

    return render_template('index.html', df=df, mean=mean, median=median)