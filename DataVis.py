import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

# Load the Iris dataset
url = "https://gist.githubusercontent.com/curran/a08a1080b88344b0c8a7/raw/639388c2cbc2120a14dcf466e85730eb8be498bb/iris.csv"
df = pd.read_csv(url)

# Initialize the Dash app
app = dash.Dash(__name__)

# Define the layout
app.layout = html.Div([
    dcc.Dropdown(
        id='feature_dropdown',
        options=[
            {'label': 'Sepal Length', 'value': 'sepal_length'},
            {'label': 'Sepal Width', 'value': 'sepal_width'},
            {'label': 'Petal Length', 'value': 'petal_length'},
            {'label': 'Petal Width', 'value': 'petal_width'}
        ],
        value='sepal_length',
        multi=True,
        placeholder="Select features to plot"
    ),
    dcc.Graph(id='scatterplot')
])

# Define the callback for updating the scatter plot
@app.callback(
    Output('scatterplot', 'figure'),
    Input('feature_dropdown', 'value'))
def update_scatterplot(selected_features):
    if len(selected_features) == 0:
        return px.scatter(title="Select features to plot")
    else:
        return px.scatter(df, x=selected_features[0], y=selected_features[1] if len(selected_features) > 1 else selected_features[0],
                          color="species", title="Iris Dataset: Scatter Plot", hover_data=['species'])

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)