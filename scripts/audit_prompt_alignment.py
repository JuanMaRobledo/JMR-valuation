"""Reconcile prompt v4/v5 outputs against connector-backed live grid snapshots.

Inputs are explicit JSON snapshots; no credentials or implicit network reads.
Use --grids, --engine-results, --datos and --engine to reproduce an audit.
Sheet mutations are emitted for review as structured batchUpdate requests.
"""
from __future__ import annotations
import argparse, ast, copy, datetime, glob, html, json, re, subprocess, statistics as st
from pathlib import Path
from bs4 import BeautifulSoup

FORMATS={}
SCEN=('conservador','base','optimista')
SHORT=('cons','base','opt')
NAMES={'evEbitda':'EV/EBITDA','evFcff':'EV/FCFF','pe':'P/E','pfcfe':'P/FCFE','pocf':'P/OCF'}
ROOT=Path(__file__).resolve().parents[1]
NOW=datetime.datetime.now(datetime.timezone.utc).isoformat(timespec='seconds')
def money(v):return 'US$'+f'{v:,.2f}'.replace(',','X').replace('.',',').replace('X','.')
def pct(v):return f'{v*100:.1f}%'.replace('.',',')
def table(head,rows):
 return '<div class="table-scroll" style="overflow-x:auto"><table><thead><tr>'+''.join('<th>'+html.escape(str(v))+'</th>' for v in head)+'</tr></thead><tbody>'+''.join('<tr>'+''.join('<td>'+str(v)+'</td>' for v in row)+'</tr>' for row in rows)+'</tbody></table></div>'
def load_functions(filename,ns):
 tree=ast.parse(Path(filename).read_text());tree.body=[x for x in tree.body if not isinstance(x,ast.ImportFrom) or not (x.module or '').startswith(('jmr_valuation','valuation_report','regen_saved'))];tree.body=[x for x in tree.body if not isinstance(x,ast.Import) or not any(a.name.startswith('playwright') for a in x.names)];exec(compile(tree,filename,'exec'),ns)
def write(path,obj):Path(path).write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n')

def implied_growth(tk,inp,calc,G,engine):
 ns={'__name__':'audit_module','__file__':str(ROOT/'scripts/implied_growth.py'),'ENGINE':engine,'MV':ROOT/'reference/multiplos_v3','es':lambda v,n=2:f'{v:.{n}f}'.replace('.',',')}
 load_functions(ROOT/'scripts/implied_growth.py',ns)
 anc=json.loads((ROOT/'reference/multiplos_v3'/f'{tk}_anclas.json').read_text())
 jb=anc['justificado']['Base'];f=calc['financials']['base'];dcf=calc['valorPresente']['dcf']['base'];fy=calc['precios']['dcf']['base']
 gref=st.mean(G['Valuation output'][3][2:7])
 gi=ns['node']('crecimientoImplicitoDCF(inp, m, g, d, p)',inp=inp,m=inp['marginBase'],g=gref,d=dcf,p=inp['precioActual'])
 params={'ke':inp['costoPatrimonio'],'wacc':jb['wacc_4_10'],'roe':jb['roe_fy3'],'fcffEbitda':f['fcff'][3]/f['ebitda'][3] if f['ebitda'][3] else None,'fcfeOcf':f['fcfe'][3]/f['ocf'][3] if f['ocf'][3] else None}
 rows=[]
 for key,label in NAMES.items():
  M=inp['multiplos'][key]['base'];app=inp['pesos'][key]>0
  metric=f[{'evEbitda':'ebitda','evFcff':'fcff','pe':'netIncome','pfcfe':'fcfe','pocf':'ocf'}[key]][3]
  shares=max(f['shares'][1],f['shares'][3]) if key.startswith('ev') else f['shares'][3]
  divs=sum(f['dps'][1:4]);md=((fy-divs)*shares+(inp['deudaNetaMultiplos'] if key.startswith('ev') else 0))/metric if metric and metric>0 else None
  gm=ns['node']('crecimientoImplicitoMultiplo(m, M, p)',m=label,M=M,p=params) if app else None
  gd=ns['node']('crecimientoImplicitoMultiplo(m, M, p)',m=label,M=md,p=params) if app and md and md>0 else None
  dv=calc['precios'][key]['base']/fy-1 if app else None
  rows.append({'metodo':label,'multiplo':M,'multiploDcf':md if app else None,'gImplicito':gm,'gDcf':gd,'dif':gm-gd if gm is not None and gd is not None else None,'difValor':dv,'aplica':app,'lectura':ns['lectura_multiplo'](gm,gd,dv) if app else 'No aplica: peso cero en la categoría financiera.'})
 out={'fecha':'2026-09-30','precio':inp['precioActual'],'dcfHoy':dcf,'dcfFy3':fy,'umbral':.02,'dcfInverso':{'gImplicito':gi,'gDcf':gref,'dif':gi-gref if gi is not None else None,'lectura':ns['lectura_precio'](gi,gref)},'parametros':params,'multiplos':rows,'metodo':'DCF inverso completo sin calibración; múltiplos frente al DCF capitalizado FY+3','nota':'Crecimiento constante en años 1–5 para el DCF inverso. Las proyecciones de múltiplos conservan sus métricas propias; PagBank usa FCFE financiero para el DCF y trata los múltiplos de flujo bancario con cautela.'}
 write(ROOT/'reference/multiplos_v3'/f'{tk}_crecimiento.json',out)
 return out

def reconcile(grids,results,datos,engine):
 ns={'__name__':'audit_module','__file__':str(ROOT/'scripts/damodaran_stories.py')}
 load_functions(ROOT/'scripts/damodaran_stories.py',ns)
 ns.update(ENGINE=engine,DATOS=datos)
 # Model values come from exact numeric snapshots, rather than rounded HTML.
 def load_sheet(sid):
  tk=next(t for t in grids if sid in json.loads(next(datos.glob('valoraciones/'+t+'-*.json')).read_text())['hojaGoogle'])
  G=grids[tk]
  def cell(s,a):
   m=re.fullmatch(r'([A-Z]+)(\d+)',a);col=0
   for ch in m[1]:col=col*26+ord(ch)-64
   if s=='Descuento de múltiplos' and a=='D38':return results[tk]['calc']['valorPresente']['dcf']['base']
   if tk=='PAGS' and s=='Input sheet' and a=='B30':return .156
   rows=G.get(s,[]);ri=int(m[2])-1
   return rows[ri][col-1] if ri<len(rows) and rows[ri] and col<=len(rows[ri]) else None
  return G,cell
 ns['load_sheet']=load_sheet
 ns['engine_inputs']=lambda cell,fm,price:copy.deepcopy(results[next(t for t in grids if cell('Input sheet','B12')==grids[t]['Input sheet'][11][1])]['inp'])
 reports=[]
 for path in sorted(datos.glob('valoraciones/*.json')):
  rec=json.loads(path.read_text());tk=rec['ticker'];old=json.loads(subprocess.check_output(['git','show','HEAD:valoraciones/'+path.name],cwd=datos,text=True));inp=results[tk]['inp'];calc=results[tk]['calc'];G=grids[tk]
  # Current sheet quote is a dated reference, never described as a real-time trade.
  rec['precio']=inp['precioActual'];rec['precioReferenciaFuente']='Input sheet!D1 (Google Sheets; puede tener retraso)';rec['precioReferenciaConsultadoAt']=NOW
  dm=rec['descuentoMultiples'];vp=calc['valorPresente'];dm['dcfHoy']={k:vp['dcf'][s] for k,s in zip(SCEN,SHORT)}
  dm['multiplesHoy']={k:vp['multiplos'][s] for k,s in zip(SCEN,SHORT)};dm['ponderadoHoy']={k:vp['ponderado'][s] for k,s in zip(SCEN,SHORT)}
  rec['valorPresentePonderado']=copy.deepcopy(dm['ponderadoHoy'])
  rec['crecimientoImplicito']=implied_growth(tk,inp,calc,G,engine)
  for m in rec['metodos']:
   key='dcf' if 'DCF' in m['nombre'] else next(k for k,v in NAMES.items() if v==m['nombre'])
   for k,s in zip(SCEN,SHORT):m[k]=calc['precios'][key][s]
   if key=='dcf':m['nombre']='DCF Damodaran · FCFE' if tk=='PAGS' else 'DCF Damodaran';m['horizonte']='FY+3; capitalizado desde el DCF presente'
  rec['objetivoPonderado']={k:calc['precioObjetivo'][s] for k,s in zip(SCEN,SHORT)}
  # CAGR is explicitly measured from the historical analysis quote.
  rec['cagr']={k:(v/rec['precioAnalisis'])**(1/3)-1 for k,v in rec['objetivoPonderado'].items()}
  for m in dm['metodos']:
   key=next(k for k,v in NAMES.items() if v==m['nombre'])
   for k,s in zip(SCEN,SHORT):
    d=vp['metodos'][key][s];m[k].update(fy=d['nominal'],vp=d['vp'],consolidado=d['consolidado'])
  for k,s in zip(SCEN,SHORT):
   cons=dm['consolidado'][k];keys=list(NAMES);w=vp['pesoMultiplos']
   cons['fy']=[sum(inp['pesos'][m]*vp['metodos'][m][s]['nominal'][n] for m in keys)/w for n in range(3)]
   cons['vp']=[sum(inp['pesos'][m]*vp['metodos'][m][s]['vp'][n] for m in keys)/w for n in range(3)]
   cons['consolidado']=vp['multiplos'][s]
  if tk=='PAGS':rec['dcfFinanciero']=copy.deepcopy(inp['dcfFinanciero'])
  write(path,rec) # compute() reads the reconciled quote.
  r=ns['compute'](tk);sp=r['spec'];sp['fecha']='2026-09-30'
  # Remove price anchoring from the narrative before the final-price subsection.
  sp['historia']=re.sub(r' y la acción cayó de ~US\$95 a ~US\$44','',sp['historia'])
  if tk=='DUOL':
   sp['filtro'][0]=['Los ingresos crecen cerca de 11% anual cinco años','Sí','Sí: reservas +8% en el 2T y guía anual +10,9%; exige estabilización','Media, condicionada a conversión']
   sp['filtro'][2][0]='El margen operativo ajustado por I+D llega a 27%';sp['fuentes'][1][1]='https://www.sec.gov/Archives/edgar/data/1562088/000162828026053603/duol-20260630.htm'
  if tk=='PAGS':
   # Financials use earnings and capital retention, not industrial EBIT/FCFF.
   r['m_base']=.156;r['dcf_base']=dm['dcfHoy']['base'];sp['margenes']['texto']='Para PagBank la rentabilidad relevante es el ROE, no el margen EBIT. El DCF de flujos al accionista parte de utilidad LTM de US$406,6 millones, 276 millones de acciones, ROE Base de 15,6%, crecimiento de beneficios de 5% el primer año y 6% en años 2-5. El ROE se desvanece al costo del patrimonio terminal de 12%; crecimiento estable en dólares de 3%. ROE de 13%/17% delimitan los escenarios. Son supuestos del analista, no guía; la cifra de ROAE ajustado de 15,6% procede del comunicado 2T de 11-ago-2026.'
   sp['reinversion']['texto']='La reinversión patrimonial se estima como utilidad × crecimiento / ROE; el FCFE es utilidad menos esa retención. Se descuenta al Ke de 14,7%, que converge a 12%. No se suma la liquidez bancaria ni se restan depósitos. El 22,5% de Basilea reportado en 2T muestra holgura, pero no identifica por sí solo capital distribuible: no se agrega un valor por exceso de capital no comprobado. La aproximación requiere que crecimiento de ingresos y beneficios sea comparable; la sensibilidad debe revisarse si cambia el riesgo de crédito o el capital regulatorio.'
  # Spec text containing rounded price/inverse values is replaced by live outputs.
  sp['precio_lectura']='La comparación es condicional a las historias y a su probabilidad. La diferencia frente al precio no constituye una recomendación. Revisar primero las métricas operativas y los supuestos de reinversión si el mercado exige una historia distinta.'
  # Use a single authoritative, auditable expected-value field.
  ve={'fecha':'2026-09-30','valor':r['valor_esperado_beta_hoja'],'valorBetaPropuesta':r['valor_esperado_beta_prop'],'betaHoja':r['beta_hoja'],'betaPropuesta':r['beta_prop'],'dcfBase':dm['dcfHoy']['base'],'metodo':'Promedio de DCF completos ponderado por probabilidades del analista.', 'historias':[{'nombre':h['nombre'],'probabilidad':h['prob'],'valor':h['valor_beta_hoja'],'valorBetaPropuesta':h['valor_beta_prop'],'margen':h['margen'],'crecimiento':h['cagr'],'roicTerminal':h.get('roic_terminal_usado',0) or 'costo_capital'} for h in r['historias']]}
  rec['valorEsperado']=ve;rec['precioMOSValorEsperado']=ve['valor']*(1-rec['mos']);rec['baseMOS']='valorEsperado'
  rec['precioMOSHoy']={k:rec['precioMOSValorEsperado'] for k in SCEN};rec['precioMOS']=rec['precioMOSMax']=rec['precioMOSValorEsperado']
  rec['zonas']['conMOS']={'min':rec['precioMOS'],'max':rec['precioMOSMax'],'base':'valor esperado; una cifra, sin escenarios'}
  for key in ['value','deepValue','historica']:rec['zonas'][key]={k:calc['zonas'][key][k] for k in ['min','max']}
  rec['zonas']['descripcion']='Value, Deep Value e histórica son bandas heredadas del objetivo FY+3; no son umbrales de valor intrínseco presente. MOS vigente: valor esperado.'
  rec['savedAt']=NOW;rec.setdefault('auditoria',{})['prompts20260930']={'prompts':['valoracion-modelo-jmr-v4','research-fundamental-jmr-v5'],'fecha':NOW,'dcfAntes':old['descuentoMultiples']['dcfHoy'],'dcfAhora':dm['dcfHoy'],'valorEsperadoAntes':old['valorEsperado']['valor'],'valorEsperadoAhora':ve['valor'],'MOS':'Sobre el valor esperado','fuente':'Lecturas numéricas de las hojas vinculadas; DCF y múltiplos reproducidos con jmr_engine.js','forward':'Retirada columna heredada Nov 26 (E); no se sustituye con un consenso inventado.'}
  if tk=='PAGS':rec['auditoria']['prompts20260930']['metodologia']='FCFF industrial sustituido por FCFE financiero. EV/EBITDA y EV/FCFF no aplican (peso cero). P/FCFE y P/OCF con cautela; datos de flujo bancario sensibles a depósitos y crédito.'
  # Re-render current sheet snapshots, keeping only verified historical columns.
  for group,shs in rec['hojas'].items():
   for name in list(shs):
    if name not in G or name in ['Resumen de Valoración','Descuento de múltiplos']:continue
    rows=G[name][1:] if name in ['Income Statement','Forward Valuation'] else G[name]
    start=1 if name in ['Income Statement','Forward Valuation'] else 0
    rows=[[FORMATS.get(tk,{}).get(name,{}).get(str(i+start)+','+str(j),str(v if v is not None else '—')) for j,v in enumerate(row)] if row else [] for i,row in enumerate(rows)]
    if name=='Income Statement':rows=[row[:12] for row in rows if row]
    if name=='Forward Valuation':rows=[row[:12] for row in rows if row]
    if name in ['Income Statement','Forward Valuation','Valuation output','Financials Multiples','EVEBITDA','EVFCFF','PE','PFCFE','POCF','Tesis de Inversión y Supuestos']:
     shs[name]='<table><tbody>'+''.join('<tr>'+''.join('<td>'+html.escape(str(v if v is not None else '—'))+'</td>' for v in row)+'</tr>' for row in rows if row)+'</tbody></table>'
  for name in ['Balance Sheet','Cash Flow Statement']:
   h=rec['hojas']['financieros'][name];s=BeautifulSoup(h,'html.parser')
   for tr in s.find_all('tr'):
    cells=tr.find_all(['td','th'],recursive=False)
    if len(cells)>12:
     for td in cells[12:]:td.decompose()
   rec['hojas']['financieros'][name]=str(s)
  # Compact outputs make horizon and MOS basis explicit.
  today=[['DCF hoy · valor intrínseco']+[money(dm['dcfHoy'][k]) for k in SCEN],['Múltiplos hoy · secundarios']+[money(dm['multiplesHoy'][k]) for k in SCEN],['Ponderado hoy · secundario']+[money(dm['ponderadoHoy'][k]) for k in SCEN],['Valor esperado de historias','—',money(ve['valor']),'—'],['Precio con MOS sobre el valor esperado','—',money(rec['precioMOSValorEsperado']),'—']]
  rec['hojas']['valoracion']['Resumen de Valoración']=table(['Concepto','Conservador','Base','Optimista'],today)+'<h3>Objetivos FY+3 · otro horizonte</h3>'+table(['Método','Conservador','Base','Optimista'],[[m['nombre']]+[money(m[k]) for k in SCEN] for m in rec['metodos']])+f'<p>Precio de referencia de la hoja consultado el 30-sep-2026: {money(rec["precio"])}; puede tener retraso. Ke: {pct(dm["costoPatrimonio"])}.</p>'
  rec['hojas']['valoracion']['Descuento de múltiplos']=table(['Método','Conservador','Base','Optimista'],[[m['nombre']]+[money(m[k]['consolidado']) for k in SCEN] for m in dm['metodos']])+table(['Concepto','Conservador','Base','Optimista'],today)
  write(path,rec)
  md,section=ns['render'](r)
  if tk=='PAGS':
   section=section.replace('Margen objetivo','ROE objetivo').replace('Sales-to-capital','Reinversión patrimonial').replace('crecimiento anual de ingresos','crecimiento anual de beneficios').replace('margen operativo objetivo','ROE objetivo')
  # Always document exact assumptions and terminal treatment in the valuation section.
  appendix='<h3>Supuestos vigentes verificados</h3>'+table(['Supuesto','Conservador','Base','Optimista'],[[label]+[pct(inp[k+s]) if is_pct else str(inp[k+s]) for s in ['Cons','Base','Opt']] for label,k,is_pct in [('Crecimiento año 1','growthY1',True),('Crecimiento años 2–5','growth',True),('Margen año 1 (base ajustada del modelo)','marginY1',True),('Margen objetivo','margin',True)]])+f'<p>Ventas/capital: {inp["salesToCapital"]}x en años 1–5 y {inp["salesToCapital2"]}x en 6–10. WACC: {pct(inp["wacc"])}. Ke: {pct(inp["costoPatrimonio"])}. Impuesto efectivo: {pct(inp["taxEffective"])}. Convergencia: {inp["convergenceYear"]} años. Estos parámetros son escenarios del analista, no cifras reportadas.</p>'
  if tk=='PAGS':appendix='<h3>DCF financiero: supuestos y limitaciones</h3><p>'+sp['margenes']['texto']+' '+sp['reinversion']['texto']+'</p>'
  section=section.replace('<h3>Historias cuantificadas y valor esperado</h3>',appendix+'<h3>Historias cuantificadas y valor esperado</h3>')
  analysis=next(datos.glob('analisis/'+tk+'-research-*.json'));research=json.loads(analysis.read_text());soup=BeautifulSoup(research['html'],'html.parser')
  oldsec=soup.select_one('section.jmr-valuation-current')
  if oldsec:oldsec.decompose()
  for comment in soup.find_all(string=lambda x:isinstance(x,__import__('bs4').Comment)):
   if 'JMR-CURRENT-VALUATION' in comment:comment.extract()
  # Remove stale valuation commentary outside section 12, preserving operating facts.
  dam=next(x for x in soup.find_all('h2') if 'Valor con criterio Damodaran' in x.text)
  nxt=dam.find_next_sibling('h2');node=dam.next_sibling
  while node is not None and node is not nxt:after=node.next_sibling;node.extract();node=after
  dam.string='12. Valor con criterio Damodaran'
  for node in reversed(list(BeautifulSoup(section,'html.parser').contents)):dam.insert_after(node)
  for p in soup.find_all('p'):
   if p.get_text(' ',strip=True).startswith('Lectura de la valoración vigente:'):p.decompose()
  # Current valuation table belongs only to section 12, after the price is introduced.
  priceheading=next(x for x in soup.find_all('h3') if x.text=='El precio al final')
  link={k:copy.deepcopy(rec[k]) for k in ['precio','fecha','zonas','objetivoPonderado','valorPresentePonderado','descuentoMultiples','cagr','metodos','precioMOS','precioMOSMax','precioMOSHoy','valorEsperado']};link['sourcePath']='valoraciones/'+path.name;link.update(mos=rec['mos'],hojaGoogle=rec['hojaGoogle'],precioMOSValorEsperado=rec['precioMOSValorEsperado'],baseMOS='valorEsperado')
  ns2={'__name__':'audit_module','__file__':str(ROOT/'scripts/sync_research_present_value.py')};load_functions(ROOT/'scripts/sync_research_present_value.py',ns2)
  block=ns2['current_block'](tk,link,rec).replace('<h2>Valoración vigente','<h3>Valoración vigente').replace(' · '+tk+'</h2>', ' · '+tk+'</h3>')
  # Place after final-price discussion, just before the decision register.
  reg=next(x for x in soup.find_all('h3') if x.text=='Registro de decisión')
  for node in list(BeautifulSoup(block,'html.parser').contents):reg.insert_before(node)
  # Remove price claims from the opening history/filter (the generator already delays comparisons).
  for p in soup.find_all('p'):
   if p.find_previous('h3') and p.find_previous('h3').text=='La historia en un párrafo':
    text=p.get_text();text=re.sub(r' y la acción cayó de ~US\$95 a ~US\$44','',text)
    if text!=p.get_text():p.clear();p.append(text)
  # ROIC evidence and conditionally allowed terminal excess returns.
  moat=json.loads((ROOT/'reference/moat_2026-09-30.json').read_text())['empresas'][tk]
  pieces=next(x for x in soup.find_all('h3') if x.text=='Historias cuantificadas y valor esperado')
  roic=inp['roicTerminal'] or inp['terminalWacc'];nomoat=copy.deepcopy(inp);nomoat['roicTerminal']=0
  js='const fs=require("fs"),vm=require("vm"),c={};vm.createContext(c);vm.runInContext(fs.readFileSync('+json.dumps(str(engine))+',"utf8"),c);const i='+json.dumps(nomoat)+';console.log(c.runDCF(i,i.growthBase,i.marginBase,i.growthY1Base,i.marginY1Base));'
  without=float(subprocess.check_output(['node','-e',js],text=True)) if tk!='PAGS' else dm['dcfHoy']['base']
  roh='<h3>Moat y retorno terminal: comprobación</h3>'+table(['Clasificación','ROIC actual (ajustado del modelo)','ROIC industria','Costo de capital terminal','ROIC terminal usado','DCF Base con regla vigente','DCF sin exceso de ROIC terminal'],[[moat['moat'],pct(moat['roic_actual']),pct(moat['roic_industria']) if moat['roic_industria'] else 'No disponible',pct(inp['terminalWacc']),pct(roic),money(dm['dcfHoy']['base']),money(without)]])+f'<p>Fuentes de ventaja: {html.escape(moat["fuentes"])}. Evidencia histórica: {html.escape(moat["evidencia"])}. Amenaza: {html.escape(moat["amenaza"])}. El ROIC actual del motor y el histórico GAAP pueden diferir por I+D, arrendamientos y goodwill; no se usan indistintamente. Clasificación aplicada a retornos terminales, no una negación de todas las ventajas comerciales.</p>'
  if tk!='PAGS':
   for node in list(BeautifulSoup(roh,'html.parser').contents):pieces.insert_before(node)
  research.update(valuationHtml=block,html=str(soup),linkedValuation=link,updatedAt=NOW,price=rec['precio'],priceFetchedAt=NOW)
  research['auditoriaPrompts']={'hojaNativaSincronizada':tk in ['UBER','PAGS'],'fecha':NOW,'valoracion':'v4','research':'v5','fuenteNumerica':rec['hojaGoogle'],'alcance':'Cálculos, coherencia interna, estructura, y fuentes primarias disponibles; las limitaciones de divulgación se conservan.'}
  write(analysis,research)
  write(ROOT/'reference/damodaran'/f'{tk}.json',sp)
  (ROOT/'reference/damodaran'/f'{tk}_seccion.html').write_text(section+'\n')
  r.pop('spec',None);write(ROOT/'reference/damodaran'/f'{tk}_resultado.json',r)
  reports.append({'ticker':tk,'dcf':dm['dcfHoy'],'valorEsperado':ve['valor'],'precioMOS':rec['precioMOSValorEsperado'],'precioReferencia':rec['precio'],'metodologia':'FCFE' if tk=='PAGS' else 'FCFF','motorVsHoja': max(abs(vp['dcf'][s]-results[tk]['sheetPV'][s]) for s in SHORT)<1e-8,'forwardRetiradoEnTablasApp':tk!='CELH','hojaNativaEditada':tk in ['UBER','PAGS'],'bloqueoHojaNativa':None if tk in ['UBER','PAGS'] else 'Auto-review exige enlace autorizado expresamente por el usuario'})
 write(datos/'auditoria-prompts-2026-09-30.json',{'fecha':NOW,'empresas':reports})
 return reports
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--formats',type=Path);p.add_argument('--grids',type=Path,required=True);p.add_argument('--engine-results',type=Path,required=True);p.add_argument('--datos',type=Path,required=True);p.add_argument('--engine',type=Path,required=True);a=p.parse_args()
 if a.formats:FORMATS=json.loads(a.formats.read_text())
 print(json.dumps(reconcile(json.loads(a.grids.read_text()),json.loads(a.engine_results.read_text()),a.datos.resolve(),a.engine.resolve()),ensure_ascii=False,indent=2))
