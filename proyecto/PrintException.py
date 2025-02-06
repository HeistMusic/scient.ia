import linecache
import sys
from datetime import datetime

def PrintException():
    try:
        exc_type, exc_obj, tb = sys.exc_info()
        f = tb.tb_frame
        lineno = tb.tb_lineno
        filename = f.f_code.co_filename
        linecache.checkcache(filename)
        line = linecache.getline(filename, lineno, f.f_globals)
        mensaje = 'EXCEPTION IN ({}, LINE {} "{}"): {}'.format(filename, lineno, line.strip(), exc_obj)
        x = datetime.now()
        fech = x.strftime('%Y-%m-%d')
        #f = open('static/logs/errores/' + str(fech) + '-errores.txt', "a+", encoding="ISO-8859-1", errors="ignore")
        #f.write(str(x.isoformat()) + ': ' + str(mensaje) + "\n")
        #f.close()
        print(mensaje)
    except:
        print('ERROR DE ERRORES')
        x = datetime.now()
        fech = x.strftime('%Y-%m-%d')
        #f = open('static/logs/errores/' + str(fech) + '-errores.txt', "a+", encoding="ISO-8859-1", errors="ignore")
        #f.write("ERROR DE ERRORES\n")
        #f.close()