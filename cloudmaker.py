import dash
import dash.dependencies as dd
import dash_core_components as dcc
import dash_html_components as html
from parser import freqs
from sandbox import mask
from io import BytesIO

from wordcloud import WordCloud, ImageColorGenerator
import base64

# external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
image_colors = ImageColorGenerator(mask)
app = dash.Dash(__name__) #, external_stylesheets=external_stylesheets)


app.layout = html.Div([
    html.Img(id="image_wc"),
])

#/usr/share/fonts/truetype/msttcorefonts/times.ttf
#/home/t/.local/share/fonts/FeFCrm27C.otf"
#/home/t/Téléchargements/oldnewspapertypes/OldNewspaperTypes.ttf

def plot_wordcloud(data):
    d = data
    wc = WordCloud(background_color='white',
                   font_path="/usr/share/fonts/truetype/msttcorefonts/times.ttf",
                   max_words = 2000,
                   mask=mask,
                   width=1024,
                   height=1024,
                   max_font_size=90,
                   min_font_size=5,
                   mode='RGBA'
                   )
    wc.fit_words(d)
    wc.recolor(color_func=image_colors)

    return wc.to_image()

@app.callback(dd.Output('image_wc', 'src'), [dd.Input('image_wc', 'id')])

def make_image(b):
    img = BytesIO()
    plot_wordcloud(data=freqs).save(img, format='PNG')
    return 'data:image/png;base64,{}'.format(base64.b64encode(img.getvalue()).decode())

if __name__ == '__main__':
    app.run_server(debug=True)
