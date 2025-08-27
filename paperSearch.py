import bibtexparser
import re

def clean_text(text):
    text = re.sub(r'[\{\}"\',]', '', text)
    text = re.sub(r'\s+', ' ', text)
    return text.strip()



if __name__ == '__main__':
    output_filename = 'teste.txt'
    input_filename = 'anthology+abstracts'
    ano_inicio = 2025
    ano_fim = 2025
    words = ['llm']

    with open(f'{input_filename}.bib') as bibtex_file:
        bib_database = bibtexparser.load(bibtex_file)
    
    words = [x.lower() for x in words]

    th = 1
    
   
    with open(output_filename, 'w', encoding='utf-8') as output_file:
        output_file.write(f"Resultados da busca por artigos entre {ano_inicio} e {ano_fim}\n")
        output_file.write(f"Palavras-chave: {', '.join(words)}\n\n")

        for entry in bib_database.entries:
            ano_str = entry.get('year')
            if not ano_str:
                continue

            try:
                ano = int(ano_str)
            except ValueError:
                continue

            if ano < ano_inicio:
                output_file.write(f"\nBusca parada. Artigos restantes são mais antigos que {ano_inicio}.\n")
                break 
            
            if ano <= ano_fim:
                title = entry.get('title', '')
                abstract = entry.get('abstract', '')

                content_text = clean_text(title + ' ' + abstract)
                content_text_lower = content_text.lower()
                
                hit = 0
                for word in words:
                    if content_text_lower.count(word) >= th:
                        hit = hit + 1

                if hit >= len(words):
                    output_file.write(f"Artigo encontrado: {entry['ID']} (Ano: {ano})\n")
                    output_file.write(f"  Título: {title}\n\n")

    print(f"Busca concluída. Os resultados foram guardados no ficheiro '{output_filename}'.")