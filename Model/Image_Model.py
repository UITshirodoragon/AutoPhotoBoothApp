import sqlite3
import os
import json

class ImageModel:
    def __init__(self, db_path = None):
        self.database_path = db_path

    def set_image_database_path(self, db_path: str) -> None:
        self.database_path = db_path
        
    def create_table_in_database(self)  -> None:
        conn = sqlite3.connect(self.database_path)
        cursor = conn.cursor()
        
        # Tạo bảng templates
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS images (
            id INTEGER PRIMARY KEY,
            name TEXT,
            path TEXT,
            size TEXT
        )
        ''')
        
        conn.commit()
        conn.close()

    def insert_image_into_database(self, name: str, 
                                   path: str, 
                                   size: tuple) -> None:
        conn = sqlite3.connect(self.database_path)
        cursor = conn.cursor()
        
        cursor.execute('''
        INSERT INTO images 
        (
            name, 
            path, 
            size
        )
        VALUES (?, ?, ?)
        ''', (
            name, 
            path, 
            json.dumps(size)
              )
        )
        
        conn.commit()
        conn.close()

    def get_image_from_database(self, id) -> dict:
        conn = sqlite3.connect(self.database_path)
        cursor = conn.cursor()
        
        cursor.execute('SELECT * FROM images WHERE id = ?', (id,))
        image = cursor.fetchone()
        
        conn.close()
        
        return dict(id=image[0], name=image[1], path=image[2], size=tuple(json.loads(image[3])))

    def get_image_with_field_from_database(self, id, field = None):
        conn = sqlite3.connect(self.database_path)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        
        cursor.execute('SELECT * FROM images WHERE id = ?', (id,))
        image = cursor.fetchone()
        conn.close()
        
        if image == None:
            print('Image not found')
            return None
        if field == None:
            return dict(id=image[0], name=image[1], path=image[2], size=tuple(json.loads(image[3])))
        elif field == 'name':
            return image[1]
        elif field == 'path':
            return image[2]
        elif field == 'size':
            return tuple(json.loads(image[3]))
        else:
            print('Field not found')
            return None
        
        
    def delete_image_from_database(self, id) -> None:
        conn = sqlite3.connect(self.database_path)
        cursor = conn.cursor()
        
        cursor.execute('DELETE FROM images WHERE id = ?', (id,))
        
        conn.commit()
        conn.close()
        
    def delete_all_images_from_database(self) -> None:
        conn = sqlite3.connect(self.database_path)
        cursor = conn.cursor()
        
        cursor.execute('DELETE FROM images')
        
        conn.commit()
        conn.close()
        
    def get_all_images_from_database(self) -> list[dict]:
        conn = sqlite3.connect(self.database_path)
        cursor = conn.cursor()
        
        cursor.execute('SELECT * FROM images')
        images = cursor.fetchall()
        
        conn.close()
        
        images = [dict(id=image[0], name=image[1], path=image[2], size=tuple(json.loads(image[3]))) for image in images]
        
        return images

    def update_image_in_database(self, id: int, 
                                 name: str = None,
                                 path: str = None,
                                    size: tuple = None) -> None:
        conn = sqlite3.connect(self.database_path)
        cursor = conn.cursor()
        
        if name is not None:
            cursor.execute('''
            UPDATE images
            SET name = ?
            WHERE id = ?
            ''', (name, id))
            
        if path is not None:
            cursor.execute('''
            UPDATE images
            SET path = ?
            WHERE id = ?
            ''', (path, id))
            
        if size is not None:
            cursor.execute('''
            UPDATE images
            SET size = ?
            WHERE id = ?
            ''', (json.dumps(size), id))
            
        conn.commit()
        conn.close()
        
    def count_images_from_database(self) -> int:
        conn = sqlite3.connect(self.database_path)
        cursor = conn.cursor()
        
        cursor.execute('SELECT COUNT(*) FROM images')
        count = cursor.fetchone()[0]
        
        conn.close()
        
        return count
    
    
            
            
if __name__ == '__main__':
    model = ImageModel("Data/ImageGallery/user_uit001_image_gallery/user_uit001_image.db")
    image_infos = model.get_all_images_from_database()
    for image_info in image_infos:
        print(image_info)