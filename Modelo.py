from typing import List
from pydantic import BaseModel

# Detalles de la Factura

class DetallesFactura(BaseModel):
   f_id: int
   Codigo: int
   Nombre: str
   Precio: float
   Cantidad: int
   Total: float

# Factura
class Factura(BaseModel):
    id: int
    Fecha: str
    Cliente_id: int
    Descripcion: str
    Subtotal: int
    Itbis: int
    Total: int
    Detalle: List[DetallesFactura] = []

# Clientes
class Clientes(BaseModel):
    id: int
    Correo: str
    Nombre: str
    Apellido: str
    Rnc: str
    Telefono: str

# Articulos
class Articulos(BaseModel):
   id: int 
   Codigo: str
   Tipo: str
   Nombre: str
   Precio: float
   Cantidad: int
   Comentario: str 