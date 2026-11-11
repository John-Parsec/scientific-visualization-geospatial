# Dados

Os arquivos aqui são os usados pelos notebooks. Conferir o termo de uso de cada fonte no portal do IBGE antes da entrega.

| Arquivo | Fonte | Produto | Ano | Acesso | Status |
| --- | --- | --- | --- | --- | --- |
| `tabela5938.csv` | IBGE, SIDRA | Tabela 5938, PIB dos Municípios (referência 2010) | 2022 | 10/11/2026 | ok: 417 municípios, com código em `Cód.` |
| `ba_municipios.gpkg` | IBGE, Malha Municipal Digital (camada `ba_municipios_2025`; mantidos só `CD_MUN`, `NM_MUN` e a geometria) | Malha municipal da Bahia | 2025 | a preencher | ok: 417 municípios, SIRGAS 2000; códigos e nomes casam 417/417 com o PIB |
| `Estados_brasileiros.gpkg` | IBGE, Malha Municipal Digital (camada `br_uf_2025`, convertida de `BR_UF_2025/BR_UF_2025.shp`) | Unidades da Federação | 2025 | a preencher | ok: 27 UFs, SIRGAS 2000 (EPSG:4674); coordenadas e atributos idênticos ao shapefile |
| população por município | IBGE, SIDRA | Censo 2022, população residente | 2022 | a preencher | pendente |
| migração de e para a Bahia | IBGE, SIDRA | Censo 2022, migração de data fixa | 2017 a 2022 | 10/11/2026 | ok: 417 municipios |

## Notas

- `tabela5938.csv`: separador `;`, vírgula decimal, uma linha de cabeçalho e a coluna `Cód.` com o código IBGE de 7 dígitos (ler como texto). Os valores de PIB estão em mil reais.
- O PIB per capita não vem na tabela; é calculado nos notebooks como PIB ÷ população do Censo 2022.
- As colunas de valor adicionado por setor vêm como `...` (indisponíveis para 2022, conforme a nota do próprio IBGE na tabela) e não são usadas.
- O cruzamento da tabela com a malha é feito pelo código (`Cód.` = `CD_MUN`); os nomes também coincidem (`NM_MUN` + " (BA)").
- As duas malhas são da edição 2025 do IBGE: a área da Bahia em `Estados_brasileiros.gpkg` (564.764 km²) coincide com a soma das áreas dos municípios.
- Os mapas são reprojetados para uma projeção de área igual antes de desenhar. O "antes" do slide de projeção (Web Mercator) sai da reprojeção de `Estados_brasileiros.gpkg` para EPSG:3857 no próprio notebook.
- Uso da malha: o `LEIA-ME.txt` que acompanha `BR_UF_2025/` remete à Nota Metodológica "Informações técnicas e legais para a utilização dos dados publicados", da Malha Municipal, no portal do IBGE.
- `Bahia.gpkg` não é usado nos notebooks. O contorno do estado vem de `Estados_brasileiros.gpkg`.
