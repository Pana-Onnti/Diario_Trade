from flask import Flask, render_template
import plotly.express as px
import pandas as pd
import plotly.io as pio
import plotly.graph_objects as go

app = Flask(__name__)

@app.route("/")
def index():
    def grafico():
        df = px.data.stocks(indexed=True) - 1
        fig = px.area(df, x=df.index, y="GOOG")
        fig.update_layout(xaxis=dict(showgrid=False, zeroline=False, showticklabels=False, title=None, tickmode='array', ticks=''),
                          yaxis=dict(showgrid=False, zeroline=False, showticklabels=False, title=None, tickmode='array', ticks=''))
        fig.update_traces(line={'color': '#3782cd'})
        fig.update_traces(line=dict(width=1.5))

        fig.update_layout(
            autosize=False,
            width=200,
            height=100,
            margin=dict(l=1, r=1, b=1, t=1, pad=1),
            paper_bgcolor="white",
            hovermode=False
        )
        fig.update_layout(plot_bgcolor='rgba(26, 28, 45, 1)')
        #

        config = {'displayModeBar': False,'responsive': True}

        graph = pio.to_html(fig, full_html=False, config=config)
        return graph
    def grafico1():
        df = px.data.stocks(indexed=True) - 1
        fig = px.area(df, x=df.index, y="MSFT")
        fig.update_layout(xaxis=dict(showgrid=False, zeroline=False, showticklabels=False, title=None, tickmode='array', ticks=''),
                          yaxis=dict(showgrid=False, zeroline=False, showticklabels=False, title=None, tickmode='array', ticks=''))
        fig.update_traces(line={'color': '#3782cd'})
        fig.update_traces(line=dict(width=1.5))

        fig.update_layout(
            autosize=False,
            width=200,
            height=100,
            margin=dict(l=1, r=1, b=1, t=1, pad=1),
            paper_bgcolor="white",
            hovermode=False
        )
        fig.update_layout(plot_bgcolor='rgba(26, 28, 45, 1)')
        #

        config = {'displayModeBar': False,'responsive': True}

        graph = pio.to_html(fig, full_html=False, config=config)
        return graph
    def graficopie():
        values = [4500, 2500]

        fig = go.Figure(data=[go.Pie(labels=None, values=values, hole=.8, marker=dict(colors=['#9b3232',  '#4D5F2F']))])
        # configurar opciones de visualización
        fig.update_traces(textinfo='none', showlegend=False)
    
        # establecer títulos en None
        fig.update_layout(title=None)
        fig.update_layout(
            autosize=False,
            width=200,
            height=100,
            margin=dict(l=1, r=1, b=15, t=15, pad=1),
            paper_bgcolor="rgba(26, 28, 45, 1)",
            hovermode=False
        )
        # configurar opciones de visualización
        fig.update_layout(plot_bgcolor='rgba(26, 28, 45, 1)')
        config = {'displayModeBar': False,'responsive': True}

        graph = pio.to_html(fig, full_html=False, config=config)
        return graph
    def graficobar():
        import plotly.express as px

        df = px.data.gapminder().query("continent == 'Europe' and year == 2007 and pop > 2.e6")
        fig = px.bar(df, y='pop', x='country', text='pop')
        fig.update_layout(title=None)
        fig.update_layout(
            autosize=False,
            width=400,
            height=600,
            margin=dict(l=1, r=10, b=15, t=15, pad=1),
            paper_bgcolor="rgba(26, 28, 45, 1)",
            hovermode=False,
            plot_bgcolor="#7F8C8D"
            
        )
        fig.update_traces(texttemplate='%{text:.2s}', textposition='outside')
        fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
        fig.update_layout(plot_bgcolor='rgba(26, 28, 45, 1)')
        fig.update_traces(marker_color='#3782cd')
        fig.update_layout(xaxis=dict(zeroline=False, showgrid=False),
                  yaxis=dict(zeroline=False, showgrid=False))
        fig.update_xaxes(showgrid=False, tickfont=dict(color='hsla(208, 100%, 97%, 0.616)'))
        fig.update_yaxes(showgrid=False, tickfont=dict(color='hsla(208, 100%, 97%, 0.616)'))
        fig.update_layout(plot_bgcolor='rgba(26, 28, 45, 1)',showlegend=False)


        config = {'displayModeBar': False,'responsive': True}

        graph = pio.to_html(fig, full_html=False, config=config)
        return graph
    
    def graficoultimo():
        
        years = ['2016','2017','2018','2019']

        fig = go.Figure()
        
        fig.add_trace(go.Bar(x=years, y=[500, 600, 700],
                        base=[-500,-600,-700],
                        marker_color='#4D5F2F',
                        name='expenses'))
        fig.add_trace(go.Bar(x=years, y=[300, 400, 700],
                        base=0,
                        marker_color='#9b3232',
                        name='revenue'
                        ))
        fig.update_layout(title=None)
        fig.update_layout(
            autosize=False,
            width=300,
            height=600,
            margin=dict(l=1, r=1, b=15, t=15, pad=1),
            paper_bgcolor="rgba(26, 28, 45, 1)",
            hovermode=False,
            plot_bgcolor="#7F8C8D"
            
            
        )
        fig.update_layout(plot_bgcolor='rgba(26, 28, 45, 1)',showlegend=False)
        fig.update_layout(xaxis=dict(zeroline=False, showgrid=False), 
                  yaxis=dict(zeroline=False, showgrid=False))
        fig.update_xaxes(showgrid=False, tickfont=dict(color='hsla(208, 100%, 97%, 0.616)'))
        fig.update_yaxes(showgrid=False, tickfont=dict(color='hsla(208, 100%, 97%, 0.616)'))


        config = {'displayModeBar': False,'responsive': True}

        graph = pio.to_html(fig, full_html=False, config=config)
        return graph
    
    return render_template('grafico.html', graph=grafico(),graph1=grafico1(),graph2=grafico1(),graph3=graficopie(),graph4=graficobar(),graph5=graficoultimo())

