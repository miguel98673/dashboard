# -*- coding: utf-8 -*-
"""
Created on Mon May 17 15:14:11 2021

@author: Utilizador
"""

# Miguel Piçarra 98673

import pandas as pd
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output


def generate_table(dataframe, max_rows=100):
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in dataframe.columns])
        ),
        html.Tbody([
            html.Tr([
                html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
            ]) for i in range(min(len(dataframe), max_rows))
        ])
    ])



IST_meteo=pd.read_csv('IST_meteo_data_2017_2018_2019.csv')

IST_North_Tower_2017=pd.read_csv('IST_North_Tower_2017_Ene_Cons.csv')

IST_North_Tower_2018=pd.read_csv('IST_North_Tower_2018_Ene_Cons.csv')

Modelo_IST=pd.read_csv('Modelo_IST.csv')


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    html.Img(src=app.get_asset_url('AIST_logo.png')),
    html.H2('Miguel Piçarra - 98673'),
    html.H3('Torre Norte'),
    dcc.Tabs(id='tabs', value='tab1', children=[
        dcc.Tab(label='Dados', value='tab1'),
        dcc.Tab(label='Análise aos Gráficos', value='tab2'),
        dcc.Tab(label='Clustering', value='tab3'),
        dcc.Tab(label='Feature Selection', value='tab4'),
        dcc.Tab(label='Modelo Final', value='tab5'),
        dcc.Tab(label='Regressão', value='tab6')
        
    ]),
    html.Div(id='tabs-content')
])


@app.callback(Output('tabs-content', 'children'),
              Input('tabs', 'value'))

def render_content(tab):
    if tab == 'tab1':
        return html.Div([
            html.H3('Dados'),
            dcc.RadioItems(
        id='radio1',
        options=[
            {'label': 'Dados de Metereologia de 2017, 2018 e 2019', 'value': 1},
            {'label': 'Dados de Consumo de Energia da Torre Norte 2017', 'value': 2},
            {'label': 'Dados de Consumo de Energia da Torre Norte 2018', 'value': 3},
        ], 
        value=1
        ),
        html.Div(id='Dados'),
                    ])
    
    elif tab == 'tab2':
        return html.Div([
            html.H3('Análise aos Gráficos'),
            dcc.RadioItems(
        id='radio2',
        options=[
            {'label': 'Gráfico Humidade Relativa ao longo do tempo ', 'value': 1},
            {'label': 'Gráfico Potência ao longo do tempo', 'value': 2},
            {'label': 'Gráfico Pressão ao longo do tempo', 'value': 3},
            {'label': 'Gráfico Chuva ao longo do tempo', 'value': 4},
            {'label': 'Gráfico Dias de Chuva ao longo do tempo', 'value': 5},
            {'label': 'Gráfico Radiação Solar ao longo do tempo', 'value': 6},
            {'label': 'Gráfico Temperatura ao longo do tempo', 'value': 7},
            {'label': 'Gráfico Wind Gust ao longo do tempo', 'value': 8},
            {'label': 'Gráfico Wind Speed ao longo do tempo', 'value': 9}   
        ], 
        value=1
        ),
        html.Div(id='Análise aos Gráficos'),
                    ])
    
    elif tab == 'tab3':
        return html.Div([
            html.H3('Clustering'),
            dcc.RadioItems(
        id='radio3',
        options=[
            {'label': 'Gráfico Horas vs Potência', 'value': 1},
            {'label': 'Gráfico Humidade Relativa vs Temperatura', 'value': 2},
            {'label': 'Gráfico Temperatura vs Potência', 'value': 3},
            {'label': 'Gráfico Wind Gust vs Wind Speed', 'value': 4},  
        ], 
        value=1
        ),
        html.Div(id='Clustering'),
                    ])
    
    elif tab == 'tab4':
        return html.Div([
            html.H3('Feature Selection'),
            html.H6('De acordo com o kBest, os inputs mais relevantes para a optenção do output (Power_kW) são (por ordem decrescente):'),
            html.H6('- O valor da energia na hora anterior;'),
            html.H6('- A radiação solar;'),
            html.H6('- A temperatura;'),
            html.H6('De acordo com o RFE, os inputs mais relevantes para a optenção do output (Power_kW) são (por ordem decrescente):'),
            html.H6('- A chuva em mm/h;'),
            html.H6('- A hora do dia;'),
            html.H6('- O valor da energia na hora anterior;'),
            html.H6('De acordo com o Emsemble Methods, os inputs mais relevantes para a optenção do output (Power_kW) são (por ordem decrescente):'),
            html.H6('- A radiação solar;'),
            html.H6('- O valor da energia na hora anterior;'),
            html.H6('- A hora do dia;'),
                    ])
    
    elif tab == 'tab5':
        return html.Div([
            html.H3('Modelo Final'),
            html.H6('Após cuidada análise, decidiu-se que os dados que melhor descrevem o consumo de energia são:'),
            html.H6('- O valor da energia na hora anterior'),
            html.H6('- A radiação solar'),
            html.H6('- A temperatura'),
            html.H6('- A humidade relativa'),
            
            dcc.Graph(
        id='final_data',
        figure={
            'data': [
                {'x': Modelo_IST['Date'], 'y': Modelo_IST['Power_kW'], 'type': 'line', 'name': 'Potência'},
                {'x': Modelo_IST['Date'], 'y': Modelo_IST['temp_C'], 'type': 'line', 'name': 'Temperatura'},
                {'x': Modelo_IST['Date'], 'y': Modelo_IST['HR'], 'type': 'line', 'name': 'Humidade Relativa'},
                {'x': Modelo_IST['Date'], 'y': Modelo_IST['solarRad_W/m2'], 'type': 'line', 'name': 'Radiação Solar'},
                {'x': Modelo_IST['Date'], 'y': Modelo_IST['Power-1'], 'type': 'line', 'name': 'Potência Hora Anterior'},
            ],
        }
    ),
       
                    ])

    elif tab == 'tab6':
        return html.Div([
            html.H3('Regressão'),
            html.H6('O melhor Método é o Random Forest:'),
            html.H6('- MAE = 7.632093592063719'),
            html.H6('- MSE = 219.3813661944555'),
            html.H6('- RMSE = 14.811528151897612'),
            html.H6('- cvRMSE = 0.13423980132093005'),
            dcc.RadioItems(
        id='radio6',
        options=[
            {'label': 'Decision Tree Regressor', 'value': 1},
            {'label': 'Gradient Boosting', 'value': 2},
            {'label': 'Linear Regression', 'value': 3},
            {'label': 'Neural Networks', 'value': 4},
            {'label': 'Random Forest', 'value': 5},
            {'label': 'Uniformized Data', 'value': 6},    
        ], 
        value=5
        ),
        html.Div(id='Regressão'),
                    ])


@app.callback(Output('Dados', 'children'), 
             Input('radio1', 'value'))

def render_figure_png(teste1):
    
    if teste1 == 1:
        return generate_table(IST_meteo)
    elif teste1 == 2:
        return generate_table(IST_North_Tower_2017)
    elif teste1 == 3:
        return generate_table(IST_North_Tower_2018)


@app.callback(Output('Análise aos Gráficos', 'children'), 
             Input('radio2', 'value'))

def render_figure_png(teste2):
    
    if teste2 == 1:
        return html.Div([html.Img(src='assets/hr.PNG'),])
    elif teste2 == 2:
        return html.Div([html.Img(src='assets/power_kW.PNG'),])
    elif teste2 == 3:
        return html.Div([html.Img(src='assets/pres_mbar.PNG'),])
    elif teste2 == 4:
        return html.Div([html.Img(src='assets/rain_day.PNG'),])
    elif teste2 == 5:
        return html.Div([html.Img(src='assets/rain.PNG'),])
    elif teste2 == 6:
        return html.Div([html.Img(src='assets/solarRad.PNG'),])
    elif teste2 == 7:
        return html.Div([html.Img(src='assets/temp_C.PNG'),])
    elif teste2 == 8:
        return html.Div([html.Img(src='assets/windGust.PNG'),])
    elif teste2 == 9:
        return html.Div([html.Img(src='assets/windSpeed.PNG'),]),



@app.callback(Output('Clustering', 'children'), 
             Input('radio3', 'value'))

def render_figure_png(teste3):
    
    if teste3 == 1:
        return html.Div([html.Img(src='assets/Clustering_HOURvsPOWER.PNG'),])
    elif teste3 == 2:
        return html.Div([html.Img(src='assets/Clustering_HRvsTEMP.PNG'),])
    elif teste3 == 3:
        return html.Div([html.Img(src='assets/Clustering_TEMPvsPOWER.PNG'),])
    elif teste3 == 4:
        return html.Div([html.Img(src='assets/Clustering_WINDGUSTvsWINDSPEED.PNG'),])
   


@app.callback(Output('Regressão', 'children'), 
             Input('radio6', 'value'))

def render_figure_png(teste4):
    
    if teste4 == 1:
        return html.Div([html.Img(src='assets/FS_decision_tree_regression.PNG'),])
    elif teste4 == 2:
        return html.Div([html.Img(src='assets/FS_gradient_boosting.PNG'),])
    elif teste4 == 3:
        return html.Div([html.Img(src='assets/FS_linear_regression.PNG'),])
    elif teste4 == 4:
        return html.Div([html.Img(src='assets/FS_neural_networks.PNG'),])
    elif teste4 == 5:
        return html.Div([html.Img(src='assets/FS_random_forest.PNG'),])
    elif teste4 == 6:
        return html.Div([html.Img(src='assets/FS_uniformized_data.PNG'),])

    
if __name__ == '__main__':
    app.run_server(debug=True)