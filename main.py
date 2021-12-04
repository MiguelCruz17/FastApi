from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
from Modelo import  *
import Database as bd
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def Inicio():
    return {"Mensaje": "Inicio"}

@app.post("/Factura/Agregar", tags=['Facturación'])
def Agregar(Fac: Factura):
    bd.guardar(Fac)
    return {"Mensaje":"Los datos fueron guardados y recibí " + str(len(Fac.Detalle))}
    
@app.put("/Factura/Actualizar", tags=['Facturación'])
def Actualizar(Fac: Factura):
    bd.actualizar(Fac)
    return {"Mensaje":"Los datos fueron actualizados."}

@app.delete("/Factura/Eliminar", tags=['Facturación'])
def Eliminar(Fac: Factura):
    bd.eliminar(Fac)
    return {"Mensaje":"Los datos fueron eliminados."}


@app.get("/Factura/Lista", tags=['Facturación'])
def lista_Facturas():
    result = bd.cargar()
    return result     


 # Clientes   

@app.post("/Cliente/Agregar", tags=['Clientes'])
def Agregar_Cliente(Cle: Clientes):
    bd.GuardarCliente(Cle)
    return {"Mensaje":"Los datos fueron guardados"}
    
@app.put("/Cliente/Actualizar", tags=['Clientes'])
def Actualizar(Cle: Clientes):
    bd.ActualizarCliente(Cle)
    return {"Mensaje":"Los datos fueron actualizados."}

@app.delete("/Cliente/Eliminar", tags=['Clientes'])
def Eliminar(Cle: Clientes):
    bd.EliminarCliente(Cle)
    return {"Mensaje":"El usuario fue eliminado."}

@app.get("/Cliente/Lista", tags=['Clientes'])
def Lista_de_Clientes():
    result = bd.CargarClientes()
    return result



# Articulos  

@app.post("/Articulo/Agregar", tags=['Artículo'])
def Agregar_Articulo(Art: Articulos):
    bd.GuardarArticulo(Art)
    return {"Mensaje":"Los datos fueron guardados"}
    
@app.put("/Articulo/Actualizar", tags=['Artículo'])
def Actualizar(Art: Articulos):
    bd.ActualizarArticulo(Art)
    return {"Mensaje":"Los datos fueron actualizados."}

@app.delete("/Articulo/Eliminar", tags=['Artículo'])
def Eliminar(Art: Articulos):
    bd.EliminarArticulo(Art)
    return {"Mensaje":"El artículo fue eliminado."}

@app.get("/Articulo/Lista", tags=['Artículo'])
def Lista_de_Articulos():
    result = bd.CargarArticulo()
    return result              