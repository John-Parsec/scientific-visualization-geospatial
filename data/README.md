# Dados

Esta pasta reúne os arquivos de dados lidos pelos notebooks `topico_004_01` a `topico_004_04`. Todos são produtos públicos do IBGE,.

## Arquivos usados

| Arquivo | Conteúdo | Fonte | Usado em |
| --- | --- | --- | --- |
| `tabela5938.csv` | PIB dos Municípios (PIB a preços correntes, em mil reais, e participações), 2022. 417 municípios da Bahia | IBGE, SIDRA, tabela 5938 (referência 2010) | 01, 02, 03 |
| `tabela_2_1_BA.xlsx` | População residente, área e densidade demográfica por município, Censo 2022 | IBGE, SIDRA, tabela 4714 | 01, 02, 03 |
| `ba_municipios.gpkg` | Malha municipal da Bahia, 2025 (camada `ba_municipios_2025`; mantidos só `CD_MUN`, `NM_MUN` e a geometria) | IBGE, Malha Municipal Digital | 01, 03 |
| `Estados_brasileiros.gpkg` | Unidades da Federação, 2025 (camada `br_uf_2025`, convertida de `BR_UF_2025.shp`). Serve de contorno da Bahia | IBGE, Malha Municipal Digital | 01, 03 |
| `BA_Municipios_2022.shp` (com `.shx`, `.dbf`, `.prj`, `.cpg`) | Malha municipal da Bahia, 2022 (417 municípios) | IBGE, Malha Municipal Digital 2022 | 02 |
| `BR_UF_2022.shp` (com `.shx`, `.dbf`, `.prj`, `.cpg`) | Unidades da Federação, 2022 (27 UFs) | IBGE, Malha Municipal Digital 2022 | 04 |
| `tabela10159.xlsx` | Matriz UF × UF: pessoas de 5 anos ou mais que não residiam na UF 5 anos antes, por UF de residência 5 anos antes, Censo 2022 (resultados preliminares) | IBGE, SIDRA, tabela 10159 | 04 |

Os arquivos de uma mesma linha com várias extensões (shapefile) precisam ficar juntos na pasta. Os notebooks 01 e 03 leem os arquivos pelo módulo `utils.py` (`carregar_bahia` e `contorno_bahia`).

Se `BR_UF_2022.shp` não estiver na pasta, o notebook 04 tenta baixar as UFs pelo pacote `geobr`; sem ele, mostra só os pontos das UFs.

## Fonte, data de acesso e licença

| Arquivo | Acesso |
| --- | --- |
| `tabela5938.csv` | 10/11/2026 |
| `tabela_2_1_BA.xlsx` | a preencher |
| `ba_municipios.gpkg` | a preencher |
| `Estados_brasileiros.gpkg` | a preencher |
| `BA_Municipios_2022.*` | a preencher |
| `BR_UF_2022.*` | a preencher |
| `tabela10159.xlsx` | a preencher |

**Licença.** São dados públicos do IBGE, publicados como dados abertos (Política de Dados Abertos do Poder Executivo federal, Decreto nº 8.777/2016). Nas páginas do IBGE e no *Leia-me* da malha municipal que consultamos não encontramos uma licença nomeada. A condição que seguimos é citar o IBGE como fonte: todas as figuras trazem a linha "Fonte: IBGE ...". Antes de redistribuir os arquivos fora deste trabalho, convém conferir os termos no site do IBGE.

**Malha municipal.** O próprio IBGE avisa que a Malha Municipal Digital não é a malha oficial da divisão político-administrativa, que os limites são aproximados e que a linha de costa não serve para fins econômicos ou ambientais (*Leia-me* da malha 2022). Aqui ela serve só para desenhar os mapas.

**Onde baixar.**

- Tabelas: SIDRA, https://sidra.ibge.gov.br (tabelas 5938, 4714 e 10159).
- Malhas: IBGE, Geociências, Organização do território, Malhas territoriais, Malhas municipais (anos 2022 e 2025).

## Verificações

- `tabela5938.csv`: 417 municípios, com o código IBGE na coluna `Cód.`.
- `tabela_2_1_BA.xlsx`: 417 municípios; a soma da população é igual ao total da Bahia (14.141.626).
- `ba_municipios.gpkg` e `BA_Municipios_2022.shp`: 417 municípios cada, em SIRGAS 2000 (EPSG:4674). Os códigos e nomes de `ba_municipios.gpkg` casam 417 de 417 com o PIB e com a população; o notebook 02 casa a malha 2022 pelo nome normalizado.
- `Estados_brasileiros.gpkg`: 27 UFs; coordenadas e atributos idênticos ao shapefile de origem.
- `BR_UF_2022.shp`: 27 UFs, SIRGAS 2000 (EPSG:4674).
- `tabela10159.xlsx`: só há matriz UF × UF; não existe detalhe por município.

## Arquivos gerados pelos notebooks

Ao rodar, o notebook 02 grava `dados_cartograma_bahia.csv` e o notebook 04 grava `fluxos_entrada_bahia.csv` e `fluxos_saida_bahia.csv`, na pasta de onde o notebook é executado. São resultados derivados dos dados acima, não dados de entrada.
