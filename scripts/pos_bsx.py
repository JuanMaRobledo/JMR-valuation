"""Valoracion de Boston Scientific Corporation (BSX) -- posicion IBKR sin valoracion previa en Modelo JMR.
Motor: scripts/posiciones_ibkr.py. Hoja: Drive > Análisis > BSX > Modelo JMR - BSX
(copia nueva de la plantilla maestra auditada)."""
from __future__ import annotations

SHEET_ID = "1LVn63SMyvovWzNjbF5Jdi-v0EFUPXLqp4A6n8gwbKHc"
TICKER = "BSX"
COMPANY = "Boston Scientific Corporation"
SHORT = "Boston Scientific"
INDUSTRY = "Healthcare Products"
PEERS = ['MDT', 'SYK', 'ABT', 'EW']

CATEGORY = "Crecimiento"
EMPLOYEES = 59000  # 10-K 2025: ~59.000 empleados
DIVIDEND = False
MULT_ANCHOR = "LTM"  # la accion cayo ~54% en 2026: los cierres 2022-2025 (P/E 49-96x) ya no representan el multiplo pagado

K10 = "https://www.sec.gov/Archives/edgar/data/885725/000088572526000010/bsx-20251231.htm"
Q2 = "https://www.sec.gov/Archives/edgar/data/885725/000088572526000053/bsx-20260630.htm"
SOURCES = (
    "Fuentes: estados financieros del modelo (SEC EDGAR, XBRL, CIK 0000885725: 10-K 2025 presentado el 17-feb-2026, "
    f"{K10}; 10-Q del 2T 2026 presentado el 03-ago-2026, {Q2}); ventas por unidad de negocio, recompra acelerada "
    "(ASR) de US$2.000M, acuerdo por Penumbra y demanda colectiva del mismo 10-Q; Damodaran Online (industria "
    "'Healthcare Products'); UST 10 años y precio de BSX vía yfinance (cierre del 25-sep-2026)."
)

BASE = dict(g1=0.07, m1=0.20, g25=0.07, mt=0.24, conv=5, s2c1=1.3, s2c2=1.2, tax=0.19, wacc_term=0.09)
SCEN = dict(g1_cons=0.04, g1_opt=0.10, mt_cons=0.20, mt_opt=0.27)
COC = {
    # Beta observado ~1,0 tras la caida de 2026 (antes ~0,8); la canasta global
    # 'Healthcare Products' da 1,12 desapalancada.
    "B22": "Direct Input", "B23": 1.00,
    "B26": "Country of Incorporation",
    "B33": 8, "B34": "Actual rating", "B36": "A3/A-",
}

CUALI = dict(
    ceo="Michael F. Mahoney — Presidente y CEO desde 2012; Presidente del Directorio desde 2016.",
    sector="Dispositivos médicos intervencionistas (Damodaran: Healthcare Products)",
    web="https://www.bostonscientific.com  |  IR: https://investors.bostonscientific.com",
    overview=("Boston Scientific desarrolla y vende dispositivos médicos mínimamente invasivos en dos segmentos: "
              "Cardiovascular (68% de las ventas del 1S 2026) y MedSurg. Facturó US$20.074M en 2025 (+19,9%, con "
              "adquisiciones) y US$10.646M en el 1S 2026 (+9,5%; crecimiento orgánico de 7,0% en el 2T). La acción "
              "cayó de ~US$95 a ~US$44 en 2026 por la desaceleración de Electrofisiología y Watchman frente a la "
              "competencia (10-Q 2T 2026)."),
    segments=[
        ("Cardiovascular: Electrofisiología (FARAPULSE)",
         "US$1.821M en el 1S 2026 (+16%), pero en el 2T solo +3% en EE.UU. (US$606M vs US$587M): la ablación por campo "
         "pulsado, que Boston Scientific lideró, ahora tiene competencia directa de Medtronic y Johnson & Johnson."),
        ("Cardiovascular: Watchman, ICVT y CRM",
         "Watchman (cierre de orejuela izquierda) US$1.014M en el 1S (+11%, pero +3% en EE.UU. en el 2T por "
         "desaceleración de ciertos procedimientos); Cardiología Intervencionista y Terapias Vasculares US$2.577M "
         "(+12%); Ritmo Cardíaco US$1.163M (plano)."),
        ("MedSurg: Endoscopía, Urología y Neuromodulación",
         "US$3.519M en el 1S 2026 (+7%): Endoscopía US$1.529M, Urología US$1.330M (incluye Axonics, comprada en "
         "nov-2024) y Neuromodulación US$659M (+15%, incluye Nalu Medical desde ene-2026)."),
        ("Adquisiciones en curso",
         "Acuerdo del 15-ene-2026 para comprar Penumbra (trombectomía) por ~US$14.500M (US$374/acción); la FTC pidió "
         "información adicional (Second Request) el 16-mar-2026. Esta hoja valora el negocio sin Penumbra."),
    ],
    bulls=[
        ("Cartera diversificada en categorías de crecimiento estructural",
         "Electrofisiología, Watchman, trombectomía (Penumbra) y neuromodulación son mercados de crecimiento de doble "
         "dígito por envejecimiento poblacional y sustitución de cirugía abierta por procedimientos mínimamente "
         "invasivos."),
        ("Escala comercial y de I+D",
         "I+D de US$2.052M en 2025 (10% de las ventas) y una fuerza de ventas global que permite lanzar y adquirir "
         "tecnologías (Bolt, SoniVie, Cortex, Nalu) y escalarlas rápido."),
        ("Valuación re-ajustada y recompras",
         "Tras la caída, la acción cotiza a ~18x utilidad GAAP LTM (vs. 49-96x en los cierres 2022-2025) y la empresa "
         "recompró US$2.000M con una ASR en mayo de 2026 (~40 millones de acciones)."),
    ],
    bears=[
        ("Pérdida de liderazgo en campo pulsado (PFA)",
         "El motor de crecimiento de 2024-2025 (FARAPULSE) enfrenta competidores con productos equivalentes; el "
         "crecimiento de EE.UU. en Electrofisiología cayó a un dígito bajo en el 2T 2026."),
        ("Integración y precio de Penumbra",
         "US$14.500M por un negocio de trombectomía con competencia creciente y revisión antimonopolio de la FTC; "
         "sumará deuda e intangibles a un balance con US$18.640M de goodwill."),
        ("Credibilidad de la guía",
         "Demanda colectiva de accionistas por la caída del 4-feb-2026 tras los resultados del 4T 2025, que alega "
         "declaraciones engañosas sobre la guía de Electrofisiología en EE.UU."),
    ],
)

STORY = dict(
    title="Boston Scientific: de ganador de la ablación por campo pulsado a crecedor de un dígito alto con una compra grande pendiente",
    text=("Boston Scientific creció 20% en 2025 impulsada por FARAPULSE y Watchman, y el mercado le pagaba 49-96x "
          "utilidad. En 2026 la competencia en campo pulsado y la desaceleración de Watchman bajaron el crecimiento "
          "orgánico a 7% en el 2T y la acción cayó a ~US$44 (P/E LTM ~18x). El caso Base asume que el crecimiento se "
          "estabiliza en 7% (cartera diversificada, sin Penumbra) y que el margen operativo GAAP (19,8% LTM, cargado "
          "de amortización de intangibles y gastos de adquisiciones) sube a 24%."),
    g="Año 1 y años 2-5 7%: crecimiento orgánico del 2T 2026 (7,0%), sin contar Penumbra.",
    m="Margen GAAP Año 1 20% (LTM 19,8%); objetivo 24% al diluirse amortización de intangibles y gastos de integración.",
    tax="Tasa marginal 19%: la efectiva histórica es baja (14,6% en 2025) por beneficios de compensación en acciones y mezcla internacional.",
    s2c="1,3x / 1,2x: dispositivos médicos con fábricas propias y crecimiento parcialmente por adquisiciones.",
    roic="ROIC GAAP moderado (goodwill de US$18.640M); el ROIC orgánico es mucho mayor.",
    wacc="Beta 1,0 (Direct Input), ERP de mercado maduro, deuda A3/A- a 8 años.",
)

RECO = dict(
    g1="Crecimiento orgánico del 2T 2026: 7,0% (10-Q); 1S 2026 reportado +9,5%.",
    m1="Margen operativo GAAP LTM 19,8% (US$4.152M / US$20.996M).",
    g25="7%: mercados de procedimientos en crecimiento de un dígito alto, con competencia más intensa en Electrofisiología.",
    mt="24% GAAP: margen ajustado de la compañía ~28%; la diferencia es amortización de intangibles y cargos de adquisiciones.",
    s2c1="1,3x: inversión en fábricas, inventarios y cuentas por cobrar hospitalarias.",
    s2c2="1,2x: supone que parte del crecimiento siga viniendo de adquisiciones.",
)

MULTIPLOS_EVALUACION = (
    "Evaluación BSX: los últimos cierres fiscales (dic-2022 a dic-2025) dan P/E de 49-96x y EV/EBITDA de 26-37x, "
    "múltiplos de una empresa que crecía 12-20% por año. Tras la caída de 2026 la acción cotiza a ~18x P/E y ~13x "
    "EV/EBITDA LTM. Se activó el override manual (columna J del bloque Base de las 5 hojas) = múltiplo LTM vivo "
    "('Trailing Valuation' columna L): asume que el mercado NO vuelve a pagar los múltiplos de 2022-2025. Conservador "
    "y Optimista siguen siendo x0,9 y x1,1 del Base."
)

TESIS = dict(
    historia=("Boston Scientific fue en 2024-2025 una de las grandes historias de crecimiento de la tecnología médica: "
              "la ablación por campo pulsado (FARAPULSE) y el cierre de orejuela (Watchman) llevaron las ventas de "
              "US$14.240M (2023) a US$20.074M (2025). En 2026 esa historia se rompió parcialmente: competidores con "
              "catéteres de campo pulsado equivalentes y la desaceleración de ciertos procedimientos de Watchman bajaron "
              "el crecimiento orgánico a 7% en el 2T, y la acción perdió más de la mitad de su valor. Al mismo tiempo la "
              "empresa comprometió ~US$14.500M en Penumbra y US$2.000M en recompras. La tesis Base valora el negocio "
              "actual (sin Penumbra) como un crecedor de un dígito alto con margen GAAP en expansión; el Conservador "
              "asume que la erosión de Electrofisiología se extiende (4% de crecimiento, margen estancado)."),
    bull_bear=[
        ("Cartera amplia en categorías de crecimiento estructural (EP, Watchman, trombectomía, neuromodulación).",
         "Competencia directa en campo pulsado: EE.UU. en Electrofisiología creció solo 3% en el 2T 2026."),
        ("I+D de 10% de las ventas y capacidad probada de adquirir y escalar tecnologías.",
         "Penumbra (~US$14.500M) añade riesgo de integración, deuda y revisión antimonopolio (FTC)."),
        ("P/E LTM ~18x, el más bajo de la historia reciente, y recompra acelerada de US$2.000M.",
         "Demanda colectiva por la guía de Electrofisiología; pérdida de credibilidad de la gerencia."),
        ("Margen ajustado ~28% con espacio para que el GAAP converja al diluirse la amortización.",
         "Goodwill de US$18.640M: el retorno sobre el capital total invertido es bajo."),
    ],
    j_g1="Base 7% (orgánico 2T 2026: 7,0%); Conservador 4% (erosión de EP y Watchman se extiende); Optimista 10% (nuevas indicaciones de Watchman y EP estabilizada).",
    j_g25="Base 7%: mercados de procedimientos en crecimiento de un dígito alto, sin Penumbra.",
    j_m1="Margen GAAP LTM 19,8% (US$4.152M / US$20.996M).",
    j_mt="Base 24% (ajustado ~28% menos amortización); Conservador 20% (sin expansión); Optimista 27%.",
    j_s2c="1,3x (1-5) / 1,2x (6-10): fábricas, inventario y crecimiento parcialmente por compras.",
    j_wacc="Beta 1,0 (Direct Input), ERP maduro de EE.UU., deuda A3/A- a 8 años; deuda US$11.436M + arrendamientos.",
    j_mbase="Margen operativo GAAP LTM (jul-2025 a jun-2026).",
    nota_multiplos=("Múltiplos anclados al LTM (override manual) porque los cierres 2022-2025 reflejan un crecimiento "
                    "que ya no existe; ver 'Supuestos de los Múltiplos'."),
    conclusion=("El precio actual descuenta un crecimiento de un dígito medio sin recuperación de márgenes; la "
                "valoración es muy sensible a que Electrofisiología se estabilice."),
    monitor=("Variables a monitorear: crecimiento de Electrofisiología y Watchman en EE.UU. trimestre a trimestre, "
             "decisión de la FTC sobre Penumbra y financiamiento de la compra, margen operativo ajustado vs. GAAP y "
             "evolución de la demanda colectiva."),
)
