from flask import Flask, render_template, request, redirect



from controller_db import *

app = Flask(__name__)




@app.route('/')
def index():
    return render_template('index.html', titulo="Mr Electro - Inicio")




# CRUD


@app.route('/contacto')
def contacto():
    clientes = listarClientes()
    return render_template('contacto.html', titulo ="Contactanos - Mr Electro", clientes=clientes)


# agregar datos 
@app.route("/agregar", methods=['POST'])
def agregar():
    nombre = request.form['nombre']
    email = request.form['email']
    contacto = request.form['contacto']
    result = cargar_nuevo_clie(nombre,email,contacto)
    print(result)
    return redirect('/contacto')
    
    
    
    
# Update
@app.route("/editar/<int:id>")
def editar(id):
    clie_por_id = obtener_clie_por_id(id)
    return render_template("edit.html", titulo = "EDITAR", cliente=clie_por_id)




@app.route('/edit/<int:id>', methods=['POST'])
def edit(id):
        id = request.form['id']
        nombre = request.form['nombre']
        email = request.form['email']
        contacto = request.form['contacto']
        actualizar_clie(nombre, email, contacto, id)
        return redirect('/contacto')





#delete
@app.route('/borrar/<int:id>')
def borrar_cliente(id):
    eliminar_clie(id)
    return redirect('/contacto')   
 
    
    
    
    



@app.route('/productos')
def productos():
    return render_template('productos.html', titulo ="Productos - Mr Electro")



@app.route('/servicios')
def servicios():
    return render_template('servicios.html', titulo ="Servicios - Mr Electro")



@app.route('/sucursales')
def sucursales():
    return render_template('sucursales.html', titulo ="Sucursales - Mr Electro")



if __name__=='__main__':
    app.run(debug=True)