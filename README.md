# Visualização Científica · Atividade final · Dupla A · Geoespacial

DEC1217 · PPGMC/UESC · Cap. 7 de Schwabish, *Better Data Visualizations* (2021)

**Integrantes:**

- Brenda Castro da Silva
- João Manoel Almeida Oliveira

## Tema-fio

A Bahia em 417 municípios (população e renda), com a migração de e para a Bahia. Uma só base atravessa as quatro técnicas.

## Notebooks

| Notebook | Técnica | Dado |
| --- | --- | --- |
| `topico_004_01.ipynb` | Mapa coroplético | PIB per capita municipal, 2022 |
| `topico_004_02.ipynb` | Cartograma | População (Censo 2022) como tamanho, PIB per capita como cor |
| `topico_004_03.ipynb` | Símbolos proporcionais e densidade de pontos | PIB total e população |
| `topico_004_04.ipynb` | Mapa de fluxo | Migração de data fixa de e para a Bahia, Censo 2022 |

As figuras dos slides são exportadas pelos notebooks para `figs/` (os notebooks 01 e 03 usam o prefixo `fig_004_0X_`). Os slides estão em `slides.pptx`.

## Estrutura

```text
topico_004_01.ipynb ... topico_004_04.ipynb   um notebook por técnica
utils.py                                      funções e estilo compartilhados (usado pelos notebooks 01 e 03)
data/                                         dados de entrada e data/README.md
figs/                                         figuras exportadas pelos notebooks
slides.pptx                                   slides da apresentação
slides.pdf                                    slides da apresentação
requirements.txt                              dependências
```

## Como rodar

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
jupyter lab
```

Em cada notebook, *Restart & Run All*, com `utils.py` na mesma pasta dos notebooks. Os notebooks leem apenas de `data/` e usam semente aleatória fixa (42). O notebook 04 só usa o pacote `geobr`, que baixa as UFs da internet, se `data/BR_UF_2022.shp` não existir.

## Dados

Os arquivos de dados usados pelos notebooks, com fonte, licença e data de acesso de cada um, estão em [`data/README.md`](data/README.md).

## Autoria e uso de IA

Código, dados e figuras de terceiros são citados nos notebooks e em `data/README.md`. IA generativa (Claude, da Anthropic) foi usada como apoio no planejamento, na escrita do código e criação dos slides.
