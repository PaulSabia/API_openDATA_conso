from pymongo import MongoClient
import tkinter as tk
from tkinter import filedialog
import subprocess


file = filedialog.askopenfilename()
subprocess.call(f"mongoimport --uri mongodb+srv://user:user@promessededon.sw4vx.mongodb.net/OpenData_ORE --collection conso_annuel --jsonArray --file {file}", shell=True)


