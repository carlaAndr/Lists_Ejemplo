# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/03_lista_supermercado.ipynb.

# %% auto 0
__all__ = ['ListaSupermercado']

# %% ../nbs/03_lista_supermercado.ipynb 3
class ListaSupermercado:
    "Crea una lista de artículos de supermercado"
    def __init__(self) -> None:
        self.lista_super = []
    def agrega_articulo(self,
                        nombre:str): # Nombre con el que se creará el artículo
        "Crea un articulo de supermercado y lo agrega a la lista del supermercado"
        articulo = Articulo(nombre)
        self.lista_super.add(articulo)
    def marcar_agregado(self,
                        nombre:str # Nombre del articulo que va a buscar
                        ) -> bool: #Regresa True si el elemento estaba en la lista y fue marcado como completado
        "Busa un articulo por su nombre y lo marca como agregado"
        for articulo in self.lista_super:
            if articulo.nombre == nombre:
                articulo.estado = True
                return True
        return False
    def lista_completa(self)->str:
        "Imprime la lista de supermercado completa, incluyendo los elementos marcados como ya agregados"
        for articulo in self.lista_super:
            print(articulo)
    def lista_faltantes(self)->str:
        "Imprime los artículos que faltan por agregar a la lista"
        for articulo in self.lista_super:
            if articulo.estado == False:
                print(articulo)
    __repr__ = lista_completa
