import sqlite3
from sqlite3.dbapi2 import Cursor

class Articulos:


    def abrir(self):
        conexion=sqlite3.connect("/home/adrian/Documentos/Análisis de redes/ferreteria.db")
        return conexion

    def alta(self,datos):
        cone=self.abrir()
        Cursor=cone.cursor()
        sql="INSERT INTO artículos(Artículo,Cantidad,Precio) values(?,?,?)"
        Cursor.execute(sql,datos)
        cone.commit()
        cone.close()

    def consulta(self, datos):
        try:
            cone=self.abrir()
            Cursor= cone.cursor()
            sql="select Artículo,Cantidad, Precio from artículos where Código=?,"
            Cursor.execute(sql,datos)
            return Cursor.fetchall()
        finally:
            cone.close()

    def recuperar_todos(self):
        try:
            cone=self.abrir()
            Cursor= cone.cursor()
            sql="select Código,Artículo,Cantidad, Precio from artículos"
            Cursor.execute(sql)
            return Cursor.fetchall()
        finally:
            cone.close()

    def baja(self,datos):
        try:
            cone=self.abrir()
            Cursor= cone.cursor()
            sql="delete from artículos where Código=?"
            Cursor.execute(sql,datos)
            cone.commit()
            return Cursor.rowcount #retornamos la cantidad de filas borradas
        finally:
            cone.close()









