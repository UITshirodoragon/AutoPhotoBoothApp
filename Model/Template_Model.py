import sqlite3
import json
from multiprocessing import Queue


class TemplateModel:
    def __init__(self):
        self.database_path = 'Data/Template/Template.db'
        self.selected_template_id: int = 1
        
    def create_table_in_database(self)  -> None:
        conn = sqlite3.connect(self.database_path)
        cursor = conn.cursor()
        
        # Tạo bảng templates
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS templates (
            id INTEGER PRIMARY KEY,
            path TEXT,
            style TEXT,
            number_of_images INTEGER,
            image_positions_list TEXT,
            size TEXT,
            image_size TEXT
        )
        ''')
        
        conn.commit()
        conn.close()
    
    def insert_template_into_database(self, 
                                    path: str, 
                                    style: str, 
                                    number_of_images: int, 
                                    image_positions_list: list[tuple], 
                                    size: tuple, 
                                    image_size: tuple
                                    ) -> None:
        conn = sqlite3.connect(self.database_path)
        cursor = conn.cursor()
        
        cursor.execute('''
        INSERT INTO templates 
        (
            path, 
            style, 
            number_of_images, 
            image_positions_list, 
            size, 
            image_size
        )
        VALUES (?, ?, ?, ?, ?, ?)
        ''', (
            path, 
            style, 
            number_of_images, 
            json.dumps(image_positions_list), 
            json.dumps(size), 
            json.dumps(image_size)
              )
        )
        
        conn.commit()
        conn.close()
        
    def get_template_from_database(self, id) -> dict:
        conn = sqlite3.connect(self.database_path)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        
        cursor.execute('''
        SELECT * FROM templates WHERE id = ?
        ''', (id,))
        
        template = cursor.fetchone()
        conn.close()
        
        if(template == None):
            print("Template not found")
        
        return dict(template)

    def get_template_with_field_from_database(self, id, field = None):
        conn = sqlite3.connect(self.database_path)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        
        cursor.execute('''
        SELECT * FROM templates WHERE id = ?
        ''', (id,))
        
        template = cursor.fetchone()
        conn.close()
        
        if(template == None):
            print("Template not found")
        
        if field is None:
            return dict(template)
        elif field == 'path':
            return template['path']
        elif field == 'style':
            return template['style']
        elif field == 'number_of_images':  
            return template['number_of_images']
        elif field == 'image_positions_list':
            return json.loads(template['image_positions_list'])
        elif field == 'size':
            return json.loads(template['size'])
        elif field == 'image_size':
            return json.loads(template['image_size'])
        else:
            print("Field not found")
            return None



    def delete_template_from_database(self, id) -> None:
        conn = sqlite3.connect(self.database_path)
        cursor = conn.cursor()
        
        cursor.execute('''
        DELETE FROM templates WHERE id = ?
        ''', (id,))
        
        conn.commit()
        conn.close()
        
        
    def get_all_templates_from_database(self) -> list[dict]:
        conn = sqlite3.connect(self.database_path)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        
        cursor.execute('''
        SELECT * FROM templates
        ''')
        
        templates = cursor.fetchall()
        conn.close()
        
        templates = [dict(template) for template in templates]
            
        return templates
    
    def update_template_in_database(self, 
                                    id: int, 
                                    path: str = None, 
                                    style: str = None, 
                                    number_of_images: int = None, 
                                    image_positions_list: list[tuple] = None, 
                                    size: tuple = None, 
                                    image_size: tuple = None
                                    ) -> None:
        conn = sqlite3.connect(self.database_path)
        cursor = conn.cursor()
        
        if path != None:
            cursor.execute('''
            UPDATE templates 
            SET path = ?
            WHERE id = ?
            ''', (path, id))
            
        if style != None:
            cursor.execute('''
            UPDATE templates 
            SET style = ?
            WHERE id = ?
            ''', (style, id))
            
        if number_of_images != None:
            cursor.execute('''
            UPDATE templates 
            SET number_of_images = ?
            WHERE id = ?
            ''', (number_of_images, id))   
        
        if image_positions_list != None:
            cursor.execute('''
            UPDATE templates 
            SET image_positions_list = ?
            WHERE id = ?
            ''', (json.dumps(image_positions_list), id))
            
        if size != None:
            cursor.execute('''
            UPDATE templates 
            SET size = ?
            WHERE id = ?
            ''', (json.dumps(size), id))
        
        if image_size != None:
            cursor.execute('''
            UPDATE templates 
            SET image_size = ?
            WHERE id = ?
            ''', (json.dumps(image_size), id))
        
        conn.commit()
        conn.close()
        
        
    def count_templates_from_database(self) -> int:
        conn = sqlite3.connect(self.database_path)
        cursor = conn.cursor()
        
        cursor.execute('''
        SELECT COUNT(*) FROM templates
        ''')
        
        count = cursor.fetchone()[0]
        conn.close()
        
        return count
    
    def set_selected_template_id(self, id: int) -> None:
        self.selected_template_id = id

    def get_selected_template_id(self) -> int:
        print(self.selected_template_id)
        return self.selected_template_id

if __name__ == "__main__":
    template_model = TemplateModel()
    
    # # template_model.create_table_in_database()
    
    # # template_model.insert_template_to_database('Data/Template/template1.png', 
    # #                                            'normal_2grids', 
    # #                                            2, 
    # #                                            [(52,68), (780, 508)], 
    # #                                            (1500, 1100), 
    # #                                            (676, 507)
    # #                                            )
        
    # template = template_model.get_template_from_database(1)
    # print(type())
    pass