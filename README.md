# Pesquisador de Artigos em arquivos .bib

Este é um script em Python para pesquisar de forma rápida e eficiente artigos científicos dentro de arquivos de bibliografia `.bib`. A ferramenta permite filtrar os artigos por um intervalo de anos e procurar por palavras-chave específicas e suas frequências mínimas no título e no abstract, guardando os resultados num arquivo de texto. O Script é baseado no código dispónivel no repositório [github/arturjordao/paperSearch](https://github.com/arturjordao/PaperSearch?tab=MIT-1-ov-file#readme)

## Funcionalidades Principais

- **Filtragem por Ano**: Permite definir um intervalo de anos (início e fim) para limitar a busca apenas a publicações relevantes, otimizando a velocidade.
- **Busca por Palavras-Chave**: Procura por uma ou mais palavras-chave no título e no resumo de cada artigo.
- **Otimização para arquivos Ordenados**: Se o arquivo `.bib` estiver em ordem cronológica decrescente, o script para a busca automaticamente ao encontrar um artigo mais antigo que o limite inferior, poupando tempo de processamento.
- **Saída em arquivo de Texto**: Em vez de mostrar os resultados no terminal, o script gera um ficheiro `.txt` com os artigos encontrados, facilitando a consulta e o registo.

## Requisitos

Para executar o script, é necesário ter o Python instalado e a seguinte biblioteca:

- `bibtexparser`

para instalar a biblioteca necessária, use o seguinte comando:

```bash
pip install bibtexparser
```

## parâmetros:
`output_filename`: Nome do ficheiro onde os resultados serão guardados.

`input_filename`: Nome do teu ficheiro de bibliografia.

`ano_inicio` e `ano_fim`: O intervalo de anos para a busca.

`words`: A lista de palavras-chave que queres encontrar.

`th`: A frequência mínima que cada palavra-chave deve ter para ser considerada uma correspondência.

## Resultados 
esse script foi utilizado para pesquisar artigos no BibTex da Anthology (https://aclanthology.org) usando "llm" e "annotation" como palavras-chave e os resultados obtidos estão nesse repositório 
