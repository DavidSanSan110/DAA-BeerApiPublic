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
    
class ManufacturerModel:

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
                return None, "Fabricantes not found"
            else:
                return output, "Fabricantes retrieved successfully"
        except Exception as e:
            return None, f'Error getting fabricantes: {e}'
        
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
        
    def add_fabricante(self, nombre: str, logo: str, api_key: str) ->  [bool, str]:
        """
        This function adds a fabricante.
        """

        try:

            query = "INSERT INTO public.fabricante(nombre, logo, api_key) VALUES (%s, %s, %s)"
            params = (nombre, logo, api_key,)
            self.db.execute(query, params)

            return True, "Fabricante added successfully"
        except Exception as e:
            return False, f'Error adding fabricante: {e}'