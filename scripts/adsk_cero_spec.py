"""Ficha de historias de ADSK desde cero (7-oct-2026): escribe reference/damodaran/ADSK.json.

Valoración desde cero de Autodesk con los prompts vigentes (valoración v4, research v5). Las cifras de las historias
(crecimiento por familia de productos, margen, probabilidades) son juicio del analista con la evidencia citada; los valores
por acción los calcula scripts/damodaran_stories.py con el motor que reproduce la hoja.
Márgenes: base del modelo (I+D capitalizado a 3 años, sin el ajuste de arrendamientos, que suma damodaran_stories.py).
Uso: python scripts/adsk_cero_spec.py
"""
from __future__ import annotations

import json
from pathlib import Path

_ROOT = Path(__file__).resolve().parent.parent
OUT = _ROOT / "reference" / "damodaran" / "ADSK.json"

E = "https://www.sec.gov/Archives/edgar/data/769397/"
Q2 = f"[Autodesk, comunicado del 2T FY27, 27-ago-2026]({E}000076939726000059/q227pressrelease.htm)"
Q1 = f"[Autodesk, comunicado del 1T FY27, 28-may-2026]({E}000076939726000041/q127pressrelease.htm)"
Q4 = f"[Autodesk, comunicado del 4T FY26, 26-feb-2026]({E}000076939726000010/q426pressrelease.htm)"
TENQ = f"[Autodesk, 10-Q del 2T FY27, 28-ago-2026]({E}000076939726000061/adsk-20260731.htm)"
TENK = f"[Autodesk, 10-K FY26, 3-mar-2026]({E}000076939726000015/adsk-20260131.htm)"
MX = f"[Autodesk, anuncio de la compra de MaintainX (8-K, anexo 99.1), 28-may-2026]({E}000121390026062125/ea029248301ex99-1.htm)"
MXC = f"[Autodesk, 8-K del cierre de MaintainX, 3-ago-2026]({E}000121390026084276/ea0300009-8k_autodesk.htm)"
BONOS = f"[Autodesk, 8-K de los bonos 2029 y 2033, 10-sep-2026]({E}000119312526387877/d103766d8k.htm)"
REORG = f"[Autodesk, 8-K del plan de reestructuración, 22-ene-2026]({E}000076939726000006/adsk-20260122.htm)"
CALL = ("[The Motley Fool, transcripción de la llamada del 2T FY27, 27-ago-2026]"
        "(https://www.fool.com/earnings/call-transcripts/2026/08/31/autodesk-adsk-q2-2027-earnings-call-transcript/)")
TREFIS = ("[Trefis, «Why Did Autodesk Stock Drop So Soon After Raising Its Forecast?», 10-sep-2026]"
          "(https://www.trefis.com/stock/adsk/articles/614900/why-did-autodesk-stock-drop-so-soon-after-raising-its-forecast/2026-09-10)")

SPEC = {
    "ticker": "ADSK",
    "empresa": "Autodesk, Inc.",
    "fecha": "2026-09-30",
    "industria_damodaran": "Software (System & Application)",
    "historia": (
        "En cinco a diez años Autodesk sigue siendo el sistema de registro del diseño y la obra: Revit, AutoCAD, Civil 3D, "
        "Construction Cloud, Fusion e Inventor guardan los modelos, los planos y los datos de proyectos que los estudios, "
        "constructoras y fabricantes no pueden abandonar sin rehacer años de trabajo. Crece algo por encima de su mercado, "
        "~9-10% nominal compuesto en cinco años: la obra y la nube (AECO, Construction Cloud), Fusion en manufactura y la "
        "operación de activos (MaintainX) crecen a doble dígito; AutoCAD, la franquicia madura, crece con el precio. La IA "
        "no reemplaza al puesto en esta historia: se cobra dentro de la suscripción y, cada vez más, por consumo (Flex). El "
        "margen operativo GAAP pasa de ~26% a ~31% (34% en la base del modelo, con el I+D como inversión) cuando terminan "
        "la reorganización comercial y la dilución de MaintainX, y la compensación en acciones baja de 11% a ~8% de las "
        "ventas. Reinvierte sobre todo en I+D y en compras; el capital de trabajo es negativo porque los clientes pagan por "
        "adelantado. El riesgo es tecnológico (que la IA abarate el diseño y reduzca los puestos) y de ejecución en compras "
        "caras, más que financiero."),
    "filtro": [
        ["Autodesk crece ~10% anual compuesto en cinco años sin compras grandes",
         "Sí",
         f"Sí: 18% en FY26 y 16% en el 2T FY27, con ~1,5-2 pp del nuevo modelo de transacción y ~2 pp de cambio de moneda; "
         f"la facturación orgánica subyacente crece ~10-11% y el RPO corriente +12% ({Q2}; {CALL})",
         "Probable en el rango de 8-11%; el 14-16% reportado de FY27 no se repite en FY28 (el nuevo modelo deja de sumar)"],
        ["El margen operativo GAAP llega a ~31% hacia FY29-FY30",
         "Sí",
         f"Sí: meta de 41% no GAAP en FY29 con compensación en acciones de ~9% de las ventas en FY27 (11% en FY26) ({CALL})",
         "Probable si la compensación en acciones sigue bajando y MaintainX deja de restar; la meta es de la gerencia"],
        ["La IA generativa reduce el número de puestos que compran los clientes de Autodesk",
         "Sí",
         f"Débil hoy: la retención neta de ingresos está en el extremo alto de 100-110% y los ingresos crecen 16% ({TENQ}); el "
         f"mercado sí lo descuenta: la acción cayó 16,6% del 1 al 9-sep-2026 junto con PTC y Bentley ({TREFIS})",
         "Posible a largo plazo; no se observa en las métricas de hoy"],
        ["MaintainX rinde su costo de capital",
         "Sí",
         f"Débil: US$3.575 millones por > US$135 millones de ARR a dic-2026 (~26 veces), sin utilidades ({MX})",
         "Improbable en diez años salvo que crezca > 40% varios años y llegue a márgenes de software maduro"],
    ],
    "tasas_base_nota": (
        "Con ventas LTM pro forma de US$7.880 millones (~US$5.575 millones de 2015) Autodesk está en el tramo de US$4.500-7.000 "
        "millones de The Base Rate Book: media real de crecimiento a 5 años de 5,0% y mediana de 4,1% (más ~2,5% de "
        "inflación para compararlas con cifras nominales). La Base ({cagrA} nominal) queda en el cuartil alto de la "
        "distribución: lo justifican la recurrencia de 97% de los ingresos, el precio que sube con cada renovación y la "
        "obra y la manufactura que se pasan a la nube; aun así, solo ~{tbA} de las empresas de su tamaño creció a ese ritmo."),
    "segmentos": {"AECO": 3895.0, "AutoCAD y AutoCAD LT": 1910.0, "Manufactura": 1488.0, "M&E y otros": 497.0,
                  "MaintainX": 90.0},
    "crecimiento": {
        "texto": (
            "Las ventas LTM (agosto 2025-julio 2026) suman US$7.790 millones (cálculo propio: FY26 + 1S FY27 − 1S FY26, "
            f"{TENK}; {TENQ}): AECO (arquitectura, ingeniería, construcción y operación) US$3.895 millones, AutoCAD y AutoCAD LT "
            "US$1.910 millones, manufactura US$1.488 millones y medios y entretenimiento más otros US$497 millones. A eso se "
            "suman ~US$90 millones de MaintainX (estimación propia: más de US$135 millones de ARR a dic-2026 creciendo más de "
            f"50%, {MX}), comprada el 3-ago-2026 ({MXC}). El crecimiento reportado de FY26 (+18%) y del 2T FY27 (+16%) "
            "exagera el orgánico: el nuevo modelo de transacción, que registra como ingreso bruto lo que antes cobraban los "
            "revendedores, aportó ~2 pp en el 2T FY27 y ~1,5 pp en FY27, y deja de sumar en FY28; el dólar débil sumó ~2 pp "
            f"(16% reportado frente a 14% en moneda constante) ({Q2}; {CALL}). El ritmo subyacente es ~11-12% en ingresos y "
            "~10-11% en facturación orgánica, con la construcción creciendo más de 20%. Fuera de MaintainX no hay compras "
            "grandes en la Base."),
        "tabla": {
            "cols": ["US$ millones", "FY25", "FY26", "LTM jul-26 (cálculo propio)", "2T FY27 interanual", "Moneda constante"],
            "align": ["l", "r", "r", "r", "r", "r"],
            "rows": [
                ["AECO", "2.937", "3.583", "3.895", "+17%", "+15%"],
                ["AutoCAD y AutoCAD LT", "1.572", "1.787", "1.910", "+14%", "+11%"],
                ["Manufactura", "1.189", "1.379", "1.488", "+15%", "+12%"],
                ["M&E y otros", "433", "457", "497", "+19%", "~+17%"],
                ["Total reportado", "6.131", "7.206", "7.790", "+16%", "+14%"],
                ["MaintainX (pro forma, estimación)", "—", "—", "~90", "> +50% (ARR)", "—"],
            ],
        },
    },
    "margenes": {
        "texto": (
            "El margen operativo GAAP LTM es 26,2% (EBIT de US$2.041 millones). Incluye US$134 millones de reestructuración "
            f"(el último tramo del plan de ventas de enero de 2026, {REORG}) que este análisis NO excluye: Autodesk registró "
            "cargos de reestructuración en FY25, FY26 y FY27, así que se tratan como costo recurrente. Incluye también la "
            "compensación en acciones (~9% de las ventas en FY27, 11% en FY26), que es un costo económico, y la amortización de "
            "intangibles comprados (~2% de las ventas). Con MaintainX pro forma (pérdida estimada de US$80 millones) el margen "
            "GAAP es 24,9%; con el I+D tratado como inversión (Damodaran: se suma el I+D del año y se resta la amortización del "
            "activo de I+D a tres años) es 27,7%, que es la base del modelo. La guía de FY27 es 25-27% GAAP y ~39% no GAAP, con "
            f"meta de 41% no GAAP en FY29 ({Q2}; {CALL}). El comparable maduro es Adobe (margen GAAP ~36%, 40% en la base del "
            "modelo con I+D capitalizado): Autodesk vende más por canal y tiene más mantenimiento de productos de escritorio, "
            "así que el objetivo de la Base (34% en la base del modelo, ~31% GAAP) queda por debajo del de Adobe y en línea con "
            "la meta de la gerencia menos la compensación en acciones."),
    },
    "reinversion": {
        "texto": (
            "El crecimiento orgánico pide poco capital físico (capex de ~US$70 millones al año, ~1% de las ventas) y nada de "
            "capital de trabajo: los ingresos diferidos (US$4.258 millones) financian a la empresa. La reinversión real es el "
            "I+D (~22% de las ventas), que el modelo trata como inversión con vida de tres años, y las compras. MaintainX costó "
            f"US$3.530 millones netos de caja ({TENQ}, nota 19) por un negocio de ~US$120 millones de ingresos anualizados sin "
            "utilidades: con un margen maduro de 30% y un impuesto de 25%, rendiría ~1% sobre lo pagado hoy y necesitaría "
            "multiplicar sus ventas por más de diez para cubrir un costo de capital de ~11%. Por eso el ROIC con el capital pro "
            "forma (17,9%, 'Valuation output'!B42) es menor que el de antes de la compra (~28%). La hoja usa un ventas/capital de "
            "1,25 (1,21 con el capital arrendado) en los diez años: con el margen objetivo y un impuesto de 25%, cada dólar de "
            "capital nuevo rinde ~32%, por encima del ROIC actual y por debajo del orgánico, porque Autodesk también compra "
            "crecimiento con regularidad."),
        "tabla": {
            "cols": ["Compra", "Precio pagado", "Ventas", "Retorno sobre lo pagado (cálculo propio)"],
            "align": ["l", "r", "r", "l"],
            "rows": [
                ["MaintainX (ago-2026)", "US$3.530M netos de caja (US$3.575M brutos)", "ARR > US$135M a dic-2026",
                 "Negativo hoy; ~1% después de impuestos con margen de 30% sobre las ventas de 2026"],
            ],
        },
    },
    "riesgo": {
        "beta_propuesta": None,
        "texto": (
            "La hoja usa la beta bottom-up de Software (System & Application) de la tabla global de Damodaran (enero de 2026), "
            "desapalancada 1,33 y reapalancada con la deuda de mercado de Autodesk (D/E ~10%): ~1,43. Se usa la global porque el "
            "65% de las ventas está fuera de EE.UU. (EMEA 39%, Asia Pacífico 17%); la de EE.UU. se informa como sensibilidad. "
            "La prima de mercado (4,77%) pondera la madura de 3,70% por las regiones de venta. La amenaza de la IA, la "
            "reorganización comercial y la concentración en la construcción son riesgos propios y diversificables: van en las "
            "historias Conservadora y Disrupción, no en la tasa."),
    },
    "historias": [
        {
            "id": "A", "tesis": "base", "prob": 0.45, "margen": 0.34,
            "nombre": "Base · Sistema de registro del diseño y la obra que crece a doble dígito bajo",
            "crec": {"AECO": [0.12, 0.11, 0.10, 0.09, 0.08],
                     "AutoCAD y AutoCAD LT": [0.09, 0.08, 0.07, 0.06, 0.05],
                     "Manufactura": [0.10, 0.10, 0.09, 0.08, 0.07],
                     "M&E y otros": [0.07, 0.06, 0.05, 0.05, 0.04],
                     "MaintainX": [0.55, 0.40, 0.32, 0.25, 0.20]},
            "tesis_que": (
                "La facturación orgánica sigue en ~10-11% y el ingreso en ~11% el primer año, sin el empujón del nuevo modelo "
                "de transacción ni del dólar; AECO crece por encima del promedio con la construcción y la nube; AutoCAD crece "
                "con el precio; Fusion sostiene la manufactura. MaintainX crece 55% el primer año y se modera a 20%. El margen "
                "llega a 34% en la base del modelo (~31% GAAP) en cinco años: termina la reorganización, la compensación en "
                f"acciones baja a ~8% y MaintainX deja de restar. La IA se cobra dentro de la suscripción y por consumo ({CALL})."),
            "tesis_contraste": "Facturación orgánica ≥ 9% en FY28, retención neta ≥ 100% y margen no GAAP ≥ 40% en FY28-FY29.",
        },
        {
            "id": "B", "tesis": "conservadora", "prob": 0.25, "margen": 0.30,
            "nombre": "Conservadora · Crecimiento de un dígito y margen que se queda donde está",
            "crec": {"AECO": [0.09, 0.08, 0.07, 0.06, 0.05],
                     "AutoCAD y AutoCAD LT": [0.06, 0.04, 0.03, 0.03, 0.02],
                     "Manufactura": [0.07, 0.07, 0.06, 0.05, 0.04],
                     "M&E y otros": [0.04, 0.03, 0.02, 0.02, 0.02],
                     "MaintainX": [0.45, 0.30, 0.25, 0.20, 0.15]},
            "tesis_que": (
                "La reorganización comercial cuesta más clientes nuevos de lo previsto (Europa occidental ya va atrasada, "
                f"{CALL}), la construcción se enfría con tasas altas y la IA presiona el precio por puesto en AutoCAD LT y en "
                "los clientes chicos. Autodesk conserva su base instalada, pero crece a un dígito y la mejora de margen se "
                "gasta en IA (cómputo que comprime el margen bruto) y en integrar MaintainX: el margen se queda en 30% en la "
                "base del modelo (~27% GAAP)."),
            "tesis_contraste": "Facturación orgánica < 8% en FY28, retención neta < 100% o margen no GAAP ≤ 39% en FY28.",
        },
        {
            "id": "C", "tesis": "disrupción", "prob": 0.15, "margen": 0.24,
            "nombre": "Disrupción · Deterioro de los fundamentales",
            "descripcion": "La IA abarata el diseño y los clientes compran menos puestos",
            "roic_terminal": "costo_capital", "terminal": "estabilizacion", "s2c": 0.9,
            "crec": {"AECO": [0.06, 0.03, 0.01, 0.0, 0.0],
                     "AutoCAD y AutoCAD LT": [0.02, -0.03, -0.05, -0.06, -0.06],
                     "Manufactura": [0.04, 0.01, 0.0, -0.01, -0.01],
                     "M&E y otros": [0.0, -0.04, -0.05, -0.05, -0.05],
                     "MaintainX": [0.35, 0.15, 0.10, 0.05, 0.05]},
            "tesis_que": (
                "Herramientas de diseño generativo y agentes que producen planos y modelos a partir de texto reducen el número "
                "de dibujantes y modeladores que necesitan los estudios; AutoCAD LT, el producto más expuesto, pierde puestos; "
                "los formatos abiertos (IFC, USD) y los nuevos competidores bajan los costos de cambio; MaintainX no despega. "
                "Las ventas dejan de crecer en cinco años, el margen baja a 24% en la base del modelo porque Autodesk sigue "
                "gastando en I+D y en IA para defenderse (ventas/capital de 0,9: el capital nuevo rinde ~16%, no el 32% de la "
                "Base), y la ventaja desaparece: después del año 10 el ROIC es el costo de capital."),
            "tesis_contraste": "Retención neta < 95% dos trimestres seguidos o caída interanual de suscripciones de AutoCAD LT.",
        },
        {
            "id": "D", "tesis": "optimista", "prob": 0.15, "margen": 0.38,
            "nombre": "Optimista · Plataforma de datos del ciclo de vida que cobra por la IA",
            "crec": {"AECO": [0.14, 0.13, 0.12, 0.11, 0.10],
                     "AutoCAD y AutoCAD LT": [0.10, 0.09, 0.08, 0.07, 0.06],
                     "Manufactura": [0.12, 0.11, 0.10, 0.09, 0.08],
                     "M&E y otros": [0.08, 0.07, 0.06, 0.06, 0.05],
                     "MaintainX": [0.60, 0.45, 0.35, 0.28, 0.22]},
            "tesis_que": (
                "Los datos de proyectos que Autodesk guarda (diseño, obra y operación) se vuelven la ventaja de sus modelos de "
                "IA: los asistentes y los modelos 3D propios se cobran por consumo (Flex, cuyo mínimo bajó de US$300 a US$99) "
                "y suben el ingreso por cliente; la construcción y la manufactura en la nube sostienen doble dígito y MaintainX "
                "conecta la operación con el diseño. El margen llega a 38% en la base del modelo (~35% GAAP), como Adobe."),
            "tesis_contraste": "Facturación orgánica ≥ 12% en FY28, ingresos por consumo visibles y margen no GAAP ≥ 42%.",
        },
    ],
    "prob_texto": (
        "La Base pesa 45%: es la extrapolación de lo que ya se ve (facturación orgánica ~10-11%, RPO corriente +12%, retención "
        "neta en el extremo alto de su rango) y de la meta de margen de la gerencia, sin el crecimiento prestado del nuevo "
        "modelo de transacción. La Conservadora pesa 25% porque la reorganización comercial todavía no termina, Europa "
        "occidental va atrasada y la construcción depende de las tasas. La Disrupción pesa 15%: no hay evidencia de pérdida "
        "de puestos hoy, pero el mercado la descuenta y la IA puede cambiar la economía del diseño en una década. La "
        "Optimista pesa 15% porque exige monetizar la IA por consumo, algo que Autodesk todavía no muestra en cifras. Son "
        "juicio del analista, no frecuencias publicadas."),
    "premortem": [
        "La IA generativa reduce los puestos de dibujo y modelado: AutoCAD LT y los clientes chicos de AECO renuevan menos asientos y la retención neta baja de 100%.",
        "La reorganización comercial de 2026 rompe relaciones con los revendedores y deja de generar clientes nuevos en Europa occidental, que ya va atrasada.",
        "MaintainX no crece lo prometido y se convierte en un deterioro de plusvalía de miles de millones, como otras compras caras de software.",
        "El costo de cómputo de la IA comprime el margen bruto (91%) más de lo que la gerencia anticipó y la meta de 41% no GAAP se aleja.",
        "Un ciclo largo de tasas altas frena la construcción y la manufactura, y el crecimiento cae a un dígito bajo durante varios años.",
    ],
    "contra": (
        f"el crecimiento reportado de 16-18% está inflado por el nuevo modelo de transacción y el dólar ({CALL}), el RPO total "
        "crece apenas 2% por el fin de los descuentos plurianuales, Autodesk pagó ~26 veces el ARR por MaintainX y la "
        f"reorganización comercial sigue en curso ({REORG})."),
    "indicadores": [
        ["Facturación orgánica (sin MaintainX)", "~10-11% (guía FY27)", "≥ 11%", "≤ 8%"],
        ["Retención neta de ingresos (NR3, moneda constante)", "Extremo alto de 100-110% (2T FY27)", "≥ 105%", "< 100%"],
        ["RPO corriente", "US$5.245M, +12% (2T FY27)", "≥ +12%", "≤ +8%"],
        ["Margen operativo no GAAP", "~39% (guía FY27)", "≥ 40% en FY28", "≤ 38%"],
        ["Compensación en acciones / ventas", "~9% (FY27)", "≤ 8%", "≥ 10%"],
        ["Crecimiento de AutoCAD y AutoCAD LT", "+14% (+11% en moneda constante, 2T FY27)", "≥ +8%", "≤ +3%"],
        ["MaintainX: ARR", "> US$135M a dic-2026 (> +50%)", "≥ +40% en 2027", "≤ +25%"],
        ["Acciones en circulación", "209 M (21-ago-2026); recompras de US$901M en el 1S FY27", "Bajan ≥ 1% al año", "Suben"],
    ],
    "margenes_inverso": [0.30, 0.34, 0.38],
    "precio_lectura": (
        "El precio pide algo más que la Base: con su margen y su beta, el DCF inverso exige crecer en los años 1-5 más que el "
        "{cagrA} anual de la Base (ver la tabla), y queda lejos del esperado porque no le da casi peso a la Disrupción. ¿Qué "
        "sabe el mercado que yo no? Puede estar pagando por una monetización de la IA por consumo que todavía no se ve en las "
        "cifras (la Optimista), por un costo de capital menor que el de la hoja (con la beta de la tabla de EE.UU. o una prima "
        "sin ponderar por regiones el DCF Base sube) o por más años de retornos altos. En sentido contrario, la caída de "
        "septiembre muestra que también descuenta el riesgo de la IA sobre los puestos; ninguna de las dos lecturas se "
        f"observa todavía en la facturación ni en la retención neta del 2T FY27 ({Q2})."),
    "frase": "Sistema de registro del diseño y la obra: crece ~10% sin el impulso contable de FY27 y lleva el margen GAAP a ~31%",
    "confianza": ("Media: la recurrencia, la retención y la meta de margen están documentadas; el efecto de la IA sobre los "
                  "puestos y el retorno de MaintainX no"),
    "cambiaria": "La retención neta de ingresos, la facturación orgánica de FY28, el margen no GAAP y el ARR de MaintainX",
    "revision": "Resultados del 3T FY27 (fines de noviembre de 2026)",
    "fuentes": [
        ["Autodesk, comunicado del 2T FY27 (27-ago-2026)", f"{E}000076939726000059/q227pressrelease.htm"],
        ["Autodesk, 10-Q del 2T FY27 (28-ago-2026)", f"{E}000076939726000061/adsk-20260731.htm"],
        ["Autodesk, comunicado del 1T FY27 (28-may-2026)", f"{E}000076939726000041/q127pressrelease.htm"],
        ["Autodesk, comunicado del 4T FY26 (26-feb-2026)", f"{E}000076939726000010/q426pressrelease.htm"],
        ["Autodesk, 10-K FY26 (3-mar-2026)", f"{E}000076939726000015/adsk-20260131.htm"],
        ["Autodesk, 8-K del plan de reestructuración (22-ene-2026)", f"{E}000076939726000006/adsk-20260122.htm"],
        ["Autodesk, anuncio de la compra de MaintainX (28-may-2026)", f"{E}000121390026062125/ea029248301ex99-1.htm"],
        ["Autodesk, 8-K del préstamo puente y la línea de crédito (15-jun-2026)", f"{E}000121390026068533/ea0294709-8k_autodesk.htm"],
        ["Autodesk, 8-K del programa de papel comercial (13-jul-2026)", f"{E}000121390026077574/ea0296272-8k_autodesk.htm"],
        ["Autodesk, 8-K del cierre de MaintainX (3-ago-2026)", f"{E}000121390026084276/ea0300009-8k_autodesk.htm"],
        ["Autodesk, 8-K de los bonos 2029 y 2033 (10-sep-2026)", f"{E}000119312526387877/d103766d8k.htm"],
        ["The Motley Fool, transcripción de la llamada del 2T FY27 (27-ago-2026)", "https://www.fool.com/earnings/call-transcripts/2026/08/31/autodesk-adsk-q2-2027-earnings-call-transcript/"],
        ["Trefis, caída de la acción tras la guía (10-sep-2026)", "https://www.trefis.com/stock/adsk/articles/614900/why-did-autodesk-stock-drop-so-soon-after-raising-its-forecast/2026-09-10"],
        ["Damodaran, ERP implícita de octubre de 2026", "https://pages.stern.nyu.edu/~adamodar/pc/implprem/ERPOct26.xlsx"],
        ["Damodaran, betas por industria (enero de 2026)", "https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/Betas.html"],
        ["Mauboussin y Callahan, The Base Rate Book (2016)", "https://www.credit-suisse.com/media/assets/corporate/docs/about-us/research/publications/the-base-rate-book-integrating-the-past-to-better-anticipate-the-future.pdf"],
    ],
    "arrendamientos": {
        "vp": 233.71, "ajuste_ebit": 19.048, "margen_pp": 19.048 / 7880, "capital_ventas": 233.71 / 7880,
        "cierre": "2026-01-31",
        "criterio": "Damodaran: arrendamientos operativos como deuda; EBIT + gasto − depreciación del activo",
    },
    "justificacion": [
        ["Crecimiento: el orgánico, sin el empujón contable de FY27.",
         "La Base crece {g1A} el primer año y {cagrA} compuesto en cinco años. El primer año es el ritmo subyacente de hoy "
         "(facturación orgánica ~10-11%, RPO corriente +12%) sin los ~1,5 pp del nuevo modelo de transacción, que deja de "
         "sumar en FY28, ni los ~2 pp del dólar débil, más ~US$50 millones de MaintainX. Después cada familia se modera "
         "hacia el crecimiento de su mercado: AECO y manufactura de 12% y 10% a 8% y 7%; AutoCAD de 9% a 5%. La visión "
         "externa dice que ~{tbA} de las empresas de su tamaño logró al menos ese crecimiento: la Base es exigente, y la "
         "sostienen la recurrencia (97% de los ingresos) y el precio. La alternativa de 14-15% supone repetir el ritmo "
         "reportado de FY27, que tenía un componente contable. Sensibilidad: ±2 puntos de crecimiento en los años 1-5 llevan "
         "el DCF Base a {s_g_lo} y {s_g_hi}. Obligaría a revisarlo una facturación orgánica de un dígito en FY28 (hacia la "
         "Conservadora, {cagrB}) o ingresos por consumo de IA visibles (hacia la Optimista, {cagrD})."],
        ["Margen: la meta de la gerencia menos la compensación en acciones.",
         "La Base parte de {margenY1} el primer año (la guía de FY27, 25-27% GAAP, llevada a la base del modelo con el I+D "
         "capitalizado) y llega a {mA} en {conv} años ({mrepA} antes del ajuste de arrendamientos, +{arr_pp} pp), ~31% GAAP. "
         "Es la meta de 41% no GAAP de FY29 menos ~8 puntos de compensación en acciones y ~2 de amortización de compras: el "
         "modelo trata la compensación en acciones como costo. Adobe (40% en la misma base) no es el ancla porque Autodesk "
         "vende más por canal y mantiene productos de escritorio. Sensibilidad: ±2 puntos de margen dan {s_m_lo} y {s_m_hi}. "
         "La Conservadora ({mB}) supone que la mejora se gasta en IA; la Disrupción ({mC}), pérdida de escala; la Optimista "
         "({mD}), monetización de la IA por consumo."],
        ["Reinversión: I+D y compras, no capital de trabajo.",
         "El ventas/capital es {s2c1} en los años 1-5 y {s2c2} en los años 6-10 (~US${cap1} de capital por dólar de ventas "
         "nuevas, con el activo de I+D y los arrendamientos). Con el margen objetivo y un impuesto de 25%, el capital nuevo rinde "
         "~32%: por encima del ROIC actual pro forma (17,9%), deprimido por los US$3.530 millones de MaintainX, y por debajo del "
         "orgánico, porque Autodesk compra crecimiento con regularidad. Un ventas/capital más alto (el marginal orgánico "
         "supera 3) supondría que no hay más compras. Con ±20% en el ventas/capital el DCF Base va de {s_s_lo} a {s_s_hi}."],
        ["Descuento y largo plazo: beta del sector y ventaja durable.",
         "El costo de capital inicial es {wacc0} (tasa libre de riesgo {rf} al {fecha_corte}, prima de mercado {erp} de "
         "Damodaran a {mes_erp} ponderada por regiones, beta {beta}, costo de la deuda 5,65% antes de impuestos) y el terminal "
         "{waccT}. Después del año 10 el crecimiento es {tgA} y el ROIC terminal es {roicT}: Autodesk gana por encima de su "
         "costo de capital desde hace años, tiene costos de cambio y estándares de archivo (DWG, Revit) identificables y no se "
         "ve erosión hoy, así que la ventaja es durable; el ROIC de la industria (20,6% en la base del modelo) se topa en el "
         "ROIC actual pro forma (17,9%). El terminal pesa {terminal} del valor operativo. ±1 punto de tasa da {s_k_lo} y "
         "{s_k_hi}; con el ROIC terminal igual al costo de capital el DCF Base sería {s_roic}."],
        ["Acciones, deuda y MaintainX: el balance es el de después de la compra.",
         "Se usan {acciones} millones de acciones (209 millones al 21-ago-2026, portada del 10-Q, más 5,4 millones de RSU y PSU "
         "sin consolidar); Autodesk no tiene opciones relevantes. La caja (US$1.625 millones) y la deuda (US$4.500 millones a "
         f"valor nominal) son las del 31-jul-2026 ajustadas por la compra de MaintainX y su financiamiento ({TENQ}; {BONOS}): "
         "comprar con caja y deuda baja el patrimonio en lo pagado, y el valor de MaintainX vuelve por sus ventas en las "
         "historias. Una dilución adicional de 5% llevaría el DCF Base a {s_acc}. Las recompras (~50% del flujo libre) no se "
         "modelan como valor adicional: a precio justo no crean ni destruyen valor."],
        ["Probabilidades y lectura del resultado.",
         "Con {pA} para la Base, {pB} para la Conservadora, {pC} para la Disrupción y {pD} para la Optimista, el DCF esperado es "
         "{ve} frente a un DCF Base de {vA}. Con el margen de seguridad de {mos}, el precio de compra con margen es {vmos}."],
    ],
}


def _agrupar(spec: dict) -> dict:
    """La pestaña «Escenarios e historias» admite cuatro segmentos (build_story_sheet.SLOTS): Manufactura y «M&E y
    otros» se suman en uno, con el crecimiento combinado de cada año (reproduce exactamente los ingresos de las dos
    familias). El detalle por familia queda en «crec_detalle» y «segmentos_detalle»."""
    juntar, nuevo = ("Manufactura", "M&E y otros"), "Manufactura, M&E y otros"
    seg0 = spec["segmentos"]
    spec["segmentos_detalle"] = dict(seg0)
    spec["segmentos"] = {k: v for k, v in seg0.items() if k not in juntar}
    spec["segmentos"] = {"AECO": seg0["AECO"], "AutoCAD y AutoCAD LT": seg0["AutoCAD y AutoCAD LT"],
                         nuevo: sum(seg0[k] for k in juntar), "MaintainX": seg0["MaintainX"]}
    for h in spec["historias"]:
        h["crec_detalle"] = dict(h["crec"])
        rev = {k: seg0[k] for k in juntar}
        comb = []
        for y in range(5):
            antes = sum(rev.values())
            for k in juntar:
                rev[k] *= 1 + h["crec"][k][y]
            comb.append(round(sum(rev.values()) / antes - 1, 6))
        h["crec"] = {"AECO": h["crec"]["AECO"], "AutoCAD y AutoCAD LT": h["crec"]["AutoCAD y AutoCAD LT"],
                     nuevo: comb, "MaintainX": h["crec"]["MaintainX"]}
    return spec


def main() -> int:
    OUT.write_text(json.dumps(_agrupar(SPEC), ensure_ascii=False, indent=1))
    print("escrito", OUT)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
