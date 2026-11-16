from pathlib import Path

import geopandas as gpd
import matplotlib as mpl
import pandas as pd

RAIZ = Path(__file__).resolve().parent
DADOS = RAIZ / "data"
FIGS = RAIZ / "figs"
SEED = 42

# Padrão visual
CINZA_CLARO = "#E3E3E3"
CINZA = "#8C8C8C"
GRAFITE = "#3A3A3A"
LARANJA = "#E8702A"

# Rampa sequencial de um só matiz.
RAMPA = ["#F9E5D7", "#F4C3A0", "#EE9B63", "#E8702A", "#A2430C"]

# Projeção de área igual (Albers cônica) ajustada à Bahia; metros.
CRS_AREA_IGUAL = "+proj=aea +lat_1=-9 +lat_2=-17 +lat_0=-13 +lon_0=-41.5 +ellps=GRS80 +units=m +no_defs"

FONTE_IBGE = ("Fonte: IBGE, Censo Demográfico 2022 (população) e PIB dos Municípios 2022 "
              "(SIDRA, tabelas 4714 e 5938); malha municipal 2025.")


def estilo():
    """Aplica o padrão visual (fonte, cores de texto, sem molduras)."""
    mpl.rcParams.update({
        "font.family": "sans-serif",
        "font.sans-serif": ["Calibri", "Carlito", "Segoe UI", "DejaVu Sans"],
        "text.color": GRAFITE,
        "axes.labelcolor": GRAFITE,
        "xtick.color": CINZA,
        "ytick.color": CINZA,
        "axes.edgecolor": CINZA,
        "axes.spines.top": False,
        "axes.spines.right": False,
        "figure.dpi": 100,
        "savefig.dpi": 200,
        "figure.facecolor": "white",
    })


def carregar_bahia(crs=CRS_AREA_IGUAL):
    """417 municípios da Bahia com população, área, densidade e PIB (2022).

    PIB per capita = PIB (mil R$ x 1000) / população do Censo 2022, em R$ por habitante.
    Tabela do PIB é cruzada com a malha pelo código IBGE;
    Table de população é cruzada com a malha pelo pelo nome.
    """
    g = gpd.read_file(DADOS / "ba_municipios.gpkg")
    g["CD_MUN"] = g["CD_MUN"].astype(str)

    pib = pd.read_csv(DADOS / "tabela5938.csv", sep=";", decimal=",",
                      encoding="utf-8-sig", dtype={"Cód.": str})
    pib = pib.iloc[:, [0, 2]]
    pib.columns = ["CD_MUN", "pib_mil"]
    pib["pib_mil"] = pd.to_numeric(pib["pib_mil"])

    pop = pd.read_excel(DADOS / "tabela_2_1_BA.xlsx", sheet_name="Tabela", header=None, skiprows=4)
    total_ba = float(pop.loc[pop[0] == "Bahia", 1].iloc[0])
    pop = pop[pop[0].astype(str).str.endswith("(BA)")].iloc[:, :4]
    pop.columns = ["Município", "pop", "area_km2", "dens"]
    for c in ("pop", "area_km2", "dens"):
        pop[c] = pd.to_numeric(pop[c])

    g["Município"] = g["NM_MUN"] + " (BA)"
    d = (g.merge(pib, on="CD_MUN", validate="one_to_one")
          .merge(pop, on="Município", validate="one_to_one")
          .sort_values("CD_MUN").reset_index(drop=True))
    assert len(d) == 417, "esperados 417 municípios"
    assert abs(d["pop"].sum() - total_ba) < 1, "soma da população difere do total da Bahia"
    d["pib_pc"] = d["pib_mil"] * 1000 / d["pop"]
    d = d.drop(columns=["Município"])
    return d.to_crs(crs)


def contorno_bahia(crs=CRS_AREA_IGUAL):
    """Polígono do estado (malha das UFs, 2025), na mesma projeção dos municípios."""
    uf = gpd.read_file(DADOS / "Estados_brasileiros.gpkg")
    return uf[uf["SIGLA_UF"] == "BA"].to_crs(crs)


def para_desenho(g, tolerancia_m=150):
    """Cópia com geometria simplificada (150 m) .
    """
    d = g.copy()
    d["geometry"] = g.geometry.simplify(tolerancia_m, preserve_topology=True)
    return d


def cabecalho(fig, titulo, subtitulo=None, linhas=1, x=0.01, y=0.995):
    """Título-manchete e subtítulo cinza com a medida mostrada.

    `linhas` = nº de linhas do título (use \\n para quebrar); o subtítulo desce o suficiente.
    """
    h = fig.get_figheight()
    fig.text(x, y, titulo, ha="left", va="top", fontsize=15, fontweight="bold", color=GRAFITE, linespacing=1.15)
    if subtitulo:
        fig.text(x, y - (0.27 * linhas + 0.06) / h, subtitulo, ha="left", va="top", fontsize=10.5, color=CINZA)


def topo(fig, linhas=1, com_subtitulo=True, extra=0.0):
    """Fração da altura da figura onde começa a área de desenho, abaixo do cabeçalho.

    `extra` (polegadas) abre espaço quando os painéis têm título próprio.
    """
    h = fig.get_figheight()
    return 1 - (0.27 * linhas + (0.42 if com_subtitulo else 0.12) + extra) / h


def br(x, casas=0):
    """Número no formato brasileiro: milhar com ponto, decimal com vírgula."""
    t = f"{x:,.{casas}f}"
    return t.replace(",", "§").replace(".", ",").replace("§", ".")


def fonte(fig, texto=FONTE_IBGE, x=0.01, y=0.005):
    """Fonte dos dados no rodapé de toda figura."""
    fig.text(x, y, texto, ha="left", va="bottom", fontsize=8, color=CINZA)


def salvar(fig, nome):
    """Exporta a figura para figs/nome, criando a pasta se necessário."""
    FIGS.mkdir(exist_ok=True)
    caminho = FIGS / nome
    fig.savefig(caminho, dpi=200, bbox_inches="tight", facecolor="white")
    print(f"figura salva: figs/{nome}")
    return caminho


def sem_eixos(ax):
    ax.set_axis_off()
    ax.set_aspect("equal")
