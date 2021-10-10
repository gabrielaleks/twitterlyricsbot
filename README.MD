Bot pra twittar letras aleatórias de determinadas bandas
Usa a API do twitter e a API do Genius

Para descobrir o Id dos artistas, vá na documentação da API do Genius em Resources -> Search (ou clique [aqui](https://docs.genius.com/#search-h2)) e pesquise por uma letra específica da banda que você procura. A própria documentação tem uma feature que permite ver a resposta no canto direito, mas você também pode pesquisar pela URL. Coloque https://api.genius.com/search?q=:termo&access_token=:token&callback=json, substituindo com seus valores de pesquisa e seu token.