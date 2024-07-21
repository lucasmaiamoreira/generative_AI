# Análise de Organizações na Seção "Mercado" (Q1 2015)

Este projeto realiza uma análise das organizações mencionadas nas notícias da seção "Mercado" do site Folha UOL News no primeiro trimestre de 2015. Utiliza técnicas de Reconhecimento de Entidades Nomeadas (NER) para extrair e contar as organizações mencionadas.

## Requisitos

- Python 3.10 ou superior
- Pip (gerenciador de pacotes do Python)

## Instalação

1. Clone este repositório:
   ```bash
   git clone git@github.com:lucasmaiamoreira/uol_market_analysis.git
   cd uol_market_analysis


2. Instalar Dependências

```
python -m venv venv
source venv/bin/activate  # Para Windows: venv\Scripts\activate
pip install -r requirements.txt
```

#### Executando a Aplicação

- Abra o arquivo analise_NER.ipynb em um ambiente de Jupyter Notebook.
- Execute as células do notebook.

#### Resultados
O script gera os seguintes arquivos de saída:

- organization_ranking_q1_2015.csv: Um arquivo CSV contendo as organizações mencionadas e sua frequência.
- report_q1_2015.txt: Um relatório detalhado em formato de texto.


#### Autor
Este projeto foi desenvolvido por Lucas Maia Moreira.

#### Contribuições
Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue ou enviar um pull request.

#### Licença
Este projeto está licenciado sob a Licença MIT.