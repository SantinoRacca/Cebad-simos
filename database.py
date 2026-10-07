from supabase import create_client, Client

SUPABASE_URL ="https://rbcgmkbvhouzqlxrnipg.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InJiY2dta2J2aG91enFseHJuaXBnIiwicm9sZSI6ImFub24iLCJpYXQiOjE3OTEzMjQ4ODUsImV4cCI6MjEwNjkwMDg4NX0.RQgpsUZgcsSZUmUf3rtfcxLMGMY3P7FRBzoZBkZizqU"

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

def obtener_productos():
    response = supabase.table('productos').select("*").execute()
    return response.data

def agregar_producto(nombre, categoria, precio, stock, imagen):
    supabase.table('productos').insert({
        "nombre": nombre,
        "categoria": categoria,
        "precio": precio,
        "stock": stock,
        "imagen": imagen
    }).execute()

def eliminar_producto(id_producto):
    supabase.table('productos').delete().eq('id', id_producto).execute()