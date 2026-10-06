"""Ficha de historias de MCD desde cero (6-oct-2026): escribe reference/damodaran/MCD.json.

Valoración desde cero de McDonald's con los prompts vigentes (valoración v4, research v5). Las cifras de las historias
(crecimiento por fuente de ingresos, margen, probabilidades) son juicio del analista con la evidencia citada; los valores
por acción los calcula scripts/damodaran_stories.py con el motor que reproduce la hoja.
Uso: python scripts/mcd_cero_spec.py
"""
from __future__ import annotations

import json
from pathlib import Path

_ROOT = Path(__file__).resolve().parent.parent
OUT = _ROOT / "reference" / "damodaran" / "MCD.json"

TENQ = "[McDonald's, 10-Q del 2T26, 7-ago-2026](https://www.sec.gov/Archives/edgar/data/63908/000006390826000073/mcd-20260630.htm)"
TENK = "[McDonald's, 10-K 2025, 24-feb-2026](https://www.sec.gov/Archives/edgar/data/63908/000006390826000035/mcd-20251231.htm)"
Q2 = ("[McDonald's, comunicado del 2T26, 4-ago-2026]"
      "(https://www.sec.gov/Archives/edgar/data/63908/000006390826000067/exhibit991-6302026.htm)")
Q2S = ("[McDonald's, información complementaria del 2T26 (anexo 99.2), 4-ago-2026]"
       "(https://www.sec.gov/Archives/edgar/data/63908/000006390826000067/exhibit992-6302026.htm)")
INV = ("[McDonald's, 8-K del Investor Day (anexo 99.1), 23-sep-2026]"
       "(https://www.sec.gov/Archives/edgar/data/63908/000006390826000076/exhibit991-investorupdate2.htm)")
TRANS = ("[Stock Analysis, transcripción del Investor Day, 23-sep-2026]"
         "(https://stockanalysis.com/stocks/mcd/transcripts/746101-investor-day-2026/)")
MGMT = ("[McDonald's, 8-K del nombramiento de Skye Anderson, 4-ago-2026]"
        "(https://www.sec.gov/Archives/edgar/data/63908/000006390826000069/exhibitpressrelease.htm)")
DIVE = ("[Restaurant Dive, ventas comparables de 18 cadenas, 27-ago-2026]"
        "(https://www.restaurantdive.com/news/tracking-same-store-sales-18-major-restaurant-chains/742371/)")
RDIVE = ("[Restaurant Dive, tres cifras del plan NEXT, 28-sep-2026]"
         "(https://www.restaurantdive.com/news/mcdonalds-next-franchisee-rent-relief-store-productivity-investment/831377/)")
CB = ("[The Crypto Basic, caída de la acción y payback del plan NEXT, 24-sep-2026]"
      "(https://thecryptobasic.com/2026/09/24/mcdonalds-stock-fell-4-8-amid-investor-day-cfo-puts-next-company-payback-at-5-6-years/)")

SPEC = {
    "ticker": "MCD",
    "empresa": "McDonald's Corporation",
    "fecha": "2026-09-30",
    "industria_damodaran": "Restaurant/Dining",
    "historia": (
        "En cinco a diez años McDonald's es, todavía más que hoy, un dueño de inmuebles y de una marca que cobra renta y "
        "regalías sobre las ventas de ~50.000 restaurantes operados por terceros: el refranquiciamiento lleva la mezcla de "
        "~95% a ~98% de locales franquiciados a fines de 2028, así que los ingresos reportados bajan dos años aunque las ventas "
        "del sistema sigan creciendo ~5% (aperturas ~2,5% y comparables de 2-3%). El margen operativo sube de ~46% a ~52% por "
        "esa mezcla y por un gasto general que baja de 2,2% a 1,9% de las ventas del sistema, pero no llega al tope de la guía "
        "porque el apoyo de rentas a franquiciados (plan NEXT) se amortiza contra el resultado. Reinvierte mucho capital por "
        "dólar de ventas nuevas (terrenos y edificios), con un rendimiento parecido al actual (~21% con arrendamientos). El "
        "riesgo no es financiero ni de quiebra: es de tráfico en EE.UU., de la salud económica de los franquiciados y del costo "
        "de defender el valor percibido frente a Burger King, Taco Bell y Chick-fil-A."),
    "filtro": [
        ["Las ventas del sistema crecen ~5% anual (2,5% por aperturas y 2-3% de comparables) hasta 2030",
         "Sí",
         f"Sí: +4% a moneda constante en el 2T26 con aperturas que aportan ~2,5% ({Q2}; {Q2S}); la gerencia espera comparables de 3-4% normalizadas ({TRANS})",
         "Probable con comparables de 2-3%; el 3-4% exige recuperar el tráfico en EE.UU., que fue negativo en el 2T26 y en el 3T26"],
        ["El refranquiciamiento lleva la mezcla de ~95% a ~98% a fines de 2028",
         "Sí",
         f"Sí: meta declarada por el CFO en el Investor Day ({TRANS})",
         "Probable: la empresa ya opera así en EE.UU. (95%) e IDL (99%); depende de encontrar compradores en los mercados propios de IOM"],
        ["El margen operativo llega a 52% o más en 2030",
         "Sí",
         f"Sí: guía de «low-to-mid 50%» ajustado a 2030 ({INV}); el franquiciado rinde ~84% de margen y pasa a pesar ~77% de los ingresos",
         "Plausible: el apoyo de rentas (~US$5.000 M a 2030) se amortiza ~10 años contra el resultado y la reestructuración se repite desde 2023"],
        ["El plan NEXT recupera el tráfico de EE.UU. y gana 1,5 puntos de participación en pollo y bebidas",
         "Sí",
         f"Débil: comparables de EE.UU. +0,8% en el 2T26 con tráfico negativo y guía de 3T26 levemente negativa ({Q2}; {TRANS})",
         "Incierto: la industria espera tráfico plano en los mercados propios; la ganancia tiene que salir de participación"],
    ],
    "tasas_base_nota": (
        "Con ingresos LTM de US$27.702 millones (~US$19.500 millones de 2015) McDonald's está en el tramo de más de US$12.000 "
        "millones de The Base Rate Book, donde la mediana real de crecimiento a 5 años es baja (más ~2,5% de inflación para "
        "compararla con cifras nominales). La Base ({cagrA} nominal) queda por debajo de la mediana por una razón contable y no "
        "de demanda: el refranquiciamiento cambia ventas de restaurantes propios por rentas y regalías, que son ~15% de esas "
        "ventas. Las ventas del sistema crecen ~5%."),
    "segmentos": {"Franquicias": 17073, "Restaurantes propios": 9942, "Otros": 688},
    "crecimiento": {
        "texto": (
            "Los ingresos LTM (julio 2025-junio 2026) suman US$27.702 millones: ingresos de franquicias (rentas, regalías y "
            "cuotas iniciales) US$17.073 millones, ventas de restaurantes propios US$9.942 millones y otros ingresos (tecnología "
            f"cobrada a franquiciados y licencias de marca) US$688 millones (cálculo propio: 2025 + 1S26 − 1S25, {TENK} y {Q2}). "
            "La variable económica es la venta del sistema, US$139.400 millones en 2025 (+5% a moneda constante): McDonald's "
            f"cobra ~10,4% de renta y ~6% de regalías sobre la venta de los locales franquiciados ({TENK}). En el 2T26 las "
            "ventas del sistema crecieron 4% a moneda constante con comparables de +1,3% (EE.UU. +0,8%, IOM +1,5%, IDL +1,9%) y "
            f"aperturas que aportan ~2,5% ({Q2}; {Q2S}). En EE.UU. el comparable salió del ticket y la mezcla, con tráfico "
            "negativo, y la gerencia anticipó un 3T26 levemente negativo; la competencia directa se dividió: Burger King +8,5% y "
            f"Taco Bell +7% frente a Wendy's −7% ({DIVE}). El refranquiciamiento a ~98% a fines de 2028 ({TRANS}) explica la "
            "caída de los ingresos reportados en los años 1-2: los restaurantes propios bajan ~50% y las franquicias suben algo "
            "más que las ventas del sistema por las rentas y regalías de los locales vendidos."),
        "tabla": {
            "cols": ["US$ millones", "2024", "2025", "LTM jun-26 (cálculo propio)", "Variación 2T26", "Peso LTM"],
            "align": ["l", "r", "r", "r", "r", "r"],
            "rows": [
                ["Ingresos de franquicias", "15.715", "16.548", "17.073", "+4% (+3% m. c.)", "61,6%"],
                ["Ventas de restaurantes propios", "9.782", "9.690", "9.942", "+3%", "35,9%"],
                ["Otros ingresos", "423", "647", "688", "+6%", "2,5%"],
                ["Total", "25.920", "26.885", "27.702", "+4% (+2% m. c.)", "100%"],
                ["Ventas del sistema (no son ingresos)", "~131.000", "139.400", "—", "+5% (+4% m. c.)", "—"],
            ],
        },
    },
    "margenes": {
        "texto": (
            "El margen operativo GAAP LTM es 46,2% (EBIT de US$12.805 millones). Incluye US$219 millones de cargos de "
            "reestructuración del programa Accelerating the Organization que este análisis NO excluye: se repiten desde 2023 "
            f"(US$362, 291 y 229 millones en 2023-2025, {TENK}) y la empresa sigue reorganizando su estructura. Sin ellos el "
            f"margen no GAAP del 2T26 fue 46,9% ({Q2S}). La fuente del margen es la mezcla: los ingresos de franquicias "
            "dejan ~84% después de la ocupación (US$16.548 menos US$2.618 millones en 2025), los restaurantes propios ~15% "
            f"(US$9.690 menos US$8.268 millones) y el gasto general es ~2,2% de las ventas del sistema ({TENK}; {Q2S}). Con la "
            "mezcla de 98% y un gasto general de 1,9% a 2030, la empresa guía un margen ajustado de «low-to-mid 50%» "
            f"({INV}). El comparable maduro es el propio modelo de franquicia pura: Domino's opera con márgenes de ~19% porque "
            "su ingreso incluye la distribución de insumos, y Yum!, que es casi 100% franquiciada, con ~33%; ninguno es dueño de "
            "los inmuebles como McDonald's, cuya renta explica la diferencia. La Base usa 52%: el tramo bajo-medio de la guía, "
            f"porque el apoyo de rentas del plan NEXT se amortiza ~10 años contra el resultado ({TRANS})."),
    },
    "reinversion": {
        "texto": (
            "McDonald's es intensiva en capital por dólar de ingresos porque compra o arrienda a largo plazo el terreno y el "
            f"edificio de casi todos los locales: propiedad y equipo neto de US$28.479 millones y arrendamientos por US$14.729 "
            f"millones al 30-jun-2026 ({TENQ}). El capex fue US$3.365 millones en 2025 y la guía de 2026 es US$3.700-3.900 "
            f"millones, sobre todo para ~2.600 aperturas ({Q2S}); de 2027 a 2030 serán ~US$3.000 millones al año más "
            f"US$1.500-2.000 millones acumulados de apoyo de capital a franquiciados ({INV}). La gerencia estima un repago de "
            f"5-6 años para la empresa y retornos de nuevos locales «high-teens» a 20 años ({CB}). El capital invertido con "
            "arrendamientos capitalizados es ~US$50.400 millones y el ROIC después de impuestos ~21%. La hoja usa un "
            "ventas/capital de 0,5: con el margen objetivo de 55,5% (base ajustada) y un impuesto de 25%, cada dólar nuevo rinde "
            "~21%, igual al ROIC actual; un ventas/capital de 1,0 implicaría ~42%, el doble del actual, sin evidencia. En los "
            "años 1-2 el refranquiciamiento reduce los ingresos y la fórmula libera ~US$2.600 millones de capital: es del orden "
            "de lo que cobra la empresa por vender los restaurantes (equipos y derechos) y compensa el apoyo de capital del plan "
            "NEXT, que no se modela aparte. No hay compras relevantes."),
        "tabla": {
            "cols": ["Partida", "Valor", "Fuente", "Lectura"],
            "align": ["l", "r", "l", "l"],
            "rows": [
                ["Capex 2025 / guía 2026", "US$3.365 M / US$3.700-3.900 M", "10-K 2025; anexo 99.2 del 2T26", "~1,5 veces la D&A (US$2.199 M)"],
                ["Apoyo NEXT a franquiciados", "US$8.500 M a 2036 (US$5.000 M a 2030)", "8-K del 23-sep-2026", "Rentas (resta ingresos) + capital (capex)"],
                ["Capital invertido con arrendamientos", "~US$50.400 M", "Cálculo de la hoja ('Valuation output'!B41)", "ROIC después de impuestos ~21%"],
                ["Rendimiento del capital nuevo (Base)", "~21%", "55,5% × 75% × 0,5", "Igual al ROIC actual"],
            ],
        },
    },
    "riesgo": {
        "beta_propuesta": None,
        "texto": (
            "La beta desapalancada de Restaurant/Dining es 0,66 en la tabla global de Damodaran y 0,78 en la de EE.UU. "
            "(enero de 2026). La hoja usa la global, reapalancada con la deuda a valor de mercado de McDonald's (D/E ~25%): ~0,79, "
            "porque ~60% de las ventas está fuera de EE.UU. La prima de mercado es 3,70% (octubre de 2026) ponderada por las "
            "ventas de cada región (EE.UU. y Canadá ~46%, Europa ~43%, Australia ~5%, resto ~9%): 4,33%. El riesgo propio "
            "(tráfico, salud de los franquiciados, costo laboral) es diversificable y va en las historias Conservadora y "
            "Disrupción, no en la tasa. La calificación real (Baa1/BBB+) fija el costo de la deuda antes de impuestos en 7,13%."),
    },
    "historias": [
        {
            "id": "A", "tesis": "base", "prob": 0.50, "margen": 0.52,
            "nombre": "Base · Refranquiciamiento a 98% y comparables de 2-3%",
            "crec": {"Franquicias": [0.07, 0.065, 0.05, 0.05, 0.05],
                     "Restaurantes propios": [-0.15, -0.30, -0.10, 0.03, 0.03],
                     "Otros": [0.08, 0.07, 0.06, 0.05, 0.05]},
            "tesis_que": (
                "Las ventas del sistema crecen ~5% (aperturas ~2,5% y comparables de 2-3%: el valor y el pollo recuperan algo de "
                "tráfico, sin volver al 3-4% que pide la gerencia). El refranquiciamiento vende ~60% de los restaurantes propios "
                "hasta 2028: esas ventas bajan 15%, 30% y 10% y las franquicias suben 7%, 6,5% y 5%. El apoyo de rentas del plan "
                "NEXT resta ~1 punto al crecimiento de las franquicias. El margen pasa de ~46% a 52% en cinco años por mezcla y "
                "gasto general."),
            "tesis_contraste": "Comparables de EE.UU. ≥ 2% desde el 1T27, ventas del sistema ≥ +5% y margen ajustado ≥ 48% en 2027.",
        },
        {
            "id": "B", "tesis": "conservadora", "prob": 0.25, "margen": 0.48,
            "nombre": "Conservadora · El tráfico de EE.UU. no vuelve y el valor cuesta margen",
            "crec": {"Franquicias": [0.05, 0.05, 0.035, 0.035, 0.035],
                     "Restaurantes propios": [-0.15, -0.30, -0.10, 0.01, 0.01],
                     "Otros": [0.05, 0.04, 0.04, 0.03, 0.03]},
            "tesis_que": (
                "El consumidor de menores ingresos sigue débil y la competencia por precio (Burger King, Taco Bell, Wendy's con "
                "descuentos) obliga a sostener el menú de valor; las comparables quedan en 0-1% y las aperturas se moderan a ~2%. "
                "El refranquiciamiento ocurre igual, pero parte del apoyo a franquiciados termina siendo renta resignada y el "
                "margen se queda en 48%."),
            "tesis_contraste": "Comparables de EE.UU. ≤ 0% dos trimestres más, ventas del sistema < +3% y margen ajustado ≤ 46%.",
        },
        {
            "id": "C", "tesis": "disrupción", "prob": 0.10, "margen": 0.43,
            "nombre": "Disrupción · Deterioro de los fundamentales",
            "descripcion": "Los franquiciados pierden rentabilidad y la renta deja de crecer",
            "roic_terminal": "costo_capital", "terminal": "estabilizacion",
            "crec": {"Franquicias": [0.03, 0.02, 0.005, 0.0, 0.0],
                     "Restaurantes propios": [-0.17, -0.30, -0.12, -0.02, -0.02],
                     "Otros": [0.02, 0.0, 0.0, 0.0, 0.0]},
            "tesis_que": (
                "El tráfico cae varios años: los medicamentos para bajar de peso (GLP-1) reducen la frecuencia, el costo laboral "
                "sube por ley en más estados y las cadenas de pollo y los delivery ganan participación. La venta por local deja de "
                "crecer en términos nominales, el flujo de los franquiciados se comprime y McDonald's tiene que ampliar el apoyo "
                "de rentas y cerrar locales. El margen baja a 43%, la renta se estabiliza sin recuperación y el ROIC después del "
                "año 10 es el costo de capital."),
            "tesis_contraste": "Comparables globales negativas cuatro trimestres seguidos, cierres netos en EE.UU. o más apoyo de rentas que el anunciado.",
        },
        {
            "id": "D", "tesis": "optimista", "prob": 0.15, "margen": 0.545,
            "nombre": "Optimista · NEXT recupera el tráfico y la escala se nota en el margen",
            "crec": {"Franquicias": [0.08, 0.08, 0.065, 0.065, 0.06],
                     "Restaurantes propios": [-0.15, -0.30, -0.10, 0.04, 0.04],
                     "Otros": [0.10, 0.09, 0.08, 0.07, 0.06]},
            "tesis_que": (
                "El plan NEXT cumple: el pollo y las bebidas ganan 1,5 puntos de participación, la fidelización (~220 millones de "
                "usuarios activos) sube la frecuencia y las comparables vuelven a 3-4%; con aperturas de ~2,5% las ventas del "
                f"sistema crecen 6-7%. El margen llega a 54,5%, el tope de la guía ({INV})."),
            "tesis_contraste": "Comparables de EE.UU. ≥ 3% con tráfico positivo en 2027 y margen ajustado ≥ 50% en 2028.",
        },
    ],
    "prob_texto": (
        "La Base pesa 50%: extrapola el crecimiento de las ventas del sistema de los últimos años (~5% a moneda constante) con "
        "comparables algo menores que la guía de largo plazo y toma el refranquiciamiento y el margen de la guía con un margen "
        "de prudencia. La Conservadora pesa 25% porque es lo que hoy muestran EE.UU. (comparables de +0,8% en el 2T26, 3T26 "
        "levemente negativo) y la reacción del mercado al plan NEXT. La Disrupción pesa 10%: el negocio superó crisis peores "
        "(2002-2003, 2014-2015, la pandemia), pero el GLP-1 y el costo laboral son amenazas nuevas sobre la frecuencia y la "
        "economía del franquiciado. La Optimista pesa 15% porque exige que el tráfico vuelva y que el margen llegue al tope de "
        "la guía a la vez. Son juicio del analista, no frecuencias publicadas."),
    "premortem": [
        "El valor no recupera el tráfico: los franquiciados no adoptan los precios sugeridos (solo 60-65% lo hizo en el 2T26) y las comparables de EE.UU. siguen en ~0%.",
        "El apoyo de rentas se vuelve permanente: los US$8.500 millones del plan NEXT no alcanzan y la renta efectiva baja, como en la Conservadora.",
        "El refranquiciamiento se demora o se vende barato en IOM (Francia, Alemania) y la mejora de margen llega tarde.",
        "El GLP-1 y la regulación laboral (salario mínimo de comida rápida en California y otros estados) reducen la frecuencia y el flujo del franquiciado.",
        "Un dólar más fuerte recorta ~1-2 puntos el crecimiento reportado de un negocio con ~60% de ventas fuera de EE.UU.",
    ],
    "contra": (
        f"las comparables de EE.UU. fueron +0,8% en el 2T26 con tráfico negativo y la gerencia espera un 3T26 levemente negativo ({Q2}; {TRANS}); "
        "el CEO admitió problemas de ejecución del menú de valor; la industria espera tráfico plano en los mercados propios; y el mercado "
        f"castigó el plan NEXT (−4,8% el 23-sep-2026, su peor día desde marzo de 2020) porque el efectivo sale antes que el beneficio ({CB})."),
    "indicadores": [
        ["Comparables de EE.UU.", "+0,8% (2T26); 3T26 guiado levemente negativo", "≥ +2% desde el 1T27", "≤ 0% dos trimestres más"],
        ["Comparables globales", "+1,3% (2T26)", "≥ +3%", "≤ 0%"],
        ["Ventas del sistema a moneda constante", "+4% (2T26)", "≥ +5%", "≤ +3%"],
        ["Mezcla franquiciada", "~95% (inicio de 2026)", "~98% a fines de 2028", "Se demora o se vende con descuento"],
        ["Margen operativo ajustado", "46,9% (2T26)", "≥ 48% en 2027", "≤ 45%"],
        ["Gasto general / ventas del sistema", "~2,2% (guía 2026)", "≤ 2,0% en 2028", "≥ 2,3%"],
        ["Usuarios activos de fidelización (90 días)", "~220 millones (2T26)", "≥ +10% anual", "Estancamiento"],
        ["Acciones en circulación", "707,6 M (30-jun-2026); recompras US$1.251 M en el 1S26", "Bajan ~1% anual", "Suben"],
    ],
    "margenes_inverso": [0.48, 0.52, 0.545],
    "precio_lectura": (
        "El precio pide algo más que la Base: con su margen, el DCF inverso exige un crecimiento de los ingresos de los años "
        "1-5 cercano al {cagrA} de la Base o algo mayor. ¿Qué sabe el mercado que yo no? Puede estar pagando por la "
        "estabilidad del flujo (renta y regalías indexadas a ventas, con una beta baja) más de lo que la tasa del modelo "
        "reconoce, o por un ROIC terminal mayor que el promedio de la industria. En sentido contrario, el mercado acaba de "
        "castigar el plan NEXT: la caída de septiembre descuenta parte de la Conservadora."),
    "frase": "Arrendador y franquiciador de ~50.000 locales: refranquicia a 98%, las ventas del sistema crecen ~5% y el margen sube a ~52%",
    "confianza": "Media-alta: el modelo de renta y regalías es estable y está documentado; el tráfico de EE.UU. y el costo real del plan NEXT no",
    "cambiaria": "Las comparables y el tráfico de EE.UU., el ritmo del refranquiciamiento y la amortización del apoyo de rentas",
    "revision": "Resultados del 3T26 (fines de octubre o noviembre de 2026)",
    "fuentes": [
        ["McDonald's, 10-Q del 2T26 (7-ago-2026)", "https://www.sec.gov/Archives/edgar/data/63908/000006390826000073/mcd-20260630.htm"],
        ["McDonald's, 10-K 2025 (24-feb-2026)", "https://www.sec.gov/Archives/edgar/data/63908/000006390826000035/mcd-20251231.htm"],
        ["McDonald's, comunicado del 2T26 (4-ago-2026)", "https://www.sec.gov/Archives/edgar/data/63908/000006390826000067/exhibit991-6302026.htm"],
        ["McDonald's, información complementaria del 2T26 (4-ago-2026)", "https://www.sec.gov/Archives/edgar/data/63908/000006390826000067/exhibit992-6302026.htm"],
        ["McDonald's, 8-K del Investor Day (23-sep-2026)", "https://www.sec.gov/Archives/edgar/data/63908/000006390826000076/exhibit991-investorupdate2.htm"],
        ["McDonald's, 8-K del nombramiento de Skye Anderson (4-ago-2026)", "https://www.sec.gov/Archives/edgar/data/63908/000006390826000069/exhibitpressrelease.htm"],
        ["Stock Analysis, transcripción del Investor Day (23-sep-2026)", "https://stockanalysis.com/stocks/mcd/transcripts/746101-investor-day-2026/"],
        ["Restaurant Dive, ventas comparables de 18 cadenas (27-ago-2026)", "https://www.restaurantdive.com/news/tracking-same-store-sales-18-major-restaurant-chains/742371/"],
        ["Restaurant Dive, tres cifras del plan NEXT (28-sep-2026)", "https://www.restaurantdive.com/news/mcdonalds-next-franchisee-rent-relief-store-productivity-investment/831377/"],
        ["The Crypto Basic, caída de la acción y payback del plan NEXT (24-sep-2026)", "https://thecryptobasic.com/2026/09/24/mcdonalds-stock-fell-4-8-amid-investor-day-cfo-puts-next-company-payback-at-5-6-years/"],
        ["Damodaran, ERP implícita de octubre de 2026", "https://pages.stern.nyu.edu/~adamodar/pc/implprem/ERPOct26.xlsx"],
        ["Damodaran, betas por industria (enero de 2026)", "https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/Betas.html"],
        ["Mauboussin y Callahan, The Base Rate Book (2016)", "https://www.credit-suisse.com/media/assets/corporate/docs/about-us/research/publications/the-base-rate-book-integrating-the-past-to-better-anticipate-the-future.pdf"],
    ],
    "arrendamientos": {
        "vp": 10020.405, "ajuste_ebit": 962.973, "margen_pp": 962.973 / 27702, "capital_ventas": 10020.405 / 27702,
        "cierre": "2025-12-31",
        "criterio": "Damodaran: arrendamientos operativos como deuda; EBIT + gasto − depreciación del activo",
    },
    "justificacion": [
        ["Crecimiento: las ventas del sistema crecen; los ingresos reportados, no tanto.",
         "La Base crece {g1A} el primer año y {cagrA} compuesto en cinco años. Detrás hay ventas del sistema que crecen ~5% "
         "(aperturas ~2,5%, la guía de la empresa, y comparables de 2-3%) y un cambio de mezcla: el refranquiciamiento a ~98% "
         "vende ~60% de los restaurantes propios hasta 2028 y cambia una venta de ~US$4 millones por local por rentas y "
         "regalías de ~16% de esa venta. Por eso los ingresos bajan en los años 1-2 y vuelven a ~4,6% desde el año 4. La visión "
         "externa dice que ~{tbA} de las empresas de su tamaño lograron al menos ese crecimiento; el desvío no es de demanda "
         "sino contable. La alternativa de comparables de 3-4% (la guía de largo plazo) exige tráfico positivo en EE.UU., que "
         "no se ve en 2026. Sensibilidad: ±2 puntos de crecimiento en los años 1-5 llevan el DCF Base a {s_g_lo} y {s_g_hi}. "
         "Obligaría a revisarlo que las comparables de EE.UU. sigan en ~0% en 2027 (hacia la Conservadora, {cagrB}) o que "
         "vuelvan a 3-4% (hacia la Optimista, {cagrD})."],
        ["Margen: la mezcla lo sube; el apoyo a franquiciados lo frena.",
         "La Base parte de {margenY1} el primer año (el LTM en base ajustada por arrendamientos) y llega a {mA} en {conv} años "
         "({mrepA} en base reportada, +{arr_pp} pp por el ajuste de arrendamientos). Es el tramo bajo-medio de la guía de "
         "«low-to-mid 50%» a 2030: la mezcla de franquicias (~84% de margen después de la ocupación) y un gasto general de 1,9% "
         "de las ventas del sistema lo justifican, pero el apoyo de rentas del plan NEXT se amortiza ~10 años contra el "
         "resultado y los cargos de reestructuración se repiten. Sensibilidad: ±2 puntos de margen dan {s_m_lo} y {s_m_hi}. La "
         "Conservadora ({mB}) supone que el valor y el apoyo cuestan margen de forma permanente; la Disrupción ({mC}), "
         "franquiciados débiles; la Optimista ({mD}), el tope de la guía."],
        ["Reinversión: mucho capital por dólar de ventas, con el mismo retorno de hoy.",
         "El ventas/capital es {s2c1} en los años 1-5 (~US${cap1} de capital por dólar de ventas nuevas) y {s2c2} en los años "
         "6-10. Con el margen objetivo y un impuesto de 25%, el capital nuevo rinde ~21%, igual al ROIC actual con "
         "arrendamientos: los terrenos y edificios que McDonald's compra o arrienda son el núcleo de su modelo de renta. Un "
         "ventas/capital mayor supondría que la renta crece sin comprar inmuebles, algo que el historial no muestra. En los "
         "años 1-2 la caída de ingresos libera capital, del orden de lo que se cobra por los restaurantes vendidos. Con ±20% en "
         "el ventas/capital el DCF Base va de {s_s_lo} a {s_s_hi}."],
        ["Descuento y largo plazo: beta del sector y una ventaja durable.",
         "El costo de capital inicial es {wacc0} (tasa libre de riesgo {rf} al 30-sep-2026, prima de mercado {erp} de "
         "Damodaran de octubre ponderada por regiones, beta {beta}, costo de la deuda 7,13% antes de impuestos con la "
         "calificación Baa1/BBB+) y el terminal {waccT}. Después del año 10 el crecimiento es {tgA} y el ROIC terminal es el "
         "promedio de Restaurant/Dining ({roicT}): la marca tiene 70 años y superó varias crisis, la escala en compras, "
         "publicidad e inmuebles no tiene par y el ROIC no se erosiona. El terminal pesa {terminal} del valor operativo. ±1 "
         "punto de tasa da {s_k_lo} y {s_k_hi}; con un ROIC terminal igual al costo de capital el DCF Base sería {s_roic}."],
        ["Acciones, opciones y deuda.",
         "Se usan {acciones} millones de acciones (707,6 millones en circulación al 30-jun-2026, portada del 10-Q, más 1,2 "
         "millones de RSU); las 8,8 millones de opciones a US$228,19 se restan por su valor. La deuda es la financiera de "
         f"US$39.863 millones (incluye papel comercial y vencimientos corrientes) más arrendamientos financieros de US$2.329 "
         "millones y operativos capitalizados de ~US$10.020 millones. El patrimonio contable negativo (−US$1.023 millones) "
         "refleja US$80.527 millones de recompras acumuladas, no insolvencia. Una dilución adicional de 5% llevaría el DCF Base "
         "a {s_acc}."],
        ["Probabilidades y lectura del resultado.",
         "Con {pA} para la Base, {pB} para la Conservadora, {pC} para la Disrupción y {pD} para la Optimista, el DCF esperado es "
         "{ve} frente a un DCF Base de {vA}. El esperado queda por debajo de la Base porque las historias desfavorables pesan "
         "35% y en ellas el margen cae más de lo que sube en la Optimista. Con el margen de seguridad de {mos}, el precio de "
         "compra con margen es {vmos}."],
    ],
}


def main() -> int:
    OUT.write_text(json.dumps(SPEC, ensure_ascii=False, indent=1))
    print("escrito", OUT)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
