# trab-api

Este é um sistema distribuído em Python que consulta informações sobre filmes a partir de duas APIs públicas (OMDB e TMDB). O sistema recebe o título e ano de um filme, consulta as APIs para obter a sinopse e reviews, e retorna os resultados tanto no terminal quanto em um arquivo JSON.

## Funcionalidades

- Recebe o **título** e o **ano** do filme como entrada.
- Consulta a API do **OMDB** para obter a sinopse do filme.
- Consulta a API do **TMDB** para obter até 3 reviews sobre o filme.
- Exibe os dados no **terminal** e salva a resposta em um arquivo **`output.json`**.
- As chaves de API são carregadas a partir de um arquivo **`keys.json`**.

## Tecnologias Utilizadas

- **Python 3.x**
- **aiohttp**: Para fazer requisições HTTP assíncronas.
- **asyncio**: Para gerenciar tarefas assíncronas e concorrentes.
- **JSON**: Para manipulação de dados e armazenamento da saída em arquivo.

## Pré-requisitos

Certifique-se de ter as bibliotecas necessárias instaladas antes de rodar o projeto:

```bash
pip install aiohttp
```

## Como Usar

### Passo 1: Configurar o arquivo `keys.json`

Edite o arquivo chamado **`keys.json`** inserindo suas chaves nos campos correspondentes.

### Passo 2: Executar o script `trab-api.py`

```bash
python trab-api.py
```

### Passo 3: Inserir o nome do filme e o ano de lançamento

Após inserir os dados, as informações irão aparecer no terminal e no arquivo **`output.json`**

## Exemplo de Saída

```json
{
    "titulo": "shrek",
    "ano": "2001",
    "sinopse": "A mean lord exiles fairytale creatures to the swamp of a grumpy ogre, who must go on a quest and rescue a princess for the lord in order to get his land back.",
    "reviews": [
        "Shrek is a masterpiece! It helped subvert the Disney Renaissance formula with great humor and heart. Myers, Murphy, Diaz and Lithgow did a great job voicing the characters. Now that this film is 20 years old, I am glad it existed.",
        "Eddie Murphy was actually funny in this. I mean he was 1980s Eddie Murphy style funny in this. It was like he was at the top of his game again.\r\n\r\nIt makes you miss Eddie. What we have today is not the glory that he once was.\r\n\r\nBut, beyond the great return of funny Eddie...there is a wonderful dark humor that goes great with an otherwise wholesome and moving moral.",
        "It was so fun and a new try. \ud558\ud558"
    ]
}
```
