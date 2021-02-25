import dash
import dash.dependencies as dd
# import dash_core_components as dcc
import dash_html_components as html
from parser import freqs
from sandbox import mask
from io import BytesIO
from wordcloud import WordCloud, ImageColorGenerator
import base64


<<<<<<< HEAD:cloudmaker.py
"""

generate and display a wordcloud 

"""

=======
mask = np.array(Image.open("pics/roundel2.jpg"))
>>>>>>> main:main.py
image_colors = ImageColorGenerator(mask)

# external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__)


app.layout = html.Div([
    html.Img(id="image_wc"),
])

<<<<<<< HEAD:cloudmaker.py
# /usr/share/fonts/truetype/msttcorefonts/times.ttf
# /home/t/.local/share/fonts/FeFCrm27C.otf"
# /home/t/Téléchargements/oldnewspapertypes/OldNewspaperTypes.ttf

=======
#/usr/share/fonts/truetype/msttcorefonts/times.ttf
#/home/t/.local/share/fonts/FeFCrm27C.otf
#/home/t/Téléchargements/oldnewspapertypes/OldNewspaperTypes.ttf
>>>>>>> main:main.py

def plot_wordcloud(data):
    d = data
    wc = WordCloud(background_color='white',
                   font_path="/usr/share/fonts/truetype/msttcorefonts/times.ttf",
<<<<<<< HEAD:cloudmaker.py
                   max_words=2000,
                   mask=mask,
                   width=1024,
                   height=1024,
                   max_font_size=90,
                   min_font_size=5,
                   mode='RGBA'
=======
                   max_words = 1000,
                   mask=mask,
                   width=1024,
                   height=1024,
                   max_font_size=70,
                   min_font_size=1
>>>>>>> main:main.py
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
