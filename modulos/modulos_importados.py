#Poner siempre los import primero y luego los From, por último los from propios para que así se cargue todo correctamente.

import tkinter as tk
import os

#gráficos
from tkinter import font as tkfont  # python 3
from tkinter import ttk
from tkinter import StringVar
from tkinter import END
from tkcalendar import Calendar, DateEntry
#exportar excel
from openpyxl import Workbook
#fechas
from datetime import datetime

#Clases propias importadas

from modulos.graficos.PaginaCliente import * 
from modulos.graficos.PaginaFactura import *
from modulos.graficos.PaginaInicial import *
from modulos.graficos.PaginaResumen import *
from modulos.CRUD import *
import BACKEND




