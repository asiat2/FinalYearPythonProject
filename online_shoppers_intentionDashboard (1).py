#########Loading the required library###############
import numpy as np
import plotly.graph_objects as go # creates plots
import pandas as pd # standard for data processing
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.offline as pyo
import plotly.express as px
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import matplotlib.pyplot as plt
import seaborn as sns

############Loading the data set############
path_to_csv =("C:/Users/ashia/OneDrive - Data ScienceTech Institute/Python Lab DSTI/MyPythonProject/GroupProejct/onlineshoppingintention.csv")
df = pd.read_csv(path_to_csv)
Revenue = df['Revenue'].unique()
VisitorType = df['VisitorType'].unique()
Weekend = df['Weekend'].unique()
Month = df['Month'].unique()


##########Plots to Display ########
### UniVarient Plot###    
figM = px.histogram(df, x="Month", color="Month",height=370,title="User Count By Month").update_xaxes(categoryorder="total descending")
figV = px.histogram(df, x="VisitorType", color="VisitorType",height=370,title="User Count By Visisttype")
figW = px.histogram(df, x="Weekend",color="Weekend",height=370,title="User Count By Weekend")
figB = px.histogram(df, x="Browser",color="Browser",height=370,title="User Count By Browser")
figRe = px.histogram(df, x="Region",color="Region",height=370,title="User Count By Region")
figT = px.histogram(df, x="TrafficType",color="TrafficType",height=370,title="User Count By TrafficType")

### BiVarient Plot###
groupped = df.groupby(by='TrafficType',as_index=False).sum()
fig = px.bar(groupped,x='TrafficType' ,y='Average_user_visit',orientation='v',color='TrafficType',title="Average User visits vs TrafficType",height=370)

groupped = df.groupby(by='Month',as_index=False).sum()
figMo = px.bar(groupped,x='Month' ,y='Average_user_visit',orientation='v',color='Month',title="Amount of time spent on ProductRelated pages by month",height=370)
figMo.update_layout(barmode='stack', xaxis={'categoryorder':'total descending'})

groupped2 = df.groupby(by='OperatingSystems',as_index=False).sum()
figVi = px.bar(groupped2,x='OperatingSystems' ,y='Average_D',orientation='v',color='OperatingSystems',title="Average time spent on each session by OperatingSystems",height=370)

groupped = df.groupby(by='Region',as_index=False).sum()
figR = px.bar(groupped,x='Region' ,y='Average_user_visit',orientation='v',color='Region',title="Average_user_visit by Region",height=370)

### MultiVarient Plot###
BoEx = px.scatter(df,x= 'BounceRates',y='ExitRates',orientation ='v',color='Revenue', title="BounceRate vs ExitRates with Revenue",height=370)

BoAv = px.scatter(df,x= 'BounceRates',y='Average_user_visit',orientation ='v',color='OperatingSystems', title="BounceRate vs Average_user_visit and Operating Systems",height=370)

PdPv = px.scatter(df,x='ProductRelated_Duration',y='ProductRelated_Visited',orientation ='v',color='Revenue', title="ProductRelated_Visited vs ProductRelated_Duration with Revenue",height=370)


Av_D= px.scatter(df,x='Average_D',y='Average_user_visit',orientation ='v',color='Revenue', title="Average user visit vs Average Duration and Revenue",height=370)


#create the app
app = dash.Dash("Onlineshoppingintention", external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = html.Div([
    dbc.Row(
                dbc.Col(
            html.H1(
            id="title",
            children="Online Shoppers Intention Analysis"

                ), width={"size": 8, "offset": 4}
            )
        ),
    dcc.Tabs([
        
        dcc.Tab(id = 'tab1', label='Univariate Analysis', children=[ 
           dbc.Row([
               dbc.Col(dcc.Graph(
                   figure = figM,
                 ),width=4,
               ),
               dbc.Col(dcc.Graph(
                   figure = figV,
                 ),width=4,
               ),
               dbc.Col(dcc.Graph(
                   figure = figB,
                 ),width=4,
               ),
           ]),
           dbc.Row([
               dbc.Col(dcc.Graph(
                   figure = figW,
                 ),width=4,
               ),
               dbc.Col(dcc.Graph(
                   figure = figRe,
                 ),width=4,
               ),
               dbc.Col(dcc.Graph(
                   figure = figT,
                 ),
               ),
           ]),

        ]),

        dcc.Tab(id = 'tab2',label='Bivariate Analysis', children=[
             dbc.Row([
               dbc.Col( [
                      html.H4(id ="rev", children="Revenue"),
                        dcc.Dropdown(
                            id='Reve',
                            options=[{'label': i, 'value': i} for i in Revenue],
                            value='Buy'
                        ),
             ]),
               dbc.Col( [
                   html.H4(id ="vis", children="VisitorType"),
                   dcc.Dropdown(
                        id='Visi',
                        options=[{'label': i, 'value': i} for i in VisitorType],
                        value='Returning_Visitor'
                    ),
             ]),
           ]),
           dbc.Row([
               dbc.Col(dcc.Graph(
                   id = "Bi1",
                   figure = fig,
                 ),width=6,
               ),
               dbc.Col(dcc.Graph(
                   id = "Bi2",
                   figure = figMo,
                 ),width=6,
               ),
           ]),    
           dbc.Row([
               dbc.Col(dcc.Graph(
                   id = "Bi3",
                   figure = figVi,
                 ),width=6,
               ),
               dbc.Col(dcc.Graph(
                   id = "Bi4",
                   figure = figR,
                 ),width=6,
               ),
           ]),        
        ]),
        dcc.Tab(id = 'tab3',label='Multivariate Analysis', children=[
             dbc.Row([
               dbc.Col( [
                      html.H4(id ="wek1", children="Weekend"),
                        dcc.Dropdown(
                            id='multiwek',
                            options=[{'label': i, 'value': i} for i in Weekend],
                            value='Yes'
                        ),
             ]),
               dbc.Col( [
                   html.H4(id ="mon1", children="Month"),
                   dcc.Dropdown(
                        id='multimo',
                        options=[{'label': i, 'value': i} for i in Month],
                        value='Nov'
                    ),
             ]),
           ]),
          dbc.Row([
               dbc.Col(dcc.Graph(
                   id = "Mul1",
                   figure = BoEx,
                 ),width=6,
               ),
               dbc.Col(dcc.Graph(
                   id = "Mul2",
                   figure = BoAv,
                 ),width=6,
               ),
           ]),    
           dbc.Row([
               dbc.Col(dcc.Graph(
                   id = "Mul3",
                   figure =  PdPv,
                 ),width=6,
               ),
               dbc.Col(dcc.Graph(
                   id = "Mul4",
                   figure =Av_D, 
                 ),width=6,
               ),
           ]),

        ]),
    ])
])
@app.callback([
    Output("Bi1","figure"),
    Output("Bi2","figure"),
    Output("Bi3","figure"),
    Output("Bi4","figure")
    ],
    [
    Input("Reve","value"),
    Input("Visi","value"),
    ]
)

def update_graphs(Revenue,VisitorType):
    temp_df =df[(df.Revenue.apply(lambda x :x in Revenue) ) | (df.VisitorType.apply(lambda x :x in VisitorType) ) ]

    ### BiVarient Plot###
    groupped = temp_df.groupby(by='TrafficType',as_index=False).sum()
    fig = px.bar(groupped,x='TrafficType' ,y='Average_user_visit',orientation='v',color='TrafficType',title="Average User visits vs TrafficType",height=370)

    groupped = temp_df.groupby(by='Month',as_index=False).sum()
    figMo = px.bar(groupped,x='Month' ,y='Average_user_visit',orientation='v',color='Month',title="Amount of time spent on ProductRelated pages by month",height=370)
    figMo.update_layout(barmode='stack', xaxis={'categoryorder':'total descending'})

    groupped2 = temp_df.groupby(by='OperatingSystems',as_index=False).sum()
    figVi = px.bar(groupped2,x='OperatingSystems' ,y='Average_D',orientation='v',color='OperatingSystems',title="Average time spent on each session by OperatingSystems",height=370)


    groupped = temp_df.groupby(by='Region',as_index=False).sum()
    figR = px.bar(groupped,x='Region' ,y='Average_user_visit',orientation='v',color='Region',title="Average_user_visit by Region",height=370)
        
    return[fig,figMo,figVi,figR]

@app.callback([
    Output("Mul1","figure"),
    Output("Mul2","figure"),
    Output("Mul3","figure"),
    Output("Mul4","figure")
    ],
    [
     Input("multiwek","value"),
     Input("multimo","value")
    ]
    )
def update_graphs1(Weekend,Month):
    temp_df =df[(df.Weekend.apply(lambda x :x in Weekend) ) | (df.Month.apply(lambda x :x in Month) ) ]

    
        ### MultiVarient Plot###
    BoEx = px.scatter(temp_df,x= 'BounceRates',y='ExitRates',orientation ='v',color='Revenue', title="BounceRate vs ExitRates with Revenue",height=370)

    BoAv = px.scatter(temp_df,x= 'BounceRates',y='Average_user_visit',orientation ='v',color='OperatingSystems', title="BounceRate vs Average_user_visit and Operating Systems",height=370)

    PdPv = px.scatter(temp_df,x='ProductRelated_Duration',y='ProductRelated_Visited',orientation ='v',color='Revenue', title="ProductRelated_Visited vs ProductRelated_Duration with Revenue",height=370)


    Av_D= px.scatter(temp_df,x='Average_D',y='Average_user_visit',orientation ='v',color='Revenue', title="Average user visit vs Average Duration and Revenue",height=370)

    return[BoEx,BoAv,PdPv,Av_D]

if __name__ == '__main__':
    app.run_server(debug=False)