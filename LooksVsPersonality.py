# Import Important Libararies
from tkinter.ttk import Style
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
from dash import Dash,dcc,html
from dash_bootstrap_templates import load_figure_template
import dash_bootstrap_components as dbc
from dash.dependencies import Input,Output
import grasia_dash_components as gdc
import time


# Load Dataset
data = pd.read_csv('G:/Dataset/LooksvsPersonalityWithIsoAlpha.csv')
print(data.info())
dataForValues = pd.read_csv('G:/Dataset/LooksvsPersonalityNumbers.csv')
LooksPersonalityDF_Survey = pd.read_csv("G:/Dataset/LooksvsPersonalitySurveyAll.csv")

# Bootstarp theme templalets
templates = [
    "bootstrap",
    "minty",
    "pulse",
    "flatly",
    "quartz",
    "cyborg",
    "darkly",
    "vapor",
]
# Loading these templates
load_figure_template(templates)

# Creating Dash with theme = Darkly 
app = Dash(__name__, external_stylesheets=[dbc.themes.DARKLY])

nationality_card = dbc.Card([
    dbc.CardImg()
    ,dbc.CardBody([
        dcc.RadioItems(id= 'Radioitem',options=[{'label': str(i), 'value': str(i)} for i in data['Gender'].unique()] , value=['Men'])
    ])
])
card_content_Total = [
    dbc.CardBody(
        [
            html.H5("Total Number", className="card-title" ,style={'font-size': '100%' , 'text-align': 'center' , 'color':"#40DFEF"} ),
            html.P(
                "3.8K",
                className="card-text", style={ 'font-size': '200%' , 'text-align': 'center' ,'color':"#40DFEF"}
            ),

        ]
    ),
]

card_content_Nationality = [
    dbc.CardBody(
        [
            html.H5("Total Number OF Nationalities", className="card-title" ,style={ 'font-size': '100%' , 'text-align': 'center' , 'color':"#40DFEF"} ),
            html.P(  
                "19",
                className="card-text", style={ 'font-size': '200%' , 'text-align': 'center' ,'color':"#40DFEF"}
            ),

        ]
    ),
]
card_content_ForEachNationality = [
    dbc.CardBody(
        [
            html.H5("Total Number OF For Each Nationality", className="card-title" ,style={ 'font-size': '100%' , 'text-align': 'center' , 'color':"#40DFEF"} ),
            html.P(  
                "200",
                className="card-text", style={ 'font-size': '200%' , 'text-align': 'center' ,'color':"#40DFEF"}
            ),

        ]
    ),
]
card_content_personality = [
    dbc.CardBody(
        [
            html.H5("Ranked personality higher than looks", className="card-title" ,style={ 'font-size': '100%' , 'text-align': 'center' , 'color':"#40DFEF"} ),
            html.P(
                id= 'OutDropDownpersonality',
                className="card-text", style={ 'font-size': '200%' , 'text-align': 'center' ,'color':"#40DFEF"}
            ),

        ]
    ),
]
card_content_Looks = [
    dbc.CardBody(
        [
            html.H5("Ranked looks higher than personality", className="card-title" ,style={ 'font-size': '100%' , 'text-align': 'center' , 'color':"#40DFEF"} ),
            html.P(
                id= 'OutDropDownLooks',
                className="card-text", style={ 'font-size': '200%' , 'text-align': 'center' ,'color':"#40DFEF"}
            ),

        ]
    ),
]
card_content_Men = [
    dbc.CardBody(
        [
            html.H5("Number Of Men", className="card-title" ,style={ 'font-size': '100%' , 'text-align': 'center' , 'color':"#40DFEF"} ),
            html.P(
                38,
                className="card-text", style={ 'font-size': '200%' , 'text-align': 'center' ,'color':"#40DFEF"}
            ),

        ]
    ),
]
card_content_Women = [
    dbc.CardBody(
        [
            html.H5("Number Of Women", className="card-title" ,style={ 'font-size': '100%' , 'text-align': 'center' , 'color':"#40DFEF"} ),
            html.P(
                38,
                className="card-text", style={ 'font-size': '200%' , 'text-align': 'center' ,'color':"#40DFEF"}
            ),

        ]
    ),
]
card_content_Total_Survey = [
    dbc.CardBody(
        [
            html.H5("Total Number ", className="card-title" ,style={ 'font-size': '100%' , 'text-align': 'center' , 'color':"#40DFEF"} ),
            html.P(
                76,
                className="card-text", style={ 'font-size': '200%' , 'text-align': 'center' ,'color':"#40DFEF"}
            ),

        ]
    ),
]


graphs = html.Div([
    dcc.Tabs( [
        dcc.Tab(label='Romantic Partner', children=[
            dbc.Row(
            [
            dbc.Col(lg=1)   ,
            dbc.Col(dbc.Card(card_content_Nationality, color="secondary", inverse=True , outline=True, style={"width": "12rem" , "height": "7rem" ,'backgroundColor': 'secondary' })),
            dbc.Col(dbc.Card(card_content_personality, color="secondary", inverse=True , outline=True, style={"width": "12rem" , "height": "7rem" ,'backgroundColor': 'secondary' })),
            dbc.Col(dbc.Card(card_content_Total, color="secondary", inverse=True , outline=True, style={"width": "12rem" , "height": "7rem" ,'backgroundColor': 'secondary' })),
            dbc.Col(dbc.Card(card_content_Looks, color="secondary", inverse=True , outline=True, style={"width": "12rem" , "height": "7rem" ,'backgroundColor': 'secondary' })),
            dbc.Col(dbc.Card(card_content_ForEachNationality, color="secondary", inverse=True , outline=True, style={"width": "12rem" , "height": "7rem" ,'backgroundColor': 'secondary' })),
                
                ]),
    dbc.Row([
        dbc.Col( html.P('What is the most important characteristic of a romantic partner?') ,  style={'backgroundColor': '#212121', 'color': 'White', 'font-size': '180%'  } ,lg=6),
            dbc.Col(dcc.Dropdown(id= 'DropDownForNumber',options=[{'label': str(i), 'value': str(i)} for i in data['Nationality'].unique()]  , value='American' , style={'height' : '100' , 'width' : '150'}),lg = 4 , style={'backgroundColor': '#212121', 'color': 'black', 'font-size': '150%'  }) ,
            dbc.Col(lg=2)

        ],
            className="mt-4" ),
    dbc.Row([
        dbc.Col(dcc.Graph(id  = 'nationality_compare' , style={'backgroundColor': 'black', 'color': 'black' } ) , lg=10) 
        ,dbc.Col( id="imgPartner",lg=2)
        ],
            className="mt-4" ),
    dbc.Row([
            dbc.Col( html.Hr(style={"height":"15px","border-width":"10","margin-top": "3em","color":"gray","background-color":"gray","margin-bottom": "2em"}))
        ])
        ,
    dbc.Row([
        dbc.Col(lg=1),
        dbc.Col( html.P(id ='My_Second_Q' ) ,  style={'backgroundColor': '#212121', 'color': 'White', 'font-size': '150%'  } , lg=3)
        ],
            className="mt-4" ),
    dbc.Row([
        dbc.Col(lg=1),
        dbc.Col(dcc.RadioItems(id= 'Radioitem',options=[{'label': str(i), 'value': str(i)} for i in data['Gender'].unique()]  , value='Men' ,  labelStyle={'display': 'block'}),lg = 3 , style={'backgroundColor': '#212121', 'color': 'White', 'font-size': '150%'  })
        ,dbc.Col(lg=3)
        ,dbc.Col( html.P('Which Country Favour Personality In a Partner?' ) ,  style={'backgroundColor': '#212121', 'color': 'White', 'font-size': '140%'  } )

        ],
            className="mt-4" ),
    dbc.Row([
        dbc.Col(id="IFrame",lg=5),
        dbc.Col(id="img",lg=2)
        ,dbc.Col(dcc.Graph(id  = 'Map_Compare' , style={'backgroundColor': 'black', 'color': 'black',"width": "40rem" , "height": "28rem"}),lg=5),

        ],
            className="mt-4" )
    ] ,  style={'backgroundColor': '#212121', 'color': '#CBE7E8', 'font-size': '150%'  } ,selected_style= {'backgroundColor': '#212121', 'color': '#CBE7E8', 'font-size': '150%'}) , 
        dcc.Tab(label='When People Look For Love' ,children=[ 
            dbc.Row([
            dbc.Col( html.P(id ='My_Forth_Q' ) ,  style={'backgroundColor': '#212121', 'color': 'White', 'font-size': '150%',  "margin-top": "3rem"} ) ,
            ])  
            , dbc.Row([
            dbc.Col(dcc.Dropdown(id= 'myDropDown_Most_Highly_nations',options=[{'label': str(i), 'value': str(i)} for i in data['Nationality'].unique()]  , value='American'  , style={'height' : '100' , 'width' : '200'}),lg = 7 , style={'backgroundColor': '#212121', 'color': 'black', 'font-size': '150%'  }) 
    ])
            ,dbc.Row([
            dbc.Col(dcc.Graph(id  = 'Most_Highly_nations' , style={'backgroundColor': 'black', 'color': 'black' , } ), lg=10),
            dbc.Col(id="imgPL" , lg=2) 
        ],
            className="mt-4" ), 
        dbc.Row([
            dbc.Col( html.Hr(style={"height":"15px","border-width":"10","margin-top": "4em","color":"gray","background-color":"gray","margin-bottom": "5em"}))
        ])
        ,dbc.Row([
        dbc.Col( html.P(id ='My_Third_Q' ) ,  style={'backgroundColor': '#212121', 'color': 'White', 'font-size': '140%'  } )
        ,dbc.Col( html.P(id ='My_Fifth_Q' ) ,  style={'backgroundColor': '#212121', 'color': 'White', 'font-size': '140%'  } )

])     
        ,dbc.Row([
        dbc.Col(dcc.Dropdown(id= 'myDropDown_money_and_Appearance_all_nations',options=[{'label': str(i), 'value': str(i)} for i in data['Gender'].unique()]  , value="Men"  , style={'height' : '100' , 'width' : '200'}),lg = 5 , style={'backgroundColor': '#212121', 'color': 'black', 'font-size': '150%'  }) 
        ,dbc.Col(lg=1)
        ,dbc.Col(dcc.Dropdown(id= 'myDropDown_AllQs',options=[{'label': str(i), 'value': str(i)} for i in data['Q'].unique()]  , value="They are good looking"  , style={'height' : '100' , 'width' : '200'}),lg = 5 , style={'backgroundColor': '#212121', 'color': 'black', 'font-size': '150%'  }) 

])    
        ,dbc.Row([
        dbc.Col(dcc.Graph(id  = 'money_all_nations_Gender' , style={'backgroundColor': 'black', 'color': 'black', "height": "35rem"} ),lg = 6  )
        ,dbc.Col(dcc.Graph(id  = 'Appearance_all_nations' , style={'backgroundColor': 'black', 'color': 'black',"height": "35rem"} ),lg = 6  )

        ],
            className="mt-4" )  
        ] , style={'backgroundColor': '#212121', 'color': '#CBE7E8', 'font-size': '150%' } , selected_style= {'backgroundColor': '#212121', 'color': '#CBE7E8', 'font-size': '150%'} ),
        dcc.Tab(label='Nowadays' ,children=[ 
    dbc.Row(
            [
            dbc.Col(lg=2)   ,
            dbc.Col(dbc.Card(card_content_Men, color="secondary", inverse=True , outline=True, style={"width": "12rem" , "height": "7rem" ,'backgroundColor': 'secondary' })),
            dbc.Col(dbc.Card(card_content_Total_Survey, color="secondary", inverse=True , outline=True, style={"width": "12rem" , "height": "7rem" ,'backgroundColor': 'secondary' })),
            dbc.Col(dbc.Card(card_content_Women, color="secondary", inverse=True , outline=True, style={"width": "12rem" , "height": "7rem" ,'backgroundColor': 'secondary' })),
                
                ]),
    dbc.Row([
        dbc.Col(lg=2),
        dbc.Col( html.P('Nowadays, What are the most important looks or personality?') ,  style={'backgroundColor': '#212121', 'color': 'White', 'font-size': '180%'  } )
        ],
            className="mt-4" ),
    dbc.Row([
        dbc.Col(id="imgMale"),
        dbc.Col(id="IFrameGoodLooking"),
        dbc.Col(id="IFramePersonality"),
        dbc.Col(id="imgFemale")
        ],
            className="mt-4" ),
    dbc.Row([
            dbc.Col( html.Hr(style={"height":"15px","border-width":"10","color":"gray","background-color":"gray","margin-bottom": "2em"}))
        ]),
    dbc.Row([
        dbc.Col(lg=1),
        dbc.Col(dcc.Graph(id  = 'SurveySenseOfHumor' , style={'backgroundColor': 'black', 'color': 'black' } ), lg=2),
        dbc.Col(id="imgPLTap31" , lg=2),
        dbc.Col(dcc.Graph(id  = 'SurveyMoney' , style={'backgroundColor': 'black', 'color': 'black' } ), lg=2 ),
        dbc.Col(id="imgPLTap32" , lg=2),
        dbc.Col(dcc.Graph(id  = 'SurveyIntelligent' , style={'backgroundColor': 'black', 'color': 'black' } ), lg=2 ),
        dbc.Col(lg=1)
        ],
            className="mt-4" )
        ] , style={'backgroundColor': '#212121', 'color': '#CBE7E8', 'font-size': '150%' } , selected_style= {'backgroundColor': '#212121', 'color': '#CBE7E8', 'font-size': '150%'} )
        ] , style={'backgroundColor': '#212121', 'color': 'White'} )
])

heading = html.H1("Looks Vs Personality",className="bg-primary text-white p-2" , style={'text-align': 'center'})


app.layout = dbc.Container([heading, graphs], fluid=True)

## What is the most important characteristic of a romantic partner?
@app.callback(
    Output(component_id='nationality_compare' , component_property='figure'),
    Input(component_id='DropDownForNumber' , component_property='value')
)
def UpdateALL(Radioitemvalue) :
        filtered_df = data[(data['Rank']=='Ranked first') & (data.Nationality==Radioitemvalue)]
        fig=px.bar(filtered_df, x='Gender',y='Percentage', color = 'Gender',color_discrete_map = {'Women':'#E78EA9','Men':'#40DFEF'} , barmode ='group' ,facet_col='Q',template='darkly',
        category_orders={"Q": ["They have a personality I like", "They are good looking", "They have similar interests to me","They have a sense of humour","They are intelligent","They have a decent amount of money"]}  
        )
        return fig
## Image Of What is the most important characteristic of a romantic partner?
@app.callback(
    Output(component_id='imgPartner' , component_property='children'),
    Input(component_id='Radioitem' , component_property='value')
)
def UpdateALL(Radioitemvalue) :
        return html.Img(src=app.get_asset_url('FirstTap.png'))
## Cards Of Numbers Of What is the most important characteristic of a romantic partner?
@app.callback(
    Output(component_id='OutDropDownpersonality' , component_property='children'),
    Input(component_id='DropDownForNumber' , component_property='value')
)
def UpdateALL(dropdownvalue) :
        X=dataForValues[(dataForValues['Gender']=='Men') & (dataForValues.Nationality==dropdownvalue) & (dataForValues['Measure'] =='Ranked personality higher than looks')] 
        Y=dataForValues[(dataForValues['Gender']=='Women') & (dataForValues.Nationality==dropdownvalue) & (dataForValues['Measure'] =='Ranked personality higher than looks')] 
        Sum = X['Value'].values + Y['Value'].values
        return Sum

@app.callback(
    Output(component_id='OutDropDownLooks' , component_property='children'),
    Input(component_id='DropDownForNumber' , component_property='value')
)
def UpdateALL(dropdownvalue) :
        X=dataForValues[(dataForValues['Gender']=='Men') & (dataForValues.Nationality==dropdownvalue) & (dataForValues['Measure'] =='Ranked looks higher than personality')] 
        Y=dataForValues[(dataForValues['Gender']=='Women') & (dataForValues.Nationality==dropdownvalue) & (dataForValues['Measure'] =='Ranked looks higher than personality')] 
        Sum = X['Value'].values + Y['Value'].values
        return Sum

#  Which Country Favour Personality In a Partner?
@app.callback(
    Output(component_id='Map_Compare' , component_property='figure'),
    Input(component_id='Radioitem' , component_property='value')
)
def UpdateALL(Radioitemvalue) :
    Filtered_data = data[(data['Rank']=='Ranked first') & (data['Q']=='They have a personality I like')]
    fig = px.choropleth(Filtered_data, locations="iso_alpha",
                        color="country",
                        color_discrete_map = {'United States':'#FFD93D' ,
                                'Australia' : '#FF6B6B' , 'United Kingdom' : '#6BCB77' , 'Denmark': '#4D96FF'
                                ,'Egypt' : '#F24A72' , 'Philippines' : '#FDAF75' , 'Finland': '#9ADCFF'
                                ,'France' : '#9ADCFF' , 'Germany' : '#FFF89A' , 'Hong Kong, China': '#FFB2A6' 
                                ,'India' : '#FF8AAE' , 'Indonesia' : '#655D8A' , 'Malaysia': '#7897AB' 
                                ,'Norway' : '#D885A3' , 'Singapore' : '#FDCEB9' , 'Sweden': '#40DFEF' 
                                ,'Thailand' : '#B9F8D3' , 'United Arab Emirates' : '#FFFBE7' , 'Vietnam': '#E78EA9' },
                        projection="natural earth",hover_name="country" )
    return fig

# Question Of What Do Men/Women Want?
@app.callback(
    Output(component_id='My_Second_Q' , component_property='children'),
    Input(component_id='Radioitem' , component_property='value')
)
def UpdateALL(Radioitemvalue) :
        return "What Do "+ Radioitemvalue +" Want? "
    
# What Do Men/Women Want?
@app.callback(
    Output(component_id='IFrame' , component_property='children'),
    Input(component_id='Radioitem' , component_property='value')
)
def UpdateALL(Radioitemvalue) :
    if Radioitemvalue=="Men":
        return html.Iframe(src="assets\TestMen.html" , style={ "width": "50rem" , "height": "30rem" })
    elif Radioitemvalue=="Women":
        return html.Iframe(src="assets\TestWomen.html" , style={ "width": "50rem" , "height": "30rem" })

# Image Of What Do Men/Women Want?
@app.callback(
    Output(component_id='img' , component_property='children'),
    Input(component_id='Radioitem' , component_property='value')
)
def UpdateALL(Radioitemvalue) :
    if Radioitemvalue=="Men":
        return html.Img(src=app.get_asset_url('man.png') )
    elif Radioitemvalue=="Women":
        return html.Img(src=app.get_asset_url('woman.png') )

# Question Of When People Look For Love, What Is The Thing They prioritize Most Highly? According To (Nationality)
@app.callback(
    Output(component_id='My_Forth_Q' , component_property='children'),
    Input(component_id='myDropDown_Most_Highly_nations' , component_property='value')
)
def UpdateALL(dropdownvalue) :
        return "When People Look For Love, What Is The Thing They prioritize Most Highly? According To " + dropdownvalue
    
# When People Look For Love, What Is The Thing They prioritize Most Highly? According To (Nationality) 
@app.callback(
    Output(component_id='Most_Highly_nations' , component_property='figure'),
    Input(component_id='myDropDown_Most_Highly_nations' , component_property='value')
)
def UpdateALL(dropdownvalue) :
        filtered_df=data[(data.Nationality==dropdownvalue)]
        anotherDF = filtered_df.groupby('Q').sum()
        fig=px.bar(filtered_df ,y='Q', x='Percentage', color='Gender', barmode='group' ,color_discrete_map ={'Women':'#FCBE4F','Men':'#5CBFC5'}, facet_col='Rank' ,template='darkly' )     
        return fig
# Image Of When People Look For Love, What Is The Thing They prioritize Most Highly? According To (Nationality)   
@app.callback(
    Output(component_id='imgPL' , component_property='children'),
    Input(component_id='Radioitem' , component_property='value')
)
def UpdateALL(Radioitemvalue) :
        return html.Img(src=app.get_asset_url('PersonalityLooks.png') )

# Question Of when looking for love, which nations prize money above all else? According To (Gender)
@app.callback(
    Output(component_id='My_Third_Q' , component_property='children'),
    Input(component_id='myDropDown_money_and_Appearance_all_nations' , component_property='value')
)
def UpdateALL(dropdownvalue) :
    return "when looking for love, which nations prize money above all else? According To " + dropdownvalue

# When looking for love, which nations prize money above all else? According To (Gender)
@app.callback(
    Output(component_id='money_all_nations_Gender' , component_property='figure'),
    Input(component_id='myDropDown_money_and_Appearance_all_nations' , component_property='value')
)
def UpdateALL(dropdownvalue) :
        filtered_df=data[(data.Gender==dropdownvalue) & (data['Rank']=='Ranked first') & (data['Q']=='They have a decent amount of money')]
        fig=px.scatter(filtered_df ,y='Percentage', x='Nationality', size='Percentage' ,color='Nationality',template='darkly' ,color_discrete_map = {'American':'#FF6B6B' ,
                                'Australian' : '#FFD93D' , 'British' : '#6BCB77' , 'Danish': '#4D96FF'
                                ,'Egyptian' : '#F24A72' , 'Filipino' : '#FDAF75' , 'Finnish': '#9ADCFF'
                                ,'French' : '#9ADCFF' , 'German' : '#FFF89A' , 'Hong Kong': '#FFB2A6' 
                                ,'Indian' : '#FF8AAE' , 'Indonesian' : '#655D8A' , 'Malaysian': '#7897AB' 
                                ,'Norwegian' : '#D885A3' , 'Singaporean' : '#FDCEB9' , 'Swedish': '#40DFEF' 
                                ,'Thai' : '#B9F8D3' , 'UAE' : '#FFFBE7' , 'Vietnamese': '#E78EA9' })     
        return fig
# Question Of Which Nations Favour (Q) In a Partner?
@app.callback(
    Output(component_id='My_Fifth_Q' , component_property='children'),
    Input(component_id='myDropDown_AllQs' , component_property='value')
)
def UpdateALL(dropdownvalue) :
    if dropdownvalue=='They are good looking' :
        return "Which Nations Favour looking In a Partner?"
    elif dropdownvalue=='They have a personality I like':
        return "Which Nations Favour personality In a Partner?"
    elif dropdownvalue=='They have a sense of humour' :
        return "Which Nations Favour sense of humour In a Partner?"
    elif dropdownvalue=='They are intelligent' :
        return "Which Nations Favour intelligent In a Partner?"
    elif dropdownvalue=='They have a decent amount of money' :
        return "Which Nations Favour money In a Partner?"
    elif dropdownvalue=='They have similar interests to me' :
        return "Which Nations Favour similar interests In a Partner?"
    
# Which Nations Favour (Q) In a Partner?
@app.callback(
    Output(component_id='Appearance_all_nations' , component_property='figure'),
    Input(component_id='myDropDown_AllQs' , component_property='value')
)
def UpdateALL(dropdownvalue) :
        filtered_df=data[(data.Q==dropdownvalue) & (data['Rank']=='Ranked first') ]
        fig=px.area(filtered_df, x='Nationality' ,y='Percentage' ,color="Nationality" , template='darkly' , color_discrete_map = {'American':'#FF6B6B' ,
                                'Australian' : '#FFD93D' , 'British' : '#6BCB77' , 'Danish': '#4D96FF'
                                ,'Egyptian' : '#F24A72' , 'Filipino' : '#FDAF75' , 'Finnish': '#9ADCFF'
                                ,'French' : '#9ADCFF' , 'German' : '#FFF89A' , 'Hong Kong': '#FFB2A6' 
                                ,'Indian' : '#FF8AAE' , 'Indonesian' : '#655D8A' , 'Malaysian': '#7897AB' 
                                ,'Norwegian' : '#D885A3' , 'Singaporean' : '#FDCEB9' , 'Swedish': '#40DFEF' 
                                ,'Thai' : '#B9F8D3' , 'UAE' : '#FFFBE7' , 'Vietnamese': '#E78EA9' } )     
        return fig

# Nowadays, What are the most important looks or personality?
@app.callback(
    Output(component_id='IFrameGoodLooking' , component_property='children'),
    Input(component_id='Radioitem' , component_property='value')
)
def UpdateALL(Radioitemvalue) :
        return html.Iframe(src="assets\GoodLooking.html" , style={ "width": "40rem" , "height": "30rem" })

@app.callback(
    Output(component_id='IFramePersonality' , component_property='children'),
    Input(component_id='Radioitem' , component_property='value')
)
def UpdateALL(Radioitemvalue) :
        return html.Iframe(src="assets\Personality.html" , style={ "width": "40rem" , "height": "30rem" })

# Images Of Nowadays, What are the most important looks or personality?
@app.callback(
    Output(component_id='imgMale' , component_property='children'),
    Input(component_id='Radioitem' , component_property='value')
)
def UpdateALL(Radioitemvalue) :
        return html.Img(src=app.get_asset_url('Male.png') )
@app.callback(
    Output(component_id='imgFemale' , component_property='children'),
    Input(component_id='Radioitem' , component_property='value')
)
def UpdateALL(Radioitemvalue) :
        return html.Img(src=app.get_asset_url('Female.png') )

# Pies Of They have a sense of humour , They have a decent amount of money, and They are intelligent
@app.callback(
    Output(component_id='SurveySenseOfHumor' , component_property='figure'),
    Input(component_id='Radioitem' , component_property='value')
)
def UpdateALL(dropdownvalue) :
        filtered_df=LooksPersonalityDF_Survey[((LooksPersonalityDF_Survey['Your partner has a sense of humor']==6) )]
        fig=px.pie(filtered_df,  names='Gender' ,values='Percentage sense of humor', hole=.3,color='Gender',color_discrete_map ={'Women':'#998DD8','Men':'#0065FF'} ,title="They have a sense of humour ",  height=400 , width=350 , template='darkly')
        return fig

@app.callback(
    Output(component_id='SurveyMoney' , component_property='figure'),
    Input(component_id='Radioitem' , component_property='value')
)
def UpdateALL(dropdownvalue) :
        filtered_df=LooksPersonalityDF_Survey[((LooksPersonalityDF_Survey['Your partner have/make a decent amount of money "Abo Hashema Style"']==6) )]
        fig=px.pie(filtered_df,  names='Gender' ,values='Percentage money', hole=.3,color='Gender',color_discrete_map ={'Women':'#FF8E72','Men':'#0065FF'} ,title="They have a decent amount of money ",  height=400 , width=350 , template='darkly')
        return fig

@app.callback(
    Output(component_id='SurveyIntelligent' , component_property='figure'),
    Input(component_id='Radioitem' , component_property='value')
)
def UpdateALL(dropdownvalue) :
        filtered_df=LooksPersonalityDF_Survey[((LooksPersonalityDF_Survey['Your partner has to be intelligent']==6) )]
        fig=px.pie(filtered_df,  names='Gender' ,values='Percentage intelligent',hole=.3, color='Gender' ,color_discrete_map ={'Women':'#79F2C0','Men':'#0065FF'},title="They are intelligent ",  height=400 , width=350 , template='darkly')
        return fig

# Images Of They have a sense of humour , They have a decent amount of money, and They are intelligent
@app.callback(
    Output(component_id='imgPLTap31' , component_property='children'),
    Input(component_id='Radioitem' , component_property='value')
)
def UpdateALL(Radioitemvalue) :
        return html.Img(src=app.get_asset_url('LP1.png') )
@app.callback(
    Output(component_id='imgPLTap32' , component_property='children'),
    Input(component_id='Radioitem' , component_property='value')
)
def UpdateALL(Radioitemvalue) :
        return html.Img(src=app.get_asset_url('LP2.png') )


app.run_server()

