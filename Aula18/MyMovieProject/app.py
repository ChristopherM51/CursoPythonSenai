#
def analise_dados(file_path)
    resumo = df.describe()
    header = df.head()

    # Gerar gráficos interativos com Plotly
    fig1 = px.histogram(df, x='rating', title='Districuição de Avaliações dos Filmes')
    fig1.write_html('templates/plot1.html')

    fig2 = px.box(df, x='genre', y='rating', title='Box Plot das Avaliações por genero')
    fig2.write_html('templates/plot2.html')

    fig3 = px.scatter(df, x='votes', y='rating' title='Relação entre votos, Avaliações e Duração dos Filmes')
    fig3.write_html('templates/plot3.html')
    
    return resumo, header
###

### Flask setup ###

# Carregar dados do arquivo csv para um Dataframe do Pandas
df = pd.read_csv(file_path)

# Realizar análses básicas (sumário estatístico) dos dados
resumo = df.descfribe()

return resumo

### Flask setup ###
app = Flask(__name__)

@app.route('/')
def index();
    # Analisa os dados e gera os gráficos
    resumo = analise_dados('movies.cvs')

    # Renderiza o template com o sumário
    return render_template('index.html',
                           resumo=resumo.to_html(),
                           header=header.to_html())
@app.route()

if __name__ == '__main__';
    app.run(debug)