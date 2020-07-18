import tkinter as tk
from tkinter import font as tkfont  # python 3
from tkinter import ttk
from tkinter import StringVar
from tkinter import END
import os
import sqlite3
from BACKEND import *
from modulos.graficos.PaginaInicial import *
from modulos.graficos.PaginaCliente import *
from modulos.graficos.PaginaFactura import *
from modulos.graficos.PaginaResumen import *
from modulos.manejoBD.CRUD import *

#SETUP

NOMBREBD="clinica.db"
