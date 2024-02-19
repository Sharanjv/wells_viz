import sqlalchemy
import os
import sys

def get_wells(depth, gradient):
    raw_query="""select latitude, longitude, depth, gradient 
                 from Wells 
                 where depth >=:depth and gradient >=:gradient; """
    sql_connect_string=os.getenv('DB_URL')
    engine = sqlalchemy.create_engine(sql_connect_string)
    with engine.connect() as conn:
        query=sqlalchemy.text(raw_query)
        result = conn.execute(query, {'depth': depth, 'gradient': gradient})
    
    return result.fetchall()     
    

if __name__ == '__main__':
    if len(sys.argv)!=3:
        print('Usage: database.py depth gradient')
        sys.exit()
    depth=sys.argv[1]
    gradient=sys.argv[2]    
    for row in get_wells(depth, gradient):
        print(row)
