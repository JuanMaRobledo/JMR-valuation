"""Valoracion de Intuit Inc. (INTU) -- posicion IBKR sin valoracion previa en Modelo JMR.
Motor: scripts/posiciones_ibkr.py. Hoja: Drive > Análisis > INTU > Modelo JMR - INTU
(copia nueva de la plantilla maestra auditada)."""
from __future__ import annotations

SHEET_ID = "14sbZoheKmtK5UpMOlRNzvqD1F9sCJEpHW01g4f-X8mM"
TICKER = "INTU"
COMPANY = "Intuit Inc."
SHORT = "Intuit"
INDUSTRY = "Software (System & Application)"
PEERS = ['ADBE', 'CRM', 'ADP', 'WDAY']

CATEGORY = "Software"
EMPLOYEES = 18600  # 10-K FY2026: ~18.600 empleados al 31-jul-2026 (+~12.300 temporales de temporada de impuestos)
DIVIDEND = True

K10 = "https://www.sec.gov/Archives/edgar/data/896878/000089687826000037/intu-20260731.htm"
SOURCES = (
    "Fuentes: estados financieros del modelo (SEC EDGAR, XBRL, CIK 0000896878: 10-K del año fiscal 2026 cerrado "
    f"el 31-jul-2026, presentado el 09-sep-2026, {K10}); segmentos, empleados y plan de reestructuración 2026 del "
    "mismo 10-K; Damodaran Online (industria 'Software (System & Application)', ERP de mercado maduro); UST 10 años "
    "y precio de INTU vía yfinance (cierre del 25-sep-2026). Sin guía cuantitativa FY2027 verificada en esta hoja."
)

BASE = dict(g1=0.11, m1=0.28, g25=0.09, mt=0.32, conv=5, s2c1=2.5, s2c2=2.0, tax=0.23, wacc_term=0.09)
SCEN = dict(g1_cons=0.06, g1_opt=0.14, mt_cons=0.28, mt_opt=0.36)
COC = {
    # Beta observado ~1,2 (Direct Input): la canasta global 'Software (System & Application)'
    # (1,33 desapalancada) mezcla empresas de un solo producto y mas volatiles.
    "B22": "Direct Input", "B23": 1.20,
    "B26": "Country of Incorporation",
    # Calificacion real A3/A- (Moody's/S&P); vencimiento promedio de los bonos ~7 años.
    "B33": 7, "B34": "Actual rating", "B36": "A3/A-",
}

CUALI = dict(
    ceo="Sasan K. Goodarzi — Presidente y CEO desde enero de 2019.",
    sector="Software de gestión financiera para consumidores, pymes y contadores (Damodaran: Software (System & Application))",
    web="https://www.intuit.com  |  IR: https://investors.intuit.com",
    overview=("Intuit es una plataforma de tecnología financiera que atiende a ~93 millones de consumidores, pequeñas "
              "y medianas empresas y contadores con TurboTax, Credit Karma, QuickBooks, Mailchimp, Intuit Enterprise "
              "Suite e Intuit Accountant Suite. En el año fiscal 2026 (cerrado el 31-jul-2026) facturó US$21.448M "
              "(+14%), con un margen operativo GAAP de 27,4% y un flujo de caja libre de US$8.663M (10-K FY2026)."),
    segments=[
        ("Global Business Solutions (QuickBooks, Mailchimp)",
         "US$12.864M de ingresos FY2026 (+16%), 60% del total. El Online Ecosystem creció 19% (QuickBooks Online "
         "Accounting +23% por precio, clientes y mezcla; servicios de pagos, nómina y dinero +16%). Desde el 1-ago-2026 "
         "Mailchimp se reporta como segmento separado."),
        ("Consumer: TurboTax",
         "US$5.296M (+7%): preparación de impuestos en EE.UU. y Canadá, hazlo-tú-mismo y asistida por expertos, más "
         "productos de dinero (adelanto de reembolso). Creció por el segmento asistido pese a menos declaraciones "
         "federales (unidades) que el año anterior."),
        ("Consumer: Credit Karma",
         "US$2.641M (+20%): plataforma de finanzas personales que cobra por acción/clic a bancos y aseguradoras "
         "(préstamos personales, tarjetas, seguros). Es el negocio más cíclico del grupo: depende del apetito de "
         "crédito de sus socios financieros."),
        ("Consumer: ProTax y márgenes por segmento",
         "ProTax (software para contadores: Lacerte, ProSeries, ProConnect) US$647M (+4%). Margen de segmento "
         "(antes de corporativo y compensación en acciones): 77% en Global Business Solutions y 73% en Consumer."),
    ],
    bulls=[
        ("Datos y costos de cambio en el flujo financiero de la pyme",
         "QuickBooks concentra la contabilidad, la nómina y los pagos de millones de pequeñas empresas y sus "
         "contadores; migrar implica rehacer años de historia contable y procesos. Eso sostiene aumentos de precio "
         "efectivos (QuickBooks Online Accounting +23% en FY2026) con baja pérdida de clientes."),
        ("Motor de caja y retorno al accionista",
         "Flujo de caja libre de US$8.663M en FY2026 (40% de los ingresos) y recompras de US$5.412M más US$1.347M "
         "de dividendos; el Directorio sumó US$8.000M de autorización de recompra en mayo de 2026."),
        ("Monetización de IA sobre una base de datos propia",
         "La compañía integra agentes de IA en QuickBooks, TurboTax y Credit Karma sobre datos financieros propios "
         "de sus usuarios; si esa capa eleva el ingreso promedio por cliente (pagos, nómina, mid-market con Intuit "
         "Enterprise Suite), el crecimiento de doble dígito puede sostenerse varios años."),
    ],
    bears=[
        ("Desintermediación por IA generativa",
         "El mercado re-valuó con fuerza al software en 2026 (la acción pasó de ~US$785 al cierre fiscal 2025 a "
         "~US$276): el temor es que asistentes de IA de propósito general abaraten la preparación de impuestos y la "
         "contabilidad básica y erosionen el poder de precio de TurboTax y QuickBooks."),
        ("Ciclicidad de Credit Karma y regulación del crédito",
         "Credit Karma depende de la originación de préstamos y tarjetas de terceros; una recesión o un endurecimiento "
         "del crédito lo afecta directamente (en FY2023 cayó 11%). Además, programas públicos de declaración gratuita "
         "(IRS Direct File) y la regulación de datos de consumidores son riesgos recurrentes."),
        ("Compensación en acciones y adquisiciones costosas",
         "La compensación en acciones fue US$2.056M (9,6% de los ingresos) y el balance carga US$18.623M de goodwill e "
         "intangibles (Credit Karma, Mailchimp). El retorno sobre el capital invertido total es mucho menor que el de "
         "los segmentos orgánicos."),
    ],
)

STORY = dict(
    title="Intuit: el sistema operativo financiero de la pyme y del contribuyente, re-valuado por el temor a la IA",
    text=("Intuit creció 14% en FY2026 (US$21.448M) con un margen operativo GAAP de 27,4% y un flujo de caja libre de "
          "US$8.663M, mientras la acción caía a ~US$276 (P/E LTM ~17x, frente a 57x al cierre de FY2025). El caso Base "
          "asume que la desaceleración es gradual (11% el Año 1, 9% en los años 2-5, por debajo del 14% reciente y del "
          "15-16% de GBS) y que el margen GAAP sube a 32% a medida que se diluye la compensación en acciones y maduran "
          "los ahorros del plan de reestructuración 2026. La historia no depende de expansión múltiple sino de que la "
          "IA sea una herramienta de monetización para Intuit y no un sustituto de sus productos."),
    g="Año 1 11% (FY2026 +14%; GBS +16%, Consumer +11%), años 2-5 9%: desaceleración gradual por la base más grande y la competencia de IA.",
    m="Margen GAAP Año 1 28% (FY2026 27,4% con US$293M de cargos de reestructuración); objetivo 32% por menor peso de la compensación en acciones.",
    tax="Tasa marginal 23%: federal 21% + estatal neta; la efectiva FY2026 fue 24,1%.",
    s2c="2,5x: software, poco capital operativo por dólar incremental (el capital invertido contable está inflado por el goodwill de adquisiciones).",
    roic="ROIC operativo muy alto en los segmentos orgánicos; el ROIC sobre capital total incluye ~US$18.600M de goodwill/intangibles.",
    wacc="Beta observado 1,2 (Direct Input) x ERP de mercado maduro; deuda con calificación real A3/A-; deuda neta ~US$1.100M.",
)

RECO = dict(
    g1="FY2026 +14%; se asume desaceleración a 11% por base más grande y competencia de asistentes de IA.",
    m1="Margen operativo GAAP FY2026 27,4% (incluye US$293M de reestructuración no recurrente).",
    g25="Converge desde el 11% del Año 1 hacia un dígito alto: GBS sigue creciendo por precio/mezcla; TurboTax madura.",
    mt="32% GAAP: el margen de segmentos (77% GBS, 73% Consumer) deja espacio si la compensación en acciones y el gasto corporativo crecen menos que los ingresos.",
    s2c1="2,5x: negocio de software, bajo capex (US$175M en FY2026) y capital de trabajo negativo.",
    s2c2="2,0x: algo más de inversión en infraestructura de IA y adquisiciones selectivas.",
)

MULTIPLOS_EVALUACION = (
    "Evaluación INTU: el ancla nativa (mínimo positivo de los últimos 4 cierres fiscales) cae en el cierre de FY2026 "
    "(jul-2026), después del derrumbe de la acción: P/E ~19x, EV/EBITDA ~13x y P/FCF ~10x, contra 57x/40x/36x un año "
    "antes. Es el múltiplo más bajo de toda la historia disponible (10 años), así que los 5 métodos de múltiplos "
    "suponen que la re-valuación de 2026 es permanente. Es una lectura conservadora pero coherente con el cambio de "
    "percepción del mercado sobre el software frente a la IA; no se ajustó a mano."
)

TESIS = dict(
    historia=("Intuit construyó dos franquicias con datos propios y costos de cambio altos: QuickBooks, donde vive la "
              "contabilidad, la nómina y los pagos de millones de pymes y sus contadores, y TurboTax/Credit Karma, que "
              "conoce la situación fiscal y crediticia de decenas de millones de consumidores estadounidenses. En FY2026 "
              "facturó US$21.448M (+14%), con Global Business Solutions creciendo 16% y un flujo de caja libre de "
              "US$8.663M que financió US$5.412M de recompras. Aun así, la acción cayó de ~US$785 (jul-2025) a ~US$276 "
              "(25-sep-2026), porque el mercado pasó a descontar que la IA generativa abaratará la preparación de "
              "impuestos y la contabilidad básica. La tesis Base asume que Intuit usa la IA como palanca de "
              "monetización (más servicios asistidos, pagos, mid-market) y que el crecimiento baja gradualmente a un "
              "dígito alto, sin colapso de precios; el Conservador asume que la IA sí comprime el crecimiento a 6% y "
              "el margen se queda en el nivel actual."),
    bull_bear=[
        ("Costos de cambio: la contabilidad y nómina de una pyme no se migran fácilmente; QuickBooks Online Accounting creció 23% con precio.",
         "La IA generativa puede convertir la preparación de impuestos simple en un commodity y presionar el precio de TurboTax."),
        ("Flujo de caja libre de 40% de los ingresos; recompras de US$5.412M y dividendos crecientes.",
         "Credit Karma (US$2.641M) es cíclico y depende del apetito de crédito de bancos y fintech."),
        ("Mid-market (Intuit Enterprise Suite) y servicios de dinero amplían el mercado direccionable dentro de la base actual.",
         "Compensación en acciones de 9,6% de los ingresos y US$18.600M de goodwill e intangibles de adquisiciones."),
        ("Valuación ya re-ajustada: P/E ~17x LTM, el más bajo de 10 años.",
         "La declaración gratuita del IRS y la regulación de datos de consumo son riesgos regulatorios recurrentes."),
    ],
    j_g1=("Base 11%: por debajo del +14% de FY2026 (10-K) por base más grande; Conservador 6% (la IA comprime precio y "
          "unidades de TurboTax); Optimista 14% (se sostiene el ritmo actual con GBS +16%)."),
    j_g25="Base 9%: desaceleración gradual hacia un dígito alto; GBS sigue creciendo por precio, pagos y nómina.",
    j_m1="Margen GAAP FY2026 27,4% con US$293M de reestructuración (no recurrente); Año 1 28%.",
    j_mt=("Base 32%: los segmentos operan con 77% (GBS) y 73% (Consumer) de margen antes de corporativo y compensación en "
          "acciones; se asume dilución gradual de esos costos. Conservador 28% (sin expansión); Optimista 36%."),
    j_s2c="2,5x (años 1-5) / 2,0x (6-10): software con capex de US$175M/año y capital de trabajo negativo.",
    j_wacc="Beta observado 1,2 (Direct Input), ERP de mercado maduro de EE.UU., deuda A3/A- a 7 años; deuda financiera US$7.669M + arrendamientos, caja US$7.200M.",
    j_mbase="Margen operativo GAAP LTM (FY2026): US$5.884M / US$21.448M.",
    nota_multiplos=("El ancla de los múltiplos (mínimo de 4 cierres) es el cierre de FY2026, ya después de la "
                    "re-valuación del software: P/E ~19x, el más bajo de 10 años."),
    conclusion=("El modelo pone el valor en función de si Intuit sostiene un crecimiento de 9-11% con márgenes crecientes; "
                "el precio actual descuenta un escenario cercano al Conservador (IA como amenaza, no como palanca)."),
    monitor=("Variables a monitorear: crecimiento del Online Ecosystem y de QuickBooks Online (precio vs. clientes), "
             "unidades de TurboTax en la temporada de impuestos 2027, ingresos de Credit Karma frente al ciclo de "
             "crédito y evolución de la compensación en acciones como % de ingresos."),
)
