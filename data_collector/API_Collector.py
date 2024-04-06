from abc import ABC,abstractclassmethod

from .data_storage.database import Database

class APICollector(ABC):

    def __init__(self,url:str, api_key:str, ) -> None:
        self.url=url
        self.key=api_key
        self.database=Database()

    @abstractclassmethod
    def get_data(self)->list:
        pass

    
    

        
    
        

        
         



    

        
