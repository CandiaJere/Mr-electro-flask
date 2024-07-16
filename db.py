import pymysql



def conectarMySQL():
    # local
    host="localhost"
    # port= 3306
    user="root"
    clave="admin"
    db="formulario_cliente"
    
    # deploy -> Pythonanywhere
    # host="CodeHunters2024.mysql.pythonanywhere-services.com"
    # user="CodeHunters2024"
    # clave="codo2024"
    # db="CodeHunters2024$formulario_cliente"


    return pymysql.connect(host=host,user=user,password=clave,database=db)
    # return pymysql.connect(host=host,port=port,user=user,password=clave,database=db)