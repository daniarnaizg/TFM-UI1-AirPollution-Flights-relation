from datetime import datetime, timedelta

def gen_days():
    '''
    Función que devuelve los días en formato timestamp UNIX
    '''
    start_date = datetime(2020, 1, 1)
    end_date = datetime(2020, 1, 31)
    d = start_date
    dates = []
    while d < end_date:
        d_a = d
        d += timedelta(days=1)
        t1, t2 = gen_hours(d_a.timestamp(), d.timestamp())
        dates.append([round(d_a.timestamp()), round(d.timestamp()), round(t1), round(t2)])
    return dates    

def gen_hours(t1, t2):
    '''
    Función que devuelve la hora a la que pertenece cada timestamp
    '''
    t1 = int(t1)
    t2 = int(t2)
    h1 = t1 - (t1 % 3600)
    h2 = t2 - (t2 % 3600)
    return h1, h2

def gen_query(q):
    '''
    Función que genera la query para cada día del mes junto con la hora a la que pertenece.
    '''
    q1 = "SELECT * FROM state_vectors_data4 WHERE lat > 35.512 AND lat < 44.512 AND lon > -10.415 AND lon < 5.054 AND time>="
    q2 = " AND time<="
    q3 = " AND hour>="
    q4 = " AND hour<="
    q5 = " AND time%30=0;"
    return q1 + str(q[0]) + q2 + str(q[1]) + q3 + str(q[2]) + q4 + str(q[3]) + q5

if __name__ == '__main__':
    '''
    Función principal que escribe por pantalla las queries necesarias para obtner los datos deseados de la base de datos e OpenSky
    '''
    d = gen_days()
    for i in range(len(d)):
        query = str(i+1) + " ENE --> " + gen_query(d[i])
        print(query)
