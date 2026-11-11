# Visualização Científica · Atividade final · Dupla A · Geoespacial

DEC1217 · PPGMC/UESC · Cap. 7 de Schwabish, *Better Data Visualizations* (2021) · Apresentação em 18/11/2026

**Integrantes:** [preencher]

## Tema-fio

A Bahia em 417 municípios (população e renda), com a migração de e para a Bahia. Uma só base atravessa as quatro técnicas.

## Notebooks

| Notebook | Técnica | Dado |
| --- | --- | --- |
| `topico_004_01.ipynb` | Mapa coroplético | PIB per capita municipal, 2022 |
| `topico_004_02.ipynb` | Cartograma | População (Censo 2022) como tamanho, PIB per capita como cor |
| `topico_004_03.ipynb` | Símbolos proporcionais e densidade de pontos | PIB total e população |
| `topico_004_04.ipynb` | Mapa de fluxo | Migração de data fixa de e para a Bahia, Censo 2022 |

Todas as figuras dos slides são exportadas para `figs/` com o mesmo nome usado em `slides.pdf`.

## Como rodar

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
jupyter lab
```

Em cada notebook, *Restart & Run All*. Os notebooks leem apenas de `data/` e usam semente aleatória fixa (42), então rodam do zero e sem rede.

## Dados

Fontes, licença e data de acesso de cada arquivo estão em [`data/README.md`](data/README.md).

## Autoria e uso de IA

Código, dados e figuras de terceiros são citados nos notebooks e em `data/README.md`. IA generativa (Claude, da Anthropic) foi usada como apoio no planejamento, na escrita do código e na revisão. Os integrantes revisaram o resultado e respondem pelas escolhas de design e pelo código na arguição.
