# Twitter Bot
Bot pra twittar letras aleatórias de determinadas bandas. Usa a API do twitter e a API do Genius.

O perfil é esse aqui: https://twitter.com/underground_ooc

Para descobrir o Id dos artistas, vá na documentação da API do Genius em Resources -> Search (ou clique [aqui](https://docs.genius.com/#search-h2)) e pesquise por uma letra específica da banda que você procura. A própria documentação tem uma feature que permite ver a resposta no canto direito, mas você também pode pesquisar pela URL. Coloque https://api.genius.com/search?q=:termo&access_token=:token&callback=json, substituindo com seus valores de pesquisa e seu token.

## Usando a API na URL:
### Dados de uma música específica
http://api.genius.com/songs/:songId?access_token=:accessToken

### Dados de um artista
http://api.genius.com/artists/:artistId?access_token=:accessToken

### Músicas de um artista específico
http://api.genius.com/artists/:artistId/songs?access_token=:accessToken