"""Contenido de las hojas de texto de la valoración de DUOL desde cero (7-oct-2026; pasos 3 y 10 del prompt v4).
Las cifras de resultado son fórmulas vivas contra el modelo y la pestaña «Escenarios e historias»; las demás salen de
las fuentes citadas (corte de información: 30-sep-2026; hechos posteriores al balance del 30-jun-2026 incluidos)."""
from __future__ import annotations

import model_steps as ms

SOURCES = (
    "Fuentes: 10-Q del 2T26 de Duolingo (6-ago-2026) y 10-K 2025 (27-feb-2026), SEC EDGAR; cartas a los accionistas del "
    "4T25 (26-feb-2026), 1T26 (4-may-2026) y 2T26 (5-ago-2026); 8-K del cambio de CFO (12-ene-2026), del programa de "
    "recompra (26-feb-2026), de la nueva consejera (10-ago-2026) y de los usuarios de agosto (18-ago-2026); transcripción "
    "de la llamada del 2T26 (The Motley Fool); Reuters/Yahoo Finance (26-feb-2026); TIKR sobre Evercore ISI (29-sep-2026); "
    "Damodaran (betas, márgenes, ROIC y ventas/capital por industria, ene-2026; ERP oct-2026); UST 10 años y cierre del "
    "30-sep-2026."
)

CUALITATIVO = {
    "B5": "Duolingo, Inc.",
    "B6": ("Luis von Ahn (cofundador y CEO desde 2011); Severin Hacker (cofundador y CTO). CFO: Gillian Munson (desde el "
           "23-feb-2026). Acciones Clase B con 20 votos: directivos y accionistas de 5% tienen 76,3% de los votos."),
    "B7": "Aplicación de aprendizaje (idiomas, matemáticas, música, ajedrez) por suscripción (Damodaran: Software (Internet))",
    "B8": "https://www.duolingo.com  |  IR: https://investors.duolingo.com",
    "B11": "Descripción",
    "A12": "Visión General de la Empresa",
    "B12": ("La aplicación educativa más descargada y de mayor facturación del mundo: 58,7M de usuarios activos diarios y "
            "140,6M mensuales en el 2T26, 12,7M de suscriptores pagos. Ventas LTM a jun-2026 de US$1.145M, margen operativo "
            "GAAP de 13,7% y flujo libre de ~US$400M; sin deuda y con US$1.417M de caja e inversiones."),
    "A13": "Suscripciones",
    "B13": ("US$980,7M LTM (86%): Super Duolingo, Max (IA: Video Call, explicaciones) y planes familiares, cobrados sobre todo "
            "por las tiendas de Apple (59,6% de los ingresos) y Google (23,2%). +22% en el 2T26; reservas de suscripción +10%."),
    "A14": "Publicidad",
    "B14": ("US$82,9M LTM (7%): avisos a los usuarios gratuitos. +2% en el 2T26: la empresa redujo la carga de avisos en 2026 "
            "para crecer en usuarios y prepara un formato de aviso propio."),
    "A15": "Duolingo English Test",
    "B15": "US$41,4M LTM (4%): examen de inglés en línea para admisiones universitarias. Plano desde 2023 (~US$42M al año).",
    "A16": "Compras en la app y otros",
    "B16": ("US$40,0M LTM (3%): gemas, vidas y personalizaciones. −23% en el 2T26 por la reducción de fricción; la gerencia "
            "quiere vender personalizaciones del avatar que no frenen el uso."),
    "B21": "Argumento",
    "A22": "Audiencia que se acelera",
    "B22": ("Usuarios activos diarios +23% en el 2T26 (+21% en el 1T26) y +27,4% el 17-ago-2026 (8-K del 18-ago); retención de "
            "usuarios actuales en máximo histórico (84%); meta de 100M de usuarios diarios en 2028."),
    "A23": "IA más barata",
    "B23": ("Video Call pasó de US$0,30 a menos de US$0,01 por llamada con modelos abiertos; margen bruto 72,6% en el 2T26 "
            "pese a dar más IA a más usuarios. Guía de EBITDA ajustado 2026 subida a 26,5%."),
    "A24": "Caja y recompras",
    "B24": ("Flujo libre de US$360M en 2025 (34,7% de las ventas) y más de US$375M guiado en 2026; programa de recompra de "
            "US$400M (feb-2026), US$71,9M ejecutados al 1-ago-2026."),
    "B27": "Riesgo",
    "A28": "Monetización",
    "B28": ("En 2026 se resignaron más de US$50M de reservas (~5 pp de crecimiento) para crecer en usuarios: reservas +8% en el "
            "2T26 frente a usuarios +23%. Si la audiencia nueva no paga, el ingreso por usuario sigue cayendo."),
    "A29": "IA generalista",
    "B29": ("Asistentes de voz gratuitos (OpenAI, Google, Apple) pueden practicar conversación en cualquier idioma; la acción "
            "cayó ~51% en doce meses al 14-sep-2026 por este temor y por la desaceleración de las reservas."),
    "A30": "Compensación en acciones y tiendas",
    "B30": ("Compensación en acciones de ~15% de las ventas en 2026 y dilución bruta de 3,5-4% al año; 83% de los ingresos se "
            "cobra por Apple y Google, que fijan comisiones y reglas."),
    "A32": SOURCES,
    "A35": "Periodo del Reporte: 1 de julio de 2026 – 30 de septiembre de 2026",
    "B38": "Titular",
    "A39": "Resultados",
    "B39": "2T26: ingresos +18% a US$298,5M; reservas +8% a US$289,1M",
    "D39": "Usuarios activos diarios 58,7M (+23%), suscriptores 12,7M (+17%), EBITDA ajustado 25,9%, flujo libre US$78,6M (carta del 5-ago-2026).",
    "A40": "Guía",
    "B40": "2026: reservas US$1.285M (+10,9%), ingresos US$1.207M (+16,3%), EBITDA ajustado ~26,5%",
    "D40": "3T26: reservas US$307M (+8,9%) e ingresos US$302M (+11,1%); compensación en acciones ~15% de las ventas; impuesto 23-25%.",
    "A41": "Usuarios de agosto",
    "B41": "Una pantalla mostró por error +27,4% de usuarios diarios el 17-ago-2026",
    "D41": "8-K (Reg FD) del 18-ago-2026: dato preliminar sin validar; la empresa no cambió la guía.",
    "A42": "Gobierno",
    "B42": "Sallie Krawcheck se suma al directorio y al comité de auditoría",
    "D42": "8-K del 10-ago-2026; el directorio pasa de nueve a diez miembros. Gillian Munson es CFO desde el 23-feb-2026 (8-K del 12-ene-2026).",
    "A43": "Mercado",
    "B43": "Evercore ISI sube a Outperform (precio objetivo US$210) el 29-sep-2026",
    "D43": "Encuesta propia (53% de quienes aprenden idiomas usan Duolingo) y 20 veces el EBITDA de 2028; la acción subió ~6% (TIKR, 29-sep-2026).",
    "B46": "Análisis e impacto en la valoración",
    "A47": "Año de inversión",
    "B47": ("El año 1 (jul-2026 a jun-2027) crece 11% (las reservas, no el ingreso reportado) y su margen baja a 18,5% en la base "
            "del modelo (~9,5% GAAP) por la compensación en acciones y la IA que se regala."),
    "A48": "I+D y arrendamientos",
    "B48": ("I+D capitalizado a 3 años, alineado a 12 meses a junio (margen base 24,0% frente a 13,7% GAAP); arrendamientos operativos con el conversor (VP "
            "US$105M; +0,04 pp de margen)."),
    "A49": "Historias",
    "B49": ("Cuatro historias activas: Base (45%), Conservadora (25%), Disrupción (10%) y Optimista (20%); 'Valuation output' "
            "calcula las cuatro con la estructura de Damodaran."),
    "A50": "Riesgo en el descuento",
    "B50": ("Beta 1,35 bottom-up: Software (Internet) global 1,34 reapalancada con la D/E de mercado (solo arrendamientos). "
            "Prima 3,70% (oct-2026) ponderada por regiones: 4,82%. Ke 11,81%; WACC 11,70%; terminal 8,99%."),
}

ESTADISTICAS = {
    "B4": "='Trailing Valuation'!L5", "B5": "='Trailing Valuation'!L6", "B6": "='Input sheet'!B22",
    "B7": "='Income Statement'!L3", "B8": "—",
    "B12": "='Income Statement'!L30", "B13": "='Input sheet'!B13/'Input sheet'!B12",
    "B14": "='Income Statement'!L19/'Income Statement'!L3", "B15": "='Income Statement'!L22/'Income Statement'!L3",
    "B16": "='Márgenes'!L9",
    "B21": "='Valuation output'!B42", "B23": "='Eficiencia de capital'!L3",
    "E4": "='Trailing Valuation'!L13", "E5": "='Trailing Valuation'!L18", "E6": "='Trailing Valuation'!L19",
    "E7": "='Trailing Valuation'!L21", "E8": "='Trailing Valuation'!L16", "E9": "='Trailing Valuation'!L20",
    "E12": "='Resumen de Valoración'!D12", "E13": "—", "E14": "—", "E15": "—", "E16": "—", "E17": "—",
    "E20": "='Balance Sheet'!L5", "E23": "—",
    "H4": "=('Income Statement'!K3/'Income Statement'!H3)^(1/3)-1",
    "H5": "=('Income Statement'!K3/'Income Statement'!F3)^(1/5)-1",
    "H6": "—",
    "H7": "—", "H8": "—", "H9": "—", "H10": "—",
    "H11": "—",
    "H12": "—", "H13": "—", "H14": "—", "H15": "—",
    "H18": 0, "H19": 0, "H20": 0, "H21": "—", "H22": "—", "H23": "—", "H24": "—",
}

STORIES = {
    "A3": "Duolingo: la audiencia que creció en 2026 vuelve a pagar desde 2027",
    "A4": ("Duolingo cobra suscripciones a una fracción (~9%) de una audiencia de 140M de usuarios mensuales: US$1.145M de "
           "ventas LTM, 86% de suscripciones, margen GAAP de 13,7%. La historia Base: el año 1 crece 11% (las reservas de 2026, "
           "no el ingreso reportado), los años 2-5 entre 12% y 10% cuando la audiencia más grande se monetiza otra vez, y el "
           "margen GAAP pasa de ~10% en 2026 a ~24% (28% con el I+D como inversión) cuando la compensación en acciones baja de "
           "~15% a ~10% de las ventas. La marca y el hábito de las rachas no son una ventaja estructural en el criterio de "
           "Damodaran (costos de cambio bajos, sin efectos de red): el ROIC después del año 10 es el costo de capital."),
    "G10": "Año 1 11,1% (suscripciones +13%, publicidad +4%, English Test 0%, compras en la app −10%); CAGR 1-5 11,0%.",
    "G11": "Año 1 18,5% en la base del modelo (~9,5% GAAP: guía de EBITDA ajustado 26,5% − compensación en acciones ~15%); objetivo 28,0% en 5 años.",
    "G12": "Tasa efectiva 24% (guía 23-25%) que converge a la marginal de 25%; pérdidas fiscales federales de US$111M.",
    "G13": "2,25 en los años 1-5 y 2,0 en los años 6-10 (con arrendamientos): el capital nuevo rinde ~47% y ~42% (ROIC actual 43%).",
    "G14": "ROIC actual 43% (I+D capitalizado, sin los impuestos diferidos de la liberación de la reserva); terminal = costo de capital (sin ventaja defendible).",
    "G15": "Ke 11,81% (rf 5,29% + beta 1,35 × ERP por regiones 4,82%); Kd 5,69% (sintético AAA); WACC 11,70%; terminal 8,99%.",
}

SUPUESTOS_RECOMENDADOS = {
    "C6": 0.1107, "D6": "Suma por fuente: suscripciones +13%, publicidad +4%, English Test 0%, compras en la app y otros −10%.",
    "C7": 0.1854, "D7": "~9,5% GAAP en el año 1 (guía 2026) + ~9 pp de I+D capitalizado (base del modelo) + 0,04 pp de arrendamientos.",
    "C8": 0.1100, "D8": "Años 2-5 de la Base: 12,3%, 11,5%, 10,5% y 9,6%.",
    "C9": 0.2804, "D9": "28% en la base del modelo (~24% GAAP, extremo bajo de Match Group) + 0,04 pp de arrendamientos.",
    "C10": 5, "D10": "2026 es un año de inversión deliberada; el margen vuelve en 2027-2030.",
    "C11": 2.25, "D11": "Cerca del ventas/capital de hoy (2,38) con el capital arrendado; el capital nuevo rinde ~47%.",
    "C12": 2.0, "D12": "Los prepagos dejan de crecer más que las ventas; el capital nuevo rinde ~42%.",
}

MULTIPLOS_EVALUACION = (
    "Evaluación DUOL (7-oct-2026, desde cero): los múltiplos Base salen de tres anclas (etapa actual desde el cierre de 2025, "
    "peers Spotify, Netflix, Reddit y Pinterest al cierre del 30-sep-2026 con −10% y el justificado, λ = 0,5 tras el "
    "chequeo de crecimiento implícito). Los consolidados hoy valen ~8% menos que el DCF Base: no se movió ningún múltiplo "
    "para acercarlos. Alertas explicadas: EV/EBITDA (24,2×) por encima del que implica el DCF en FY+3 (14,9×) porque el "
    "mercado paga una monetización más rápida; P/FCFE y P/OCF por debajo porque el flujo de caja suma la compensación en "
    "acciones, que el DCF trata como costo. P/E y EV/FCFF son coherentes con el DCF. El DCF es el valor intrínseco; los "
    "múltiplos son precio relativo."
)

VO, INP, COC, RES, ESC = ("'Valuation output'", "'Input sheet'", "'Cost of capital worksheet'", "'Resumen de Valoración'",
                          "'Escenarios e historias'")

TESIS_ROWS: list[list] = [
    ["DUOL (Duolingo, Inc.) — Tesis de Inversión: De la Historia a los Números (análisis desde cero, 7-oct-2026)"],
    [f'="Metodología Damodaran (NYU Stern) | Precio al 30-sep-2026: US$"&TEXT({RES}!B3;"0.00")&" | WACC inicial: "&TEXT({COC}!B14;"0.00%")'],
    [],
    ["1. LA HISTORIA"],
    ["Duolingo es la aplicación de aprendizaje más usada del mundo y en 2026 eligió crecer en usuarios antes que monetizar: "
     "la audiencia se aceleró (+23%) mientras las reservas se frenaron (+8% en el 2T26). La tensión: si esa audiencia más "
     "grande vuelve a pagar desde 2027 (Base y Optimista) o si Duolingo termina con más usuarios que valen menos, con la IA "
     "generalista como sustituto gratuito (Conservadora y Disrupción). La compensación en acciones (~15% de las ventas) "
     "separa el EBITDA ajustado del margen económico."],
    [],
    ["Caso alcista (Bull)", "Caso bajista (Bear)"],
    ["Usuarios activos diarios +23% en el 2T26 y +27,4% en agosto; retención de usuarios actuales en máximo (84%).",
     "Reservas +8% en el 2T26 y +8,9% guiado para el 3T26: la audiencia crece tres veces más que el dinero."],
    ["El costo de la IA cae (Video Call de US$0,30 a < US$0,01 por llamada) y el margen bruto se sostiene en ~72%.",
     "La compensación en acciones sube a ~15% de las ventas y la dilución bruta es de 3,5-4% al año."],
    ["Sin deuda, US$1.417M de caja e inversiones y flujo libre de ~US$375M; recompra de US$400M.",
     "Asistentes de IA gratuitos pueden practicar idiomas; 83% de los ingresos se cobra por Apple y Google."],
    ["Ajedrez, matemáticas y música como nuevos motores de usuarios; meta de 100M de usuarios diarios en 2028.",
     "Publicidad (+2%), compras en la app (−23%) y English Test (plano) no crecen; la marca no es una ventaja estructural."],
    [],
    ["2. DE LA HISTORIA A LOS NÚMEROS — HISTORIAS EN 'VALUATION OUTPUT' (fórmulas vivas)"],
    ["Supuesto", "Conservadora", "Base", "Optimista", "Justificación y fuente (dato real)"],
    ["Crecimiento de ingresos — Año 1", f"={VO}!C55", f"={VO}!C4", f"={VO}!C106",
     "Base 11,1%: las reservas de 2026 (+10,9%; +8,9% en el 3T26), no el ingreso reportado (+16,3%), carta del 2T26."],
    ["Crecimiento de ingresos — Año 2", f"={VO}!D55", f"={VO}!D4", f"={VO}!D106",
     "Base 12,3%; años 3-5 11,5%, 10,5% y 9,6%: la audiencia más grande se monetiza otra vez."],
    ["Margen operativo — Año 1", f"={VO}!C57", f"={VO}!C6", f"={VO}!C108",
     "18,5%: ~9,5% GAAP (EBITDA ajustado 26,5% − compensación en acciones ~15%) + ~9 pp de I+D capitalizado."],
    ["Margen objetivo (convergencia)", f"={VO}!C45", f"={VO}!C46", f"={VO}!C47",
     "Base 28,0% (~24% GAAP): extremo bajo de Match Group con el doble de I+D; compensación en acciones ~10%."],
    ["Años de convergencia de margen", f"={INP}!B31", f"={INP}!B31", f"={INP}!B31", "5 años: 2026 es un año de inversión deliberada."],
    ["Sales-to-Capital (años 1-5)", f"={INP}!B32", f"={INP}!B32", f"={INP}!B32",
     "2,25 (2,0 en los años 6-10): cerca del de hoy (2,38); el marginal (7,6-14,6) está inflado por los prepagos."],
    ["Costo de capital (WACC)", f"={COC}!B14", f"={COC}!B14", f"={COC}!B14",
     "rf 5,29% (UST 10 años, 30-sep-2026) + beta 1,35 × ERP por regiones 4,82% (Damodaran, oct-2026) = Ke 11,81%."],
    ["Referencia: margen base (B6, con I+D y arrendamientos)", f"={VO}!B6", f"={VO}!B6", f"={VO}!B6",
     "EBIT GAAP LTM US$157M + US$117M de I+D capitalizado + 0,4 de arrendamientos."],
    [],
    ["3. HISTORIAS ACTIVAS Y RESULTADO (DCF Base = valor intrínseco principal; esperado = complemento)"],
    ["Historia", "Probabilidad", "DCF hoy / acción", "Margen objetivo", "CAGR ingresos 1-5"],
    [f"={ESC}!A5", f"={ESC}!B5", f"={ESC}!H5", f"={ESC}!D5", f"={ESC}!C5"],
    [f"={ESC}!A6", f"={ESC}!B6", f"={ESC}!H6", f"={ESC}!D6", f"={ESC}!C6"],
    [f"={ESC}!A7", f"={ESC}!B7", f"={ESC}!H7", f"={ESC}!D7", f"={ESC}!C7"],
    [f"={ESC}!A8", f"={ESC}!B8", f"={ESC}!H8", f"={ESC}!D8", f"={ESC}!C8"],
    ["DCF esperado por probabilidades (complemento)", f"={ESC}!B10", f"={ESC}!H10", "Precio con MOS sobre el esperado", f"={ESC}!H14"],
    ["Múltiplos consolidados hoy (precio relativo, Base)", "", "='Descuento de múltiplos'!D39", "Precio al 30-sep-2026", f"={RES}!B3"],
    [],
    ["4. LOG DE CORRECCIONES Y AJUSTES (respaldo de cada celda en reference/backups/duol_desde_cero_2026-10-07.json del repo JMR-valuation)"],
    ["#", "Celda / componente", "Antes", "Después", "Razón"],
    [1, "Balance Sheet columna L", "Partidas del 31-dic-2025", "Balance al 30-jun-2026 (10-Q 2T26)", "El importador repetía el cierre anual."],
    [2, "Balance Sheet filas 4, 5 y 9 (2024, 2025, LTM)", "Inversiones de corto plazo en 0", "92 · 104 · 133", "Bonos al vencimiento de corto plazo dentro de «otros activos corrientes»."],
    [3, "Income Statement L8 y L11", "SG&A anual (307,6) · otros +14,7", "SG&A LTM 338,1 · otros −15,8", "El importador repetía el SG&A anual; el EBIT LTM (157,1) no cambia."],
    [4, "Income Statement filas 23-27", "Promedio básico 2023-2025 en 0 · acciones LTM 48,3", "41,5 · 43,5 · 45,8 · acciones 46,7", "10-K 2025 y balance del 10-Q 2T26."],
    [5, "Input sheet!B22 / B38", "48,3 M · sin opciones", "49,5 M (con 2,8 M de RSU) · 0,6 M de opciones a US$21,09", "Tabla de títulos dilutivos de la carta del 2T26."],
    [6, "Input sheet!B24 / B62-B63", "Tasa efectiva LTM −103%", "24% · pérdidas fiscales US$111M", "La LTM incluye el beneficio único de 2025 (US$256,7M); guía 23-25%."],
    [7, "Input sheet!B18 y conversor", "Arrendamientos No", "Yes (VP 105)", "Arrendamientos operativos como deuda (Damodaran)."],
    [8, "Cost of capital worksheet", "País de registro", "Beta global · prima por regiones · Kd sintético 5,69%", "62% de las ventas fuera de EE.UU. (10-K 2025)."],
    [9, "Input sheet!B4 / D1 · Resumen C25", "Fecha y precio de la corrida", "30-sep-2026 · US$142,40", "Fecha de corte común de la cartera."],
    [10, "R& D converter B12:B14", "Ejercicios 2025, 2024 y 2023", "12 meses a junio: 273,3 · 206,6 · 179,8", "Los ejercicios se solapaban seis meses con el LTM (margen base 21,8% → 24,0%)."],
    [11, "Descuento de múltiplos fila 38 / 43", "DCF de 'Valuation output' · MOS sobre el ponderado", "Historias · MOS sobre el esperado", "Presentación vigente."],
    [],
    ["5. CONCLUSIÓN"],
    [f'="El DCF Base de las historias es US$"&TEXT({ESC}!H5;"0.00")&" y el esperado US$"&TEXT({ESC}!H10;"0.00")&"; el precio del 30-sep-2026 (US$"&TEXT({RES}!B3;"0.00")&") está "&TEXT({RES}!B3/{ESC}!H5-1;"+0%;-0%")&" frente a la Base. Los múltiplos (US$"&TEXT(\'Descuento de múltiplos\'!D39;"0.00")&") quedan ~8% por debajo del DCF. El DCF es la lectura más confiable: el valor depende de si la audiencia vuelve a pagar en 2027 y de si la compensación en acciones baja, no de un múltiplo de mercado."'],
    ["Variable clave a monitorear: las reservas de 2027 frente al crecimiento de usuarios, la compensación en acciones / ventas y la retención. Si las reservas vuelven a crecer ≥ 16% con usuarios ≥ +20%, el caso se mueve hacia la Optimista; si se quedan en un dígito, hacia la Conservadora; si los usuarios dejan de crecer, hacia la Disrupción."],
    [],
    [SOURCES],
]


def format_estadisticas(sh) -> None:
    est = sh.worksheet("Estadísticas")
    pct = {"numberFormat": {"type": "PERCENT", "pattern": "0.0%"}}
    num = {"numberFormat": {"type": "NUMBER", "pattern": "#,##0"}}
    mult = {"numberFormat": {"type": "NUMBER", "pattern": "0.0\"x\""}}
    cur = {"numberFormat": {"type": "CURRENCY", "pattern": "$0.00"}}
    est.batch_format([
        {"range": "B4:B8", "format": num}, {"range": "B11:B16", "format": pct}, {"range": "B19:B23", "format": pct},
        {"range": "E4:E9", "format": mult}, {"range": "E12", "format": cur},
        {"range": "E20", "format": num},
        {"range": "H4:H15", "format": pct},
    ])


def write_tesis(sh, backup_path) -> None:
    pct = {"numberFormat": {"type": "PERCENT", "pattern": "0.0%"}}
    cur = {"numberFormat": {"type": "CURRENCY", "pattern": "$0.00"}}
    ms.write_tesis(
        sh, TESIS_ROWS, backup_path, text_rows=range(34, 45),
        merges=[f"A{r}:E{r}" for r in (1, 2, 5, 33, 48, 49, 51)] + [f"B{r}:E{r}" for r in range(7, 12)],
        bold_rows=(4, 13, 24, 33, 47), head_rows=(7, 14, 25, 34),
        formats=[
            {"range": "B15:D18", "format": pct}, {"range": "B22:D22", "format": pct},
            {"range": "B19:D19", "format": {"numberFormat": {"type": "NUMBER", "pattern": "0"}}},
            {"range": "B20:D20", "format": {"numberFormat": {"type": "NUMBER", "pattern": "0.00\"x\""}}},
            {"range": "B21:D21", "format": {"numberFormat": {"type": "PERCENT", "pattern": "0.00%"}}},
            {"range": "B26:B30", "format": {"numberFormat": {"type": "PERCENT", "pattern": "0%"}}},
            {"range": "C26:C31", "format": cur}, {"range": "D26:E29", "format": pct},
            {"range": "E30:E31", "format": cur},
        ])
