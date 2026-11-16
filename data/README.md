# Dados

Os arquivos aqui são os usados pelos notebooks. Conferir o termo de uso de cada fonte no portal do IBGE antes da entrega.

| Arquivo | Fonte | Produto | Ano | Acesso | Usado em | Status |
| --- | --- | --- | --- | --- | --- | --- |
| `tabela5938.csv` | IBGE, SIDRA | Tabela 5938, PIB dos Municípios (referência 2010) | 2022 | 10/11/2026 | 01, 02, 03 | ok: 417 municípios, com código em `Cód.` |
| `tabela_2_1_BA.xlsx` | IBGE, SIDRA | Tabela 4714, Censo 2022: população residente, área e densidade, por município | 2022 | a preencher | 01, 02, 03 | ok: 417 municípios; soma da população = total da Bahia (14.141.626) |
| `ba_municipios.gpkg` | IBGE, Malha Municipal Digital (camada `ba_municipios_2025`; mantidos só `CD_MUN`, `NM_MUN` e a geometria) | Malha municipal da Bahia | 2025 | a preencher | 01, 02, 03 | ok: 417 municípios, SIRGAS 2000; códigos e nomes casam 417/417 com o PIB e com a população |
| `Estados_brasileiros.gpkg` | IBGE, Malha Municipal Digital (camada `br_uf_2025`, convertida de `BR_UF_2025/BR_UF_2025.shp`) | Unidades da Federação | 2025 | a preencher | 01, 03 (contorno), 04 | ok: 27 UFs, SIRGAS 2000 (EPSG:4674); coordenadas e atributos idênticos ao shapefile |
| `tabela10159 (1).xlsx` | IBGE, SIDRA | Tabela 10159, Censo 2022: UF de residência 5 anos antes × UF de residência atual (resultados preliminares) | 2017 a 2022 | a preencher | 04 | matriz UF × UF; não há detalhe por município |

## Notas

- `tabela5938.csv`: separador `;`, vírgula decimal, uma linha de cabeçalho e a coluna `Cód.` com o código IBGE de 7 dígitos (ler como texto). Os valores de PIB estão em mil reais.
- `tabela_2_1_BA.xlsx`: planilha `Tabela`, cabeçalho nas 4 primeiras linhas (`skiprows=4`); as linhas de município terminam em "(BA)". O cruzamento com a malha é pelo nome, `NM_MUN` + " (BA)", e os 417 nomes casam.
- O PIB per capita não vem pronto; é calculado nos notebooks como PIB 2022 (mil R$ × 1.000) ÷ população do Censo 2022, em R$ por habitante.
- As colunas de valor adicionado por setor da tabela 5938 vêm como `...` (indisponíveis para 2022, conforme a nota do IBGE na própria tabela) e não são usadas.
- O cruzamento do PIB com a malha é feito pelo código (`Cód.` = `CD_MUN`).
- As duas malhas são da edição 2025 do IBGE: a área da Bahia em `Estados_brasileiros.gpkg` (564.764 km²) coincide com a soma das áreas dos municípios.
- Os mapas são reprojetados para uma projeção de área igual (Albers cônica ajustada à Bahia, definida em `vis_geo.py`) antes de desenhar. O "antes" do slide de projeção (Web Mercator) sai da reprojeção do contorno para EPSG:3857 no próprio notebook 01.
- Para desenhar mais rápido, os polígonos são simplificados em 150 m **só na hora de plotar**; áreas e sorteio de pontos usam a geometria original.
- Uso da malha: o `LEIA-ME.txt` que acompanha `BR_UF_2025/` remete à Nota Metodológica "Informações técnicas e legais para a utilização dos dados publicados", da Malha Municipal, no portal do IBGE.

## Arquivos na pasta que os notebooks não usam

- `tabela10157.csv`: tabela 10157 (estrangeiros por país de nascimento). Não é migração interna e não entra em nenhum notebook.
- `BA_Municipios_2022.shp`: shapefile sem os arquivos auxiliares (`.dbf`, `.shx`, `.prj`); não abre e é redundante com `ba_municipios.gpkg`.
- `area_de_estudo.gpkg` (83 municípios do projeto de georreferenciamento) e `Bahia.gpkg` (contorno antigo em Mercator): não usados.
- `29_BA/` (Censo bruto 2022): fora do repositório, listado no `.gitignore`.
