import dash
from dash import Dash, dcc, html, Input, Output, dash_table
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
from dash.exceptions import PreventUpdate
from datetime import date
import json

df=pd.read_csv('./assets/table.csv')
df1=pd.read_csv('./assets/state.csv')
Ownership=pd.read_csv('./assets/Ownership.csv')
Facility_Level=pd.read_csv('./assets/Facility_Level.csv')
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------


# naija_states = json.load(open("/home/suleiman/Music/nga.geojson", "r"))
# naija_states["features"][2]["properties"]["NAME_1"] ='Akwa-Ibom'
# naija_states["features"][14]["properties"]["NAME_1"] ='FCT'
# naija_states["features"][25]["properties"]["NAME_1"] ='Nasarawa'
# state_id_map = {}
# for feature in naija_states["features"]:
#     feature["id"] = feature["properties"]["ID_1"]
#     state_id_map[feature["properties"]["NAME_1"]] = feature["id"]
# df1["id"] = df1["State"].apply(lambda x: state_id_map[x])


#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
map1=px.scatter_mapbox(
    data_frame=df1,
    lat='lat',
    lon='long',
    color='State',
    size='Number_of_Doctors',
    width=900,
    opacity=1,
    title='Doctors by States',
    zoom=5,
    center=dict(lat=9.0820,lon=8.6753)
)
map1.update_traces(showlegend=False, mode='lines+markers+text', text=list(df1['Number_of_Doctors']), textfont=dict(color='#fff'))
map1.update_layout(
    {
'plot_bgcolor': 'rgba(0, 0, 0, 0)',
'paper_bgcolor': 'rgba(0, 0, 0, 0)',
},
    mapbox_style="carto-darkmatter",margin=dict(l=0, r=0, t=0, b=0))

#--------------------------------------------------------------------------------
#------------------------------------------------------------------------------
#df1=df1.sort_values('State',ascending = False)
kolor=[ '#b3b3b3']*len(df1)
bar1 =px.bar(
    data_frame=df1,
    x='No_of_facility',
    y='State',
    orientation='h',
    title='Total by States',
    height=900,
    text='No_of_facility',
    # template='plotly_dark',
)
bar1.update_layout(
    {
'plot_bgcolor': 'rgba(0, 0, 0, 0)',
'paper_bgcolor': 'rgba(0, 0, 0, 0)',
},
    margin=dict(l=0, r=0, t=30, b=10),
    #xaxis={'categoryorder':'total descending'},
    xaxis_visible=False,
    yaxis_title=None,
    yaxis=dict(
        categoryorder='category descending',
        color="#fff",
        tickfont=dict(family='Sherif',size=12,)),
    title =  dict(
        text ='Facilities By State',
        font =dict(family='Sherif',size=11,color = '#fff'),
))
bar1.update_traces(
    marker_color=kolor,
    textposition='outside',
    textfont=dict(size=12, color='#fff' )
    )
#df1=df1.sort_values('State',ascending = True)
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------


x=Facility_Level.groupby(by='Facility_Level',as_index=False).sum()

bar2=px.bar(
    x,
    x='ID',
    y='Facility_Level',
    text='ID',
    width=200,
    height=200,
   

)
bar2.update_layout(
    {
'plot_bgcolor': 'rgba(0, 0, 0, 0)',
'paper_bgcolor': 'rgba(0, 0, 0, 0)',
},
    margin=dict(l=0, r=0, t=60, b=0),
    xaxis_visible=False,
    yaxis_title=None,
    yaxis=dict(
    color="#fff",
    tickfont=dict(family='Sherif',size=11,)),
    title =  dict(text ='Ownership',font =dict(family='Sherif',size=14,color = '#fff'),
))
bar2.update_traces(
     marker_color=[ '#19d3f3','#b3b3b3','red',],
    showlegend=False,
    textposition='auto', #['inside', 'outside', 'auto'],
    textfont=dict(size=12, color='#fff' )
    )

#------------------------------------------------------------------------------
#------------------------------------------------------------------------------

pie1 =px.pie(
    data_frame=Ownership,
    values='ID',
    names='Ownership',
    labels={"ID":"Number"},
    hole=0.5,
    #title='Ownership',
    height=230,
    width=200,
    color_discrete_sequence=['#b3b3b3','#19d3f3']
)
pie1.update_traces(showlegend=False, textinfo='label+percent', textposition='outside', textfont=dict(color='#fff'))
pie1.update_layout({
'plot_bgcolor': 'rgba(0, 0, 0, 0)',
'paper_bgcolor': 'rgba(0, 0, 0, 0)',
},
margin=dict(l=0, r=0, t=0, b=0),
title =  dict(text ='Ownership',font =dict(family='Sherif',size=14,color = '#fff'))
)
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------


pie2 =px.pie(
    data_frame=Facility_Level,
    values='ID',
    names='Facility_Level',
    color_discrete_sequence=['#b3b3b3','#19d3f3', 'red'],
    #title='Facility Level',
    hole=0.5,
    height=250,
)
pie2.update_traces(showlegend=False,textinfo='percent', textposition='outside', textfont=dict(color='#fff'))
pie2.update_layout({
'plot_bgcolor': 'rgba(0, 0, 0, 0)',
'paper_bgcolor': 'rgba(0, 0, 0, 0)',
},
#legend=dict(orientation='h', itemsizing='constant', y=-2, x=-1),font=dict(color='#fff',size=8),
margin=dict(l=0, r=0, t=10, b=0),
title =  dict(text ='Facility Level',font =dict(family='Sherif',size=14,color = '#fff'))

)
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------


Doctor = f'{round((df1.Number_of_Doctors.sum())/1000)}K'
Dentists = f'{round((df1.Number_of_Dentists.sum())/1000)}K'
Nurses = f'{round((df1.Number_of_Nurses.sum())/1000)}K'
allied_health = f'{round((df1.Number_of_other_Health_personels.sum())/1000)}K'
Total = df1['No_of_facility'].sum()
today = date.today()

#------------------------------------------------------------------------------
#------------------------------------------------------------------------------





x=list(df1['State'])
#x.sort(reverse=False)
x.insert(0, 'Total')

#------------------------------------------------------------------------------
#------------------------------------------------------------------------------

app = dash.Dash( __name__,
    external_stylesheets=[dbc.themes.CYBORG]
)

app.layout = dbc.Container([
    dbc.Row( dbc.Col([html.H2(id='title',children='Distribution of Health Facilities',style={'color':'rgba(179, 179, 179, 1)'})],className='bod',style={'height':'60px',},),),
    dbc.Row([
    dbc.Col([
        dbc.Row([
            dbc.Col([
                dbc.Row([ 

                    dbc.Col(dcc.Dropdown(x,value='Total',id='dropdown',clearable=False,),className='bo'),
                    
                ]),
                
                dbc.Row([
                    dbc.Col([html.H3(id='Doctor',children=Doctor), html.H6('Doctors')],style={'height':'105px'},className='bod', 
                    width=6),
                    dbc.Col([html.H3(id='Dentists',children=Dentists), html.H6('Dentists') ], style={'height':'105px'},className='bod', width=6)
                ]),
                dbc.Row([
                    dbc.Col([html.H3(id='Nurses',children=Nurses),html.H6('Nurses')], style={'height':'105px'},className='bod', width=6),
                    dbc.Col([html.H3( id='allied_health', children=allied_health),html.H6('Allied Health')],style={'height':'105px'},className='bod', width=6)
                ]),
                dbc.Row(html.H5(dcc.Graph(id='pie1', figure=pie1), style={'height':'230px'},className='bode1'),className='bo'),
                dbc.Row(html.H5(dcc.Graph(id='bar2', figure=bar2,config={'modeBarButtonsToRemove': ['zoom2d', 'pan2d', 'select2d', 'lasso2d', 'zoomIn2d', 'zoomOut2d', 'autoScale2d', 'resetScale2d']}), style={'height':'215px'},className='bode2'),className='bo'),

            ],width=4),
            dbc.Col([

                dbc.Row(dbc.Col('Doctors by States',className='bod')),
                dbc.Row(dcc.Graph(id='map1', figure=map1, config={'modeBarButtonsToRemove': ['zoom2d', 'pan2d', 'select2d', 'lasso2d', 'zoomIn2d', 'zoomOut2d', 'autoScale2d', 'resetScale2d']}),className='bo',),
                
            dbc.Row(dbc.Container(dash_table.DataTable(df.to_dict('records'), [{"name": i, "id": i} for i in df.columns],
            
                style_data={
                'border': '2px solid black',
                #'border-color': '#090909',
                    #'overflow': 'hidden',
                    #'textOverflow': 'ellipsis', #use 'clip' to hide content
                    'maxWidth': '100%',
                    #'maxHeight': '110px',
                    'overflowY': 'scroll'
                },
                style_header={ 'border': '2px solid black','backgroundColor': 'rgba(6, 6, 6, 0.5)', 'color':'#19d3f3'},
    style_cell={
        'backgroundColor': 'rgb(26, 26, 26)',
        'color': '#fff',
        'textAlign': 'left'
    },
            
                            ),style={"maxHeight": "225px", "overflow": "auto"},), className='bod')

                ],className='bo',width=8),],),], width=9),
    dbc.Col(([

        dbc.Row(dbc.Col(f'Date: {today}',className='bod'),style={'color':'#fff'}),
        dbc.Row(dbc.Col([html.H2(id='Total', children=Total,),html.H5('Facilities'), ],style={'height':'130px'},className='bod')),
        dbc.Row(dbc.Container(dcc.Graph(id='bar1', figure=bar1, config={'modeBarButtonsToRemove': ['zoom2d', 'pan2d', 'select2d', 'lasso2d', 'zoomIn2d', 'zoomOut2d', 'autoScale2d', 'resetScale2d']}),style={"maxHeight": "525px", "overflow": "auto"}),className='bo',),
        dbc.Row(dbc.Col([html.Label(['Github: ', html.A('Sachimugu', href='#',)],style={'height':'25px'})],className='bod')),
    ]), width=3),
])])

#----------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------
print(df1[df1['State']=='Abia'])
@app.callback(
    Output(component_id='Doctor', component_property='children'),
    Output(component_id='Dentists', component_property='children'),
    Output(component_id='Nurses', component_property='children'),
    Output(component_id='allied_health', component_property='children'),
    Output(component_id='Total', component_property='children'),
    Output(component_id='bar1', component_property='figure'),
    Output(component_id='pie1', component_property='figure'),
    Output(component_id='bar2', component_property='figure'),
    #Output(component_id='map1', component_property='figure'),








    Input(component_id='dropdown', component_property='value'))

def update_figure(selected_state):

    if selected_state =='Total':
#-------------------------------------------------
#-------------------------------------------------
        uDoctor=Doctor
        uDentists=Dentists
        uNurses=Nurses
        uallied_health=allied_health
        uTotal=Total
#-------------------------------------------------
#-------------------------------------------------
        kolor=[ '#b3b3b3']*len(df1)
        ubar1=bar1.update_traces(marker_color=kolor)
#-------------------------------------------------
#-------------------------------------------------
        upie1=pie1
#-------------------------------------------------
#-------------------------------------------------
        ubar2=bar2
#-------------------------------------------------
#-------------------------------------------------
        # umap1=map1


        return uDoctor, uDentists, uNurses, uallied_health, uTotal, ubar1, upie1, ubar2, #umap1





    elif selected_state !='Total':

#-------------------------------------------------
#-------------------------------------------------
        uDoctor=df1[df1['State']==selected_state]['Number_of_Doctors']
        uDentists=df1[df1['State']==selected_state]['Number_of_Dentists']
        uNurses=df1[df1['State']==selected_state]['Number_of_Nurses']
        uallied_health=df1[df1['State']==selected_state]['Number_of_other_Health_personels']
        uTotal=df1[df1['State']==selected_state]['No_of_facility']

#-------------------------------------------------
#-------------------------------------------------
        kolor =  ['rgba(179, 179, 179, 1)']*len(df1)
        index=df1[df1['State']==selected_state].index[0]
        kolor[index] = '#19d3f3'
        ubar1=bar1.update_traces(marker_color=kolor)
#-------------------------------------------------
#-------------------------------------------------
        uOwnership=Ownership[Ownership['State']==selected_state]
        upie1 =px.pie(
            data_frame=uOwnership,
            values='ID',
            names='Ownership',
            labels={"ID":"Number"},
            hole=0.5,
            #title='Ownership',
            height=250,
            width=200,
            color_discrete_sequence=['#b3b3b3','#19d3f3']
        )
        upie1.update_traces(showlegend=False, textinfo='label+percent', textposition='outside', textfont=dict(color='#fff'))
        upie1.update_layout({
        'plot_bgcolor': 'rgba(0, 0, 0, 0)',
        'paper_bgcolor': 'rgba(0, 0, 0, 0)',
        },
        margin=dict(l=0, r=0, t=0, b=0),
        title =  dict(text ='',font =dict(family='Sherif',size=14,color = '#fff')))

#-------------------------------------------------
#-------------------------------------------------
        ux=Facility_Level[Facility_Level['State']==selected_state]
        ubar2=px.bar(
            ux,
            x='ID',
            y='Facility_Level',
            text='ID',
            width=200,
            height=200,
           

        )
        ubar2.update_layout(
            {
        'plot_bgcolor': 'rgba(0, 0, 0, 0)',
        'paper_bgcolor': 'rgba(0, 0, 0, 0)',
        },
            margin=dict(l=0, r=0, t=60, b=0),
            xaxis_visible=False,
            yaxis_title=None,
            yaxis=dict(
            color="#fff",
            tickfont=dict(family='Sherif',size=11,)),
            title =  dict(text ='Ownership',font =dict(family='Sherif',size=14,color = '#fff'),
        ))
        ubar2.update_traces(
             marker_color=[ '#19d3f3','#b3b3b3','red',],
            showlegend=False,
            textposition='auto', #['inside', 'outside', 'auto'],
            textfont=dict(size=12, color='#fff' )
            )
#-------------------------------------------------
#-------------------------------------------------

    #     x=df1[df1['State']==selected_state]
    #     umap1 = px.choropleth_mapbox(
    #         x,
    #         locations="id",
    #         geojson=naija_states,
    #         color='No_of_facility',
    #         hover_name="State",
    #         hover_data=["No_of_facility"],
    #         #title="India Population Density",
    #         mapbox_style="carto-darkmatter",
    #         center=dict(lat=9.0820,lon=8.6753),
    #         width=400,
    #         opacity=0.9,
    #         zoom=4,
    #         #color_discrete_sequence=['red']*len(df1)

    #     )
    #     umap1.update_traces(showlegend=False, text=list(df1['No_of_facility']),)
    #     umap1.update_layout(
    #         {
    #     'plot_bgcolor': 'rgba(0, 0, 0, 0)',
    #     'paper_bgcolor': 'rgba(0, 0, 0, 0)',
    #     },
    # mapbox_style="carto-darkmatter",margin=dict(l=0, r=0, t=0, b=0))
    #     umap1.update_coloraxes(showscale=False)

        return uDoctor, uDentists, uNurses, uallied_health, uTotal, ubar1, upie1, ubar2, #umap1



# @app.callback(
#     Output(component_id='Doctor', component_property='children'),)
    






if __name__ == '__main__':
    app.run_server(debug=True, port=8081)