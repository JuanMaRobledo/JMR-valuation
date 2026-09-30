"""Cuantifica las cuatro historias de CELH (data/CELH_Analisis_Damodaran_2026-09-30.md) con jmr_engine.js
calibrado contra el DCF Base de la hoja; no modifica la hoja. Uso: python reference/analisis_narrativa/celh_historias.py"""
import json, sys, subprocess, statistics as st
sys.path.insert(0,'scripts')
from multiples_anchors import get_gspread_client
from valuation_report_v3 import engine_inputs, ENGINE
c=get_gspread_client()
sh=c.open_by_key(json.load(open('reference/multiplos_v3/CELH_anclas.json'))['sheet_id'])
rng=["'Input sheet'!A1:D70","'Valuation output'!A1:M140","'Financials Multiples'!A1:H120","'Resumen de Valoración'!A1:U20"]
vr=sh.values_batch_get(rng,params={"valueRenderOption":"UNFORMATTED_VALUE"})['valueRanges']
grid={r.split('!')[0].strip("'"):v.get('values',[]) for r,v in zip(rng,vr)}
def cell(s,a):
    col,row=ord(a[0])-65,int(a[1:])-1; g=grid[s]
    return g[row][col] if row<len(g) and col<len(g[row]) else None
inp=engine_inputs(cell,grid['Financials Multiples'],27.71)
DCF=18.112
def run(cases):
    if len(cases)>40:
        out=[]
        for k in range(0,len(cases),40): out+=run(cases[k:k+40])
        return out
    js=("const fs=require('fs'),vm=require('vm');const c={};vm.createContext(c);"
        f"vm.runInContext(fs.readFileSync({json.dumps(str(ENGINE))},'utf8'),c);c.cases={json.dumps(cases)};"
        "console.log(JSON.stringify(vm.runInContext('cases.map(function(k){return runDCF(k.inp,k.g,k.m);})',c)));")
    return json.loads(subprocess.check_output(['node','-e',js]))
E,D,KD=0.9168,0.0832,0.0519
def wacc(beta): return E*(0.0499+beta*0.0446)+D*KD
base=dict(inp); base['wacc']=0.1114
ref=run([{'inp':base,'g':0.062,'m':0.17}])[0]
brands={'Celsius':1425.5,'Alani':1433.1,'Rockstar':188.7}
stories={
 'A · Alani lidera y Celsius se estabiliza':{'p':0.40,'Celsius':[0,.02,.03,.03,.03],'Alani':[.25,.18,.14,.10,.08],'Rockstar':[-.05]*5,'m':0.19,'s2c':2.5},
 'B · Alani crece, Celsius sigue cediendo':{'p':0.35,'Celsius':[-.06,-.04,-.02,0,0],'Alani':[.18,.12,.09,.07,.06],'Rockstar':[-.08]*5,'m':0.16,'s2c':2.5},
 'C · La moda se desgasta':{'p':0.15,'Celsius':[-.10,-.08,-.05,-.03,-.02],'Alani':[.08,.03,0,0,0],'Rockstar':[-.10]*5,'m':0.12,'s2c':2.5},
 'D · Plataforma multimarca':{'p':0.10,'Celsius':[.03,.05,.05,.04,.04],'Alani':[.35,.25,.18,.12,.10],'Rockstar':[-.03]*5,'m':0.22,'s2c':1.5},
}
out={}
for name,s in stories.items():
    rev={b:[v] for b,v in brands.items()}
    for y in range(5):
        for b in brands: rev[b].append(rev[b][-1]*(1+s[b][y]))
    tot0=sum(brands.values()); tot5=sum(rev[b][5] for b in brands)
    cagr=(tot5/tot0)**(1/5)-1
    mix5={b:rev[b][5]/tot5 for b in brands}
    cases=[]
    for beta in (1.5,1.0):
        i=dict(inp); i['wacc']=wacc(beta); i['salesToCapital']=s['s2c']
        cases.append({'inp':i,'g':cagr,'m':s['m']})
    vals=[DCF*v/ref for v in run(cases)]
    out[name]={'p':s['p'],'cagr':cagr,'rev5':tot5,'mix5':mix5,'m':s['m'],'s2c':s['s2c'],'v15':vals[0],'v10':vals[1],'yr':{b:s[b] for b in brands}}
    print(f"{name:45s} p={s['p']:.2f} CAGR5={cagr*100:5.1f}% ingresos5={tot5:7.0f} Alani%={mix5['Alani']*100:4.1f} margen={s['m']*100:.0f}% s2c={s['s2c']} valor(b1.5)={vals[0]:6.2f} valor(b1.0)={vals[1]:6.2f}")
ev15=sum(o['p']*o['v15'] for o in out.values()); ev10=sum(o['p']*o['v10'] for o in out.values())
print('valor esperado beta1.5',round(ev15,2),'beta1.0',round(ev10,2))
# sanity: sheet base through engine ratio
chk=run([{'inp':dict(base),'g':0.062,'m':0.17}])[0]; print('check',DCF*chk/ref)
# sensitivities on story A/B midpoint
sens=[]
for g in (0.04,0.06,0.08,0.10,0.12):
    row=[]
    for m in (0.12,0.15,0.17,0.19,0.21):
        row.append({'inp':base,'g':g,'m':m})
    sens.append(row)
flat=[x for r in sens for x in r]; vals=run(flat)
grid_=[[round(DCF*vals[i*5+j]/ref,2) for j in range(5)] for i in range(5)]
print('grid g x m (beta 1.5)',grid_)
for beta in (0.62,1.0,1.25,1.5):
    i=dict(inp); i['wacc']=wacc(beta); print('beta',beta,'wacc',round(wacc(beta),4),'valor base',round(DCF*run([{'inp':i,'g':0.062,'m':0.17}])[0]/ref,2))
json.dump({'stories':out,'ev15':ev15,'ev10':ev10,'grid':grid_},open('reference/analisis_narrativa/CELH_historias.json','w'),ensure_ascii=False,indent=1)

# DCF inverso con distintos márgenes y betas (calibrado contra el Base de la hoja)
gs=[x/1000 for x in range(-50,401,2)]
res={}
for beta in (1.5,1.0):
    for m in (0.17,0.19,0.22):
        i=dict(inp); i['wacc']=wacc(beta); i['salesToCapital']=2.5
        vals=run([{'inp':i,'g':g,'m':m} for g in gs])
        v=[DCF*x/ref for x in vals]
        g_imp=next((gs[k] for k in range(len(gs)) if v[k]>=27.71),None)
        res[f'b{beta}_m{m}']=g_imp
        print('beta',beta,'margen',m,'crecimiento implícito años 1-5:',g_imp)
d=json.load(open('reference/analisis_narrativa/CELH_historias.json')); d['inverso']=res
json.dump(d,open('reference/analisis_narrativa/CELH_historias.json','w'),ensure_ascii=False,indent=1)
