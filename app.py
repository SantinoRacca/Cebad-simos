from flask import Flask, render_template, request, redirect, url_for
from database import supabase  # Tu conexión con Supabase

app = Flask(__name__)

# Ruta principal: Pantalla de Registro / Login moderna
@app.route('/')
def index():
    return render_template('index.html')

# Ruta de la Tienda: Catálogo de productos
@app.route('/tienda')
def tienda():
    return render_template('tienda.html')

# Ruta del Panel de Administración (Conectada a Supabase)
@app.route('/admin')
def admin():
    try:
        response = supabase.table('productos').select('*').execute()
        productos = response.data
    except Exception as e:
        print("Error al conectar con Supabase:", e)
        productos = []
        
    return render_template('admin.html', productos=productos)

# Ruta para agregar productos desde el panel de admin
@app.route('/admin/agregar', methods=['POST'])
def agregar_producto():
    nombre = request.form['nombre']
    precio = float(request.form['precio'])
    stock = int(request.form['stock'])
    
    try:
        supabase.table('productos').insert({
            "nombre": nombre, 
            "precio": precio, 
            "stock": stock
        }).execute()
    except Exception as e:
        print("Error al insertar producto:", e)
        
    return redirect(url_for('admin'))

# Ruta para eliminar productos desde el panel de admin
@app.route('/admin/eliminar/<int:id>')
def eliminar_producto(id):
    try:
        supabase.table('productos').delete().eq('id', id).execute()
    except Exception as e:
        print("Error al eliminar producto:", e)
        
    return redirect(url_for('admin'))

if __name__ == '__main__':
    app.run(debug=True)