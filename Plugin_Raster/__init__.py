def name():
    return "Raster"

def author():
    return "Miriam Temahuay Garcia"

def authorName():
    return author()

def email():
    return "mtemahuayg002@alumno.uaemex.mx"

def description():
    return "raster"

def about():
    return "Raster"

def version():
    return "0.0.1"

def qgisMinimumVersion():
    return "3.0"

def icon():
    return "raster.png"

def classFactory(iface):
    from .main import mainMenu
    return mainMenu(iface)