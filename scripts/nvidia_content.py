"""Contenido cualitativo de la valoracion de NVIDIA Corporation (NVDA).
Las cifras de resultado de la Tesis son formulas vivas contra el modelo;
las cifras de negocio citadas en el texto salen de los propios estados
financieros de la hoja (SEC EDGAR, XBRL, CIK 0001045810), no de memoria,
salvo los hechos generales marcados como tales (segmentos, CEO,
estructura de clientes, controles de exportacion)."""
from __future__ import annotations

import model_steps as ms

SOURCES = (
    "Fuentes: estados financieros del modelo (SEC EDGAR, XBRL, 10-K y 10-Q de NVIDIA Corp, "
    "CIK 0001045810); Damodaran Online (indname.xls, industria 'Semiconductor'; ERPbymonth; "
    "Country equity risk premiums); UST 10 años y precio de NVDA vía yfinance (fecha del análisis). "
    "No se citan titulares de prensa de trimestres específicos por no tener una fuente verificada al "
    "momento de escribir esta hoja -- actualizar en la próxima revisión con los datos del trimestre "
    "más reciente."
)

CUALITATIVO = {
    "B5": "NVIDIA Corporation",
    "B6": "Jen-Hsun (Jensen) Huang — Fundador, Presidente y CEO desde 1993, miembro del Directorio desde entonces.",
    "B7": "Semiconductores / Cómputo acelerado — diseño fabless de GPUs y sistemas para IA (Damodaran: Semiconductor)",
    "B8": "https://www.nvidia.com  |  IR: https://investor.nvidia.com",
    "B11": "Descripción",
    "B12": ("Nvidia diseña unidades de procesamiento gráfico (GPU) y sistemas completos de cómputo acelerado, "
            "con un modelo fabless (no fabrica sus propios chips: TSMC los produce). Reporta en dos segmentos "
            "contables (Compute & Networking y Graphics) que se desglosan por línea de producto en Data Center "
            "(GPUs e infraestructura de red para entrenar e inferir modelos de IA), Gaming (GeForce), "
            "Professional Visualization (Quadro/RTX profesional) y Automotive (plataformas de conducción "
            "asistida/autónoma). Ingresos LTM de US$302.970M con un margen operativo de 65,2%."),
    "A13": "Data Center (GPUs e infraestructura de IA)",
    "B13": ("El segmento dominante: entrenamiento e inferencia de modelos de IA para hiperescaladores de nube, "
            "laboratorios de IA y empresas. Su moat central es CUDA, la plataforma de software propietaria que "
            "corre solo sobre GPUs de Nvidia y que casi todo el ecosistema de IA (frameworks, librerías, "
            "investigadores) usa como estándar de facto, generando altísimos costos de cambio para el cliente."),
    "A14": "Gaming (GeForce)",
    "B14": ("El negocio histórico de Nvidia: GPUs para videojuegos en PC. Crece con normalidad de mercado maduro "
            "(un dígito alto), muy por debajo del ritmo de Data Center, pero sigue siendo una fuente de caja "
            "estable y de escala relevante en términos absolutos."),
    "A15": "Professional Visualization y Automotive",
    "B15": ("Segmentos más chicos: estaciones de trabajo profesionales (diseño, renderizado) y plataformas de "
            "conducción asistida/autónoma para fabricantes de autos. Crecimiento de doble dígito pero de escala "
            "menor frente a Data Center; opcionalidad de largo plazo más que motor de valoración actual."),
    "A16": "Concentración de clientes e hiperescaladores",
    "B16": ("Una porción muy significativa de los ingresos de Data Center proviene de un número reducido de "
            "hiperescaladores (los mismos que están construyendo sus propios ASICs de IA: TPU de Google, "
            "Trainium de Amazon, Maia de Microsoft, MTIA de Meta). Esta concentración de clientes es, a la vez, "
            "la fuente de la escala actual del negocio y su mayor riesgo estructural de mediano plazo."),
    "B21": "Argumento",
    "A22": "CUDA como foso de software, no solo de hardware",
    "B22": ("A diferencia de un fabricante de commodities, Nvidia vende una plataforma de software (CUDA) que "
            "lleva casi dos décadas siendo el estándar de la industria para computación paralela e IA. Migrar a "
            "un ASIC propio o a un competidor implica reescribir y revalidar software, un costo de cambio real "
            "que sostiene el poder de fijación de precios de Nvidia incluso frente a chips de la competencia con "
            "especificaciones técnicas competitivas."),
    "A23": "Balance neto de caja y recompras",
    "B23": ("Caja e inversiones de US$22.443M contra una deuda financiera total (corto plazo + largo plazo + "
            "arrendamientos) de US$11.040M: posición de caja neta positiva, calificación crediticia real Aa1/AA "
            "(muy sólida). Nvidia no paga un dividendo material y prioriza la recompra de acciones como "
            "mecanismo de retorno de capital."),
    "A24": "Demanda de cómputo de IA con oferta restringida",
    "B24": ("La compañía describe su propio crecimiento reciente como 'limitado por la oferta' (supply-"
            "constrained), no por la demanda: la capacidad de fabricación de TSMC y de empaquetado avanzado "
            "(CoWoS/HBM) es hoy la restricción principal, no la cantidad de clientes dispuestos a comprar. Esto "
            "sostiene un poder de fijación de precios inusual para un fabricante de semiconductores."),
    "B27": "Riesgo",
    "A28": "ASICs propios de los hiperescaladores",
    "B28": ("Google (TPU), Amazon (Trainium), Microsoft (Maia) y Meta (MTIA) desarrollan sus propios "
            "aceleradores de IA para reducir su dependencia de Nvidia, con una tasa de crecimiento del mercado "
            "de ASICs a medida muy superior a la del mercado de GPUs de propósito general. El riesgo de cola de "
            "la tesis es que la sustitución de GPUs por ASICs propios en cargas de trabajo de inferencia erosione "
            "la cuota de mercado y el margen de Nvidia más rápido de lo que el crecimiento total del mercado de "
            "IA puede compensar."),
    "A29": "Controles de exportación a China",
    "B29": ("El gobierno de EE.UU. restringe la venta de los chips de IA más avanzados de Nvidia a China desde "
            "2022, con episodios adicionales de restricción/autorización parcial (H20) durante 2025-2026 que ya "
            "le costaron a la compañía miles de millones de dólares en ingresos no reconocidos y cargos por "
            "inventario. La política sigue siendo cambiante y es un riesgo regulatorio genuino, no solo "
            "coyuntural."),
    "A30": "Concentración de clientes",
    "B30": ("Una proporción muy alta de los ingresos de Data Center proviene de un puñado de hiperescaladores. "
            "Si alguno de ellos redujera de forma material sus compras (por migración a ASICs propios, por un "
            "recorte de capex de IA, o por saturación de capacidad), el impacto sobre los ingresos consolidados "
            "sería desproporcionado frente a un negocio con una base de clientes más diversificada."),
}

ESTADISTICAS = {
    "B4": "='Trailing Valuation'!L5", "B5": "='Trailing Valuation'!L6", "B6": "='Input sheet'!B22",
    "B7": "='Income Statement'!L3", "B8": 40000,  # empleados a tiempo completo (10-K mas reciente)
    "B12": "='Income Statement'!L30", "B13": "='Income Statement'!L13",
    "B14": "='Income Statement'!L19/'Income Statement'!L3", "B15": "='Income Statement'!L22/'Income Statement'!L3",
    "B16": "='Márgenes'!L9",
    "B21": "='Eficiencia de capital'!L5", "B23": "='Eficiencia de capital'!L3",
    "E4": "='Trailing Valuation'!L13", "E5": "='Trailing Valuation'!L18", "E6": "='Trailing Valuation'!L19",
    "E7": "='Trailing Valuation'!L21", "E8": "='Trailing Valuation'!L16", "E9": "='Trailing Valuation'!L20",
    "E12": "='Resumen de Valoración'!D12",
    "E13": "=PE!F19", "E14": "=E4/('Input sheet'!B29*100)",
    "E16": "=IFERROR('Trailing Valuation'!L6/'Financials Multiples'!E57;\"\")",
    "E20": "='Balance Sheet'!L5", "E23": "='Income Statement'!L12/'Income Statement'!L16",
    "H4": "=IF('Income Statement'!H3<0;\"N/A (base negativa)\";IFERROR(('Income Statement'!K3/'Income Statement'!H3)^(1/3)-1;\"\"))",
    "H5": "=IF('Income Statement'!F3<0;\"N/A (base negativa)\";IFERROR(('Income Statement'!K3/'Income Statement'!F3)^(1/5)-1;\"\"))",
    "H6": "=IF('Income Statement'!B3<0;\"N/A (base negativa)\";IFERROR(('Income Statement'!K3/'Income Statement'!B3)^(1/9)-1;\"\"))",
    "H7": "=IF('Income Statement'!H24<0;\"N/A (base negativa)\";IFERROR(('Income Statement'!K24/'Income Statement'!H24)^(1/3)-1;\"\"))",
    "H8": "=IF('Income Statement'!F24<0;\"N/A (base negativa)\";IFERROR(('Income Statement'!K24/'Income Statement'!F24)^(1/5)-1;\"\"))",
    "H9": "=IF('Income Statement'!B24<0;\"N/A (base negativa)\";IFERROR(('Income Statement'!K24/'Income Statement'!B24)^(1/9)-1;\"\"))",
    "H10": "=IF('Cash Flow Statement'!F36<0;\"N/A (base negativa)\";IFERROR(('Cash Flow Statement'!K36/'Cash Flow Statement'!F36)^(1/5)-1;\"\"))",
    "H11": "=IF('Income Statement'!F26<0;\"N/A (base negativa)\";IFERROR(('Income Statement'!K26/'Income Statement'!F26)^(1/5)-1;\"\"))",
    "H12": "N/D (guía externa; sin dato verificado para esta empresa)",
    "H13": "N/D (guía externa; sin dato verificado para esta empresa)",
    "H14": "N/D (guía externa; sin dato verificado para esta empresa)",
    "H15": "N/D (guía externa; sin dato verificado para esta empresa)",
    "H18": "N/D (Nvidia no paga un dividendo material; prioriza recompra de acciones)",
    "H19": "N/D (sin dividendo material)", "H20": "N/D (sin dividendo material)",
    "H21": "N/D (sin dividendo material)",
    "H22": "N/D (sin dividendo material)", "H23": "N/D (sin dividendo material)",
}

STORIES = {
    "A3": "Nvidia: el proveedor casi monopólico de cómputo de IA, con CUDA como foso de software y la concentración de clientes como principal riesgo",
    "A4": ("Nvidia genera US$302.970M de ingresos LTM con un margen operativo de 65,2% y una posición de caja "
           "neta positiva (US$22.443M de caja e inversiones contra US$11.040M de deuda financiera total). El "
           "crecimiento se desaceleró de +65% (año fiscal 2026 completo) a +40% (LTM) a medida que la base de "
           "comparación crece, aunque Data Center siguió acelerando en el trimestre más reciente reportado en la "
           "hoja. La tesis Base asume una desaceleración deliberada frente al ritmo actual y frente a la propia "
           "guía de la compañía (que apunta a un crecimiento de ~70% para el próximo año fiscal, calificado por "
           "la propia empresa como 'limitado por la oferta'): no tomamos esa guía como caso central porque "
           "asume que la única restricción es la capacidad de fabricación, sin ceder nada de cuota a los ASICs "
           "propios de los hiperescaladores. El riesgo estructural de más largo plazo es que esa cesión de cuota "
           "sea más rápida de lo que el crecimiento total del mercado de cómputo de IA puede compensar."),
    "G10": "Año 1 Base 50%: desaceleración deliberada frente al crecimiento reciente de Data Center (+117% i.a. en el trimestre más reciente) y frente a la mitad de la propia guía de la compañía para el próximo año fiscal (~70%, 'limitado por la oferta').",
    "G11": "Margen operativo Año 1 en línea con el margen GAAP LTM real (65,2%), con el margen objetivo Base cediendo levemente (58%) por presión de precio de los ASICs propios de los hiperescaladores y mezcla de producto.",
    "G12": "Tasa marginal de largo plazo 16%: corporativa de EE.UU. (21%) neta de la tasa efectiva histórica más baja de Nvidia (créditos fiscales, mezcla geográfica).",
    "G13": "3,0x: diseño fabless de chips (TSMC fabrica), relativamente liviano en capital fijo propio frente a un fabricante integrado.",
    "G14": "ROIC muy por encima del costo de capital: el negocio de Data Center genera retornos excepcionales sobre el capital operativo mientras dure el poder de fijación de precios de CUDA.",
    "G15": "13,4%: beta observado ~1,90 (Directo, muy por encima del beta de industria 'Semiconductor' de Damodaran, que promedia fabricantes mucho más diversificados y de menor crecimiento) x ERP de mercado maduro de EE.UU., calificación real Aa1/AA, deuda financiera neta negativa (posición de caja neta).",
}

SUPUESTOS_RECOMENDADOS = {
    "C6": 0.50, "D6": "Desaceleración deliberada frente al crecimiento reciente de Data Center (+117% i.a.) y frente a la mitad de la guía propia de la compañía para el próximo año fiscal (~70%).",
    "C7": 0.60, "D7": "En línea con el margen operativo GAAP LTM real (65,2%), sin asumir mayor expansión en el Año 1.",
    "C8": 0.14, "D8": "La demanda de cómputo de IA se mantiene fuerte, pero los ASICs propios de los hiperescaladores empiezan a restar crecimiento incremental.",
    "C9": 0.58, "D9": "Leve compresión desde el margen LTM real (65,2%) por presión de precio de los ASICs propios de los hiperescaladores y mezcla hacia productos de menor margen relativo.",
    "C10": 5, "D10": "Horizonte estándar de convergencia del modelo.",
    "C11": 3.0, "D11": "Diseño fabless de chips (TSMC fabrica): relativamente liviano en capital fijo propio por dólar de ingreso incremental.",
    "C12": 2.5, "D12": "Años 6-10: algo más de intensidad de capital por inversión creciente en capacidad de empaquetado, redes propias y acuerdos de suministro estratégicos.",
}

MULTIPLOS_EVALUACION = (
    "Evaluación NVDA: los 4 últimos cierres fiscales dieron múltiplos positivos en las 5 hojas (utilidad "
    "positiva y creciente desde hace varios años, sin el patrón de signo cambiante de una empresa en transición "
    "a la rentabilidad), así que el mecanismo nativo (mínimo positivo de 4 años) se aplicó sin ajuste manual. "
    "OJO con la lectura de estos múltiplos: el mínimo de los últimos 4 cierres fiscales cae en el cierre de "
    "enero-2024 (EV/EBITDA 4,46x, P/E 5,05x), un punto donde el mercado todavía no había re-valuado la acción al "
    "ritmo en que creció la utilidad ese año (EBITDA +6,0x interanual en FY2024, muy por delante de la suba del "
    "precio de mercado de ese momento). Los cierres siguientes (FY2025 y FY2026) muestran múltiplos mucho más "
    "altos (EV/EBITDA 41,9x y 34,2x; P/E 47,9x y 38,0x), así que el mínimo de 4,46x/5,05x es un caso atípico del "
    "rango, no la norma. Usar ese mínimo como múltiplo objetivo para los próximos 3 años produce un precio "
    "implícito por EV/EBITDA, P/E, EV/FCFF, P/FCFE y P/OCF sistemáticamente muy por debajo del DCF (ver "
    "'Resumen de Valoración': DCF Base US$237,60 vs. precio objetivo ponderado Base US$120,41, con el 60% del "
    "peso puesto en estos 5 múltiplos). Para NVDA, dado lo atípico de ese mínimo, el DCF es la lectura más "
    "confiable de las 6 metodologías; el precio objetivo ponderado debe leerse con ese sesgo a la baja en mente, "
    "no como un promedio neutral entre 6 métodos igualmente representativos."
)

VO, INP, COC, RES = "'Valuation output'", "'Input sheet'", "'Cost of capital worksheet'", "'Resumen de Valoración'"

TESIS_ROWS: list[list] = [
    ["NVDA (NVIDIA Corporation) — Tesis de Inversión: De la Historia a los Números"],
    [f'="Metodología Damodaran (NYU Stern) | Precio al día del análisis: US$"&TEXT({RES}!C25;"0.00")&" | WACC: "&TEXT({COC}!B14;"0.00%")'],
    [],
    ["1. LA HISTORIA"],
    ["Nvidia pasó de ser un fabricante de tarjetas gráficas para videojuegos a ser, de facto, el proveedor casi "
     "monopólico de la infraestructura de cómputo que entrena e infiere los modelos de inteligencia artificial "
     "generativa del mundo. Su ventaja no es solo de hardware: CUDA, su plataforma de software propietaria, lleva "
     "casi dos décadas siendo el estándar de facto de la industria, generando costos de cambio reales para "
     "cualquier cliente que considere migrar a un chip de la competencia o a un ASIC propio. La pregunta de la "
     "tesis es si esa ventaja de software puede sostener el poder de fijación de precios de Nvidia frente al "
     "avance de los ASICs propios de sus principales clientes (los mismos hiperescaladores que hoy concentran "
     "una porción muy alta de sus ingresos), antes de que la cesión de cuota en cargas de trabajo de inferencia "
     "erosione el crecimiento y el margen más rápido de lo que el crecimiento total del mercado de cómputo de IA "
     "puede compensar. El caso Base asume una desaceleración deliberada frente al ritmo actual y frente a la "
     "propia guía de la compañía; el Optimista asume que la demanda de cómputo de IA sigue superando a la oferta "
     "durante todo el horizonte de proyección, sin cesión material de cuota."],
    [],
    ["Caso alcista (Bull)", "Caso bajista (Bear)"],
    ["CUDA como foso de software de casi dos décadas: migrar a un competidor o a un ASIC propio implica "
     "reescribir y revalidar software, un costo de cambio real que sostiene el poder de fijación de precios de "
     "Nvidia incluso frente a chips técnicamente competitivos.",
     "Los mismos hiperescaladores que hoy concentran una porción muy alta de los ingresos de Data Center "
     "(Google, Amazon, Microsoft, Meta) están construyendo sus propios ASICs de IA (TPU, Trainium, Maia, MTIA) "
     "para reducir su dependencia de Nvidia."],
    ["La demanda de cómputo de IA sigue superando a la capacidad de fabricación disponible (la propia compañía "
     "describe su crecimiento reciente como 'limitado por la oferta', no por la demanda de clientes).",
     "Controles de exportación a China (H20 y episodios previos) ya le costaron a la compañía miles de millones "
     "de dólares en ingresos no reconocidos y cargos por inventario, con una política que sigue siendo "
     "cambiante."],
    ["Balance con posición de caja neta positiva y calificación crediticia real Aa1/AA, entre las más sólidas "
     "del mercado, con recompra de acciones sostenida como mecanismo de retorno de capital.",
     "Concentración de clientes: una proporción muy alta de los ingresos de Data Center proviene de un puñado "
     "de hiperescaladores; un recorte de capex de IA o una migración acelerada a ASICs propios de cualquiera de "
     "ellos tendría un impacto desproporcionado sobre los ingresos consolidados."],
    ["Diversificación creciente hacia Gaming, Professional Visualization y Automotive, con crecimiento de doble "
     "dígito en los segmentos más chicos, aunque de escala aún menor frente a Data Center.",
     "El crecimiento explosivo de los últimos 2-3 cierres fiscales distorsiona los múltiplos históricos de "
     "mercado (ver 'Supuestos de los Múltiplos'): una desaceleración incluso moderada frente al ritmo actual "
     "podría no estar completamente incorporada en el precio de mercado."],
    [],
    ["2. DE LA HISTORIA A LOS NÚMEROS — LOS TRES ESCENARIOS (fórmulas vivas del modelo)"],
    ["Supuesto", "Conservador", "Base", "Optimista", "Justificación y fuente (dato real)"],
    ["Crecimiento de ingresos — Año 1", f"={VO}!C55", f"={INP}!B27", f"={VO}!C106",
     "Base 50%: desaceleración deliberada frente al crecimiento reciente de Data Center (+117% i.a.) y frente a "
     "la mitad de la propia guía de la compañía para el próximo año fiscal (~70%, 'limitado por la oferta'). "
     "Conservador 30%: los ASICs propios de los hiperescaladores empiezan a restar cuota de forma material. "
     "Optimista 68%: la demanda de cómputo de IA sigue superando a la oferta, en línea con la guía de la propia "
     "compañía."],
    ["Crecimiento de ingresos — Años 2-5", f"={VO}!D55", f"={INP}!B29", f"={VO}!D106",
     "Base 14%: la demanda de cómputo de IA se mantiene fuerte, pero los ASICs propios de los hiperescaladores "
     "empiezan a restar crecimiento incremental de forma gradual."],
    ["Margen operativo — Año 1", f"={VO}!C57", f"={VO}!C6", f"={VO}!C108",
     "En línea con el margen operativo GAAP LTM real (65,2%, 'Valuation output'!B6), sin asumir mayor expansión "
     "en el Año 1."],
    ["Margen objetivo (convergencia)", f"={VO}!C45", f"={VO}!C46", f"={VO}!C47",
     "Base 58%: leve compresión desde el margen LTM real (65,2%) por presión de precio de los ASICs propios de "
     "los hiperescaladores y mezcla hacia productos de menor margen relativo. Conservador 50%: la competencia de "
     "ASICs erosiona el margen de forma más pronunciada. Optimista 65%: el apalancamiento operativo compensa "
     "cualquier presión de precio, sin cesión material de cuota."],
    ["Años de convergencia de margen", f"={INP}!B31", f"={INP}!B31", f"={INP}!B31",
     "5 años: horizonte estándar del modelo para una empresa madura y rentable."],
    ["Sales-to-Capital (años 1-5 / 6-10)", f"={INP}!B32", f"={INP}!B32", f"={INP}!B32",
     "3,0x (años 1-5): diseño fabless de chips (TSMC fabrica), relativamente liviano en capital fijo propio. "
     "2,5x (años 6-10): algo más de intensidad de capital por inversión creciente en capacidad de empaquetado, "
     "redes propias y acuerdos de suministro estratégicos."],
    ["Costo de capital (WACC)", f"={COC}!B14", f"={COC}!B14", f"={COC}!B14",
     "Beta observado ~1,90 (Direct Input; la canasta de industria 'Semiconductor' de Damodaran promedia "
     "fabricantes mucho más diversificados y de menor crecimiento, subestimando el riesgo idiosincrático "
     "específico de Nvidia) x ERP de mercado maduro de EE.UU. Costo de deuda con calificación real Aa1/AA (no el "
     "A1/A+ genérico de la plantilla), vencimiento promedio 10 años. Posición de caja neta positiva."],
    ["Referencia: margen base (B6)", f"={VO}!B6", f"={VO}!B6", f"={VO}!B6",
     "Margen operativo GAAP LTM real: US$197.579M sobre ingresos de US$302.970M (65,2%)."],
    [],
    ["3. RESULTADO DEL DCF POR ESCENARIO"],
    ["Escenario", "Valor DCF / acción", "Precio Objetivo Ponderado*", "DCF vs. precio del análisis", "Ponderado vs. precio del análisis"],
    ["Conservador", f"={VO}!B86", f"={RES}!C12", f"=B26/{RES}!$C$25-1", f"=C26/{RES}!$C$25-1"],
    ["Base", f"={VO}!B35", f"={RES}!D12", f"=B27/{RES}!$C$25-1", f"=C27/{RES}!$C$25-1"],
    ["Optimista", f"={VO}!B137", f"={RES}!E12", f"=B28/{RES}!$C$25-1", f"=C28/{RES}!$C$25-1"],
    ["Precio del análisis (GOOGLEFINANCE)", f"={RES}!C25"],
    [f'=IF(AND(B26<B27;B27<B28;C26<C27;C27<C28;{VO}!C55<{INP}!B27;{INP}!B27<{VO}!C106;{VO}!C45<{VO}!C46;{VO}!C46<{VO}!C47);"✔ Orden verificado: Conservador < Base < Optimista en crecimiento, margen objetivo, valor DCF y precio ponderado";"✖ REVISAR: el orden Conservador < Base < Optimista no se cumple")'],
    ["*El Precio Objetivo Ponderado combina el DCF (40%) con 5 múltiplos (EV/EBITDA 20%, P/E 20%, EV/FCFF 10%, "
     "P/FCFE 5%, P/OCF 5%) según la categoría 'Madura'. Los múltiplos históricos están distorsionados al alza "
     "por el crecimiento explosivo de los últimos 2-3 cierres fiscales (ver 'Supuestos de los Múltiplos'): "
     "leerlos como una referencia de un negocio de semiconductores genérico, no como una lectura ajustada por el "
     "crecimiento estructural específico de la demanda de cómputo de IA que sí captura el DCF."],
    [],
    ["4. CONCLUSIÓN"],
    [f'="A US$"&TEXT({RES}!C25;"0.00")&", Nvidia cotiza "&IF({VO}!B35>{RES}!C25;"por DEBAJO";"por ENCIMA")&" de su DCF Base (US$"&TEXT({VO}!B35;"0.00")&", "&TEXT({VO}!B35/{RES}!C25-1;"+0%;-0%")&") y "&IF({RES}!D12>{RES}!C25;"por DEBAJO";"por ENCIMA")&" del precio objetivo ponderado Base (US$"&TEXT({RES}!D12;"0.00")&"): el caso Base de este modelo asume una desaceleración deliberada frente al ritmo de crecimiento actual y frente a la propia guía de la compañía, sin ceder nada por competencia de ASICs propios de los hiperescaladores en el Año 1. La brecha entre este resultado y el precio de mercado refleja, en gran medida, cuánta confianza asigna el mercado a que Nvidia sostenga su ritmo de crecimiento actual (o el de la guía optimista de la propia empresa) durante varios años más, frente al riesgo de cesión de cuota que el escenario Conservador intenta capturar."'],
    ["Variable clave a monitorear: el crecimiento de Data Center trimestre a trimestre desglosado entre clientes "
     "hiperescaladores y el resto (para detectar cesión de cuota temprana hacia ASICs propios), y la evolución "
     "de la política de controles de exportación a China. El margen bruto/operativo reportado frente al guiado "
     "es el segundo indicador a monitorear de cerca."],
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
        {"range": "E4:E9", "format": mult}, {"range": "E13:E17", "format": mult}, {"range": "E12", "format": cur},
        {"range": "E20:E21", "format": num}, {"range": "E22:E23", "format": mult},
        {"range": "H4:H15", "format": pct}, {"range": "H18:H19", "format": pct}, {"range": "H20", "format": cur},
        {"range": "H21:H22", "format": pct},
    ])


def write_tesis(sh, backup_path) -> None:
    pct = {"numberFormat": {"type": "PERCENT", "pattern": "0.0%"}}
    ms.write_tesis(
        sh, TESIS_ROWS, backup_path, text_rows=(),
        merges=[f"A{r}:E{r}" for r in (1, 2, 5, 13, 24, 31, 33, 34, 35, 37)] + [f"B{r}:E{r}" for r in range(7, 12)],
        bold_rows=(4, 13, 24, 33), head_rows=(7, 14, 25),
        formats=[
            {"range": "B15:D18", "format": pct}, {"range": "B22:D22", "format": pct},
            {"range": "B19:D19", "format": {"numberFormat": {"type": "NUMBER", "pattern": "0"}}},
            {"range": "B20:D20", "format": {"numberFormat": {"type": "NUMBER", "pattern": "0.0\"x\""}}},
            {"range": "B21:D21", "format": {"numberFormat": {"type": "PERCENT", "pattern": "0.00%"}}},
            {"range": "B26:C28", "format": {"numberFormat": {"type": "CURRENCY", "pattern": "$0.00"}}},
            {"range": "B29", "format": {"numberFormat": {"type": "CURRENCY", "pattern": "$0.00"}}},
            {"range": "D26:E28", "format": {"numberFormat": {"type": "PERCENT", "pattern": "+0.0%;-0.0%"}}},
        ])
