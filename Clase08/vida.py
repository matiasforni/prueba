from datetime import time, timedelta, date, datetime

def vividos(nac):
    dia=int(nac[0]+nac[1])
    mes=int(nac[3]+nac[4])
    año=int(nac[6]+nac[7]+nac[8]+nac[9])
    hoy = date.today()
    a = hoy.year
    m= hoy.month
    d= hoy.day
    dia= d - dia
    mes= m - mes
    año= a - año
    año = año * 365
    mes = mes * 30
    dia = dia + mes + año
    segtotal= dia * 86400
    now = datetime.now()
    hora = int(now.strftime('%H'))
    min = int(now.strftime('%M'))
    segundos = int(now.strftime('%S'))
    hora = hora * 3600
    min = min * 60
    segundos = hora + min + segundos
    segundos = float(segundos)
    segtotal += segundos 
    return segtotal
  
nac = '21/08/1993'
seg=vividos(nac)
print('Vivi',seg, 'segundos')


