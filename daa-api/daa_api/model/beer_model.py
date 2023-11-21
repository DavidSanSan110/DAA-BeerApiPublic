from typing import Any, Dict

from daa_api import config, logger

from daa_api.model.db_model import PostgresSingleton

class FabricanteModel:

    id: str
    nombre: str
    logo: str

    def __init__(self, data: Dict[str, Any]) -> None:
        self.id = data[0]
        self.nombre = data[1]
        self.logo = data[2]

    def to_dict(self) -> Dict[str, Any]:
        return {
            'id': self.id,
            'nombre': self.nombre,
            'logo': self.logo
        }
    
class CervezaModel:
    
    id: str
    nombre: str
    tipo: str
    logo: str
    descripcion: str
    grados: float

    def __init__(self, data: Dict[str, Any]) -> None:
        self.id = data[0]
        self.nombre = data[1]
        self.tipo = data[2]
        self.logo = data[3]
        self.descripcion = data[4]
        self.grados = data[5]

    def to_dict(self) -> Dict[str, Any]:
        return {
            'id': self.id,
            'nombre': self.nombre,
            'tipo': self.tipo,
            'logo': self.logo,
            'descripcion': self.descripcion,
            'grados': self.grados
        }

class BeerModel:

    def __init__(self) -> None:
        self.db = PostgresSingleton.getInstance()
        self.db.connect()

    def get_fabricantes(self, api_key: str) -> [Dict[str, Any], str]:
        """
        This function returns a list of fabricantes.
        """

        try:

            output = []

            query = "SELECT * FROM public.fabricante WHERE api_key = %s"
            params = (api_key,)
            self.db.execute(query, params)

            result = self.db.fetchAll()

            for fabricante in result:
                output.append(FabricanteModel(fabricante).to_dict())

            if result is None:
                return None, "Fabricante not found"
            else:
                return output, "Fabricantes retrieved successfully"
        except Exception as e:
            return None, f'Error getting fabricantes: {e}'
        
    def get_cervezas(self, api_key: str, fabricante_id: int) -> [Dict[str, Any], str]:
        """
        This function returns a list of beers.
        """

        try:

            output = []
            finalOutput = {}

            query = "SELECT * FROM public.cerveza c, public.fabricante f WHERE c.id_fabricante = f.id AND c.id_fabricante = %s AND f.api_key = %s"
            params = (fabricante_id, api_key,)
            self.db.execute(query, params)

            result = self.db.fetchAll()

            for cerveza in result:
                output.append(CervezaModel(cerveza).to_dict())

            for cerveza in output:
                if cerveza['tipo'] not in finalOutput:
                    finalOutput[cerveza['tipo']] = []
                finalOutput[cerveza['tipo']].append(cerveza)

            if result is None:
                return None, "Fabricante not found"
            else:
                return finalOutput, "Cervezas retrieved successfully"
        except Exception as e:
            return None, f'Error getting cervezas: {e}'
        
    def delete_fabricante(self, fabricante_id: int) -> [bool, str]:
        """
        This function deletes a fabricante.
        """

        try:

            queryCerveza = "DELETE FROM public.cerveza WHERE id_fabricante = %s"
            queryFabricante = "DELETE FROM public.fabricante WHERE id = %s"
            paramsCerveza = (fabricante_id,)
            paramsFabricante = (fabricante_id,)
            
            self.db.execute(queryCerveza, paramsCerveza)
            self.db.execute(queryFabricante, paramsFabricante)

            return True, "Fabricante deleted successfully"
        except Exception as e:
            return False, f'Error deleting fabricante: {e}'
        
    def delete_cerveza(self, cerveza_id: int) -> [bool, str]:
        """
        This function deletes a cerveza.
        """

        try:

            query = "DELETE FROM public.cerveza WHERE id = %s"
            params = (cerveza_id,)
            
            self.db.execute(query, params)

            return True, "Cerveza deleted successfully"
        except Exception as e:
            return False, f'Error deleting cerveza: {e}'
        
    def add_cerveza(self, fabricante_id: int, nombre: str, tipo: str, logo: str, descripcion: str, grados: float) -> [bool, str]:
        """
        This function adds a cerveza.
        """

        try:

            query = "INSERT INTO public.cerveza (id_fabricante, nombre, tipo, logo, descripcion, grados) VALUES (%s, %s, %s, %s, %s, %s)"
            params = (fabricante_id, nombre, tipo, logo, descripcion, grados,)
            
            self.db.execute(query, params)

            return True, "Cerveza added successfully"
        except Exception as e:
            return False, f'Error adding cerveza: {e}'
        
    def update_cerveza(self, cerveza_id: int, nombre: str, tipo: str, logo: str, descripcion: str, grados: float) -> [bool, str]:
        """
        This function updates a cerveza.
        """

        try:

            query = "UPDATE public.cerveza SET nombre = %s, tipo = %s, logo = %s, descripcion = %s, grados = %s WHERE id = %s"
            params = (nombre, tipo, logo, descripcion, grados, cerveza_id,)
            
            self.db.execute(query, params)

            return True, "Cerveza updated successfully"
        except Exception as e:
            return False, f'Error updating cerveza: {e}'
        