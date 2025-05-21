import matplotlib
matplotlib.use("Agg")
import numpy as np
import matplotlib.pyplot as plt
import os
from flask import Flask, render_template

# Flask app with correct folder paths
app = Flask(__name__, static_folder='static', template_folder='templates')

def get_plot():
    data = {
        'a': np.arange(50),
        'c': np.random.randint(0, 50, 50),
        'd': np.random.randn(50)
    }
    data['b'] = data['a'] + 10 * np.random.randn(50)
    data['d'] = np.abs(data['d']) * 100

    plt.clf()  # Clear figure
    plt.scatter('a', 'b', c='c', s='d', data=data)
    plt.xlabel('X label')
    plt.ylabel('Y label')
    return plt

@app.route('/')
def home():
    plot = get_plot()
    plot_path = os.path.join(app.static_folder, 'images', 'plot.png')
    plot.savefig(plot_path)
    return render_template('matplotlib-plot1.html')

@app.route('/show-image')
def show_image():
    plot = get_plot()
    plot_path = os.path.join(app.static_folder, 'images', 'plot.png')
    plot.savefig(plot_path)
    return '''
    <html>
        <body>
            <h2>Latest Plot Image</h2>
            <img src="/static/images/plot.png" alt="Plot image">
        </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(debug=True)