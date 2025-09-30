# ── Import required libraries ──
import pandas as pd
from dash import Dash, html, dcc, Input, Output
import plotly.express as px

# ── Load dataset ──
spacex_df = pd.read_csv("spacex_launch_dash.csv")
max_payload = spacex_df['Payload Mass (kg)'].max()
min_payload = spacex_df['Payload Mass (kg)'].min()

# ── Prepare launch site options for dropdown ──
launch_sites = [{'label': 'All Sites', 'value': 'All Sites'}]
all_launch_sites = spacex_df['Launch Site'].unique().tolist()
for launch_site in all_launch_sites:
    launch_sites.append({'label': launch_site, 'value': launch_site})

# ── Initialize Dash app ──
app = Dash(__name__)

# ── Define app layout ──
app.layout = html.Div(children=[
    html.H1(
        'SpaceX Launch Records Dashboard',
        style={'textAlign': 'center', 'color': '#503D36', 'font-size': 40}
    ),

    # Dropdown for launch site selection
    html.Div([
        dcc.Dropdown(
            id='site-dropdown',
            options=launch_sites,
            placeholder='Select a Launch Site here',
            searchable=True,
            clearable=False,
            value='All Sites'
        )
    ]),
    html.Br(),

    # Pie chart for success counts
    html.Div(dcc.Graph(id='success-pie-chart')),
    html.Br(),

    # Payload range slider
    html.P("Payload range (Kg):"),
    html.Div([
        dcc.RangeSlider(
            id='payload_slider',
            min=0,
            max=10000,
            step=1000,
            marks={
                0: {'label': '0 Kg', 'style': {'color': '#77b0b1'}},
                1000: {'label': '1000 Kg'},
                2000: {'label': '2000 Kg'},
                3000: {'label': '3000 Kg'},
                4000: {'label': '4000 Kg'},
                5000: {'label': '5000 Kg'},
                6000: {'label': '6000 Kg'},
                7000: {'label': '7000 Kg'},
                8000: {'label': '8000 Kg'},
                9000: {'label': '9000 Kg'},
                10000: {'label': '10000 Kg', 'style': {'color': '#f50'}},
            },
            value=[min_payload, max_payload]
        )
    ]),

    # Scatter plot for payload vs. success
    html.Div(dcc.Graph(id='success-payload-scatter-chart'))
])

# ── Callback: Update pie chart ──
@app.callback(
    Output('success-pie-chart', 'figure'),
    Input('site-dropdown', 'value')
)
def update_piegraph(site_dropdown):
    if site_dropdown == 'All Sites' or site_dropdown == 'None':
        data = spacex_df[spacex_df['class'] == 1]
        fig = px.pie(
            data,
            names='Launch Site',
            title='Total Success Launches by All Sites'
        )
    else:
        data = spacex_df.loc[spacex_df['Launch Site'] == site_dropdown]
        fig = px.pie(
            data,
            names='class',
            title=f'Total Success Launches for Site → {site_dropdown}'
        )
    return fig

# ── Callback: Update scatter plot ──
@app.callback(
    Output('success-payload-scatter-chart', 'figure'),
    [Input('site-dropdown', 'value'),
     Input('payload_slider', 'value')]
)
def update_scattergraph(site_dropdown, payload_slider):
    low, high = payload_slider
    if site_dropdown == 'All Sites' or site_dropdown == 'None':
        data = spacex_df
    else:
        data = spacex_df.loc[spacex_df['Launch Site'] == site_dropdown]

    inrange = (data['Payload Mass (kg)'] > low) & (data['Payload Mass (kg)'] < high)
    fig = px.scatter(
        data[inrange],
        x="Payload Mass (kg)",
        y="class",
        title=f'Correlation Between Payload and Success for {"All Sites" if site_dropdown == "All Sites" else "Site → " + site_dropdown}',
        color="Booster Version Category",
        size='Payload Mass (kg)',
        hover_data=['Payload Mass (kg)']
    )
    return fig

# ── Run app ──
if __name__ == '__main__':
    app.run(debug=True)  # host='0.0.0.0', port=8050 si lo necesitas
