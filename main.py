from pathlib import Path
def fayl(fayl_nomi : str, eski_joy : str, yangi_joy : str):

    desktop =Path("/Users/Erkin/Desktop/")
    eski_joy = desktop/eski_joy/fayl_nomi
    yangi_joy = desktop/yangi_joy/fayl_nomi
    eski_joy.replace(yangi_joy)
fayl("TEXT","Olmaliq","Toshkent")
def fayl2(eski_joy : str, yangi_joy : str):
    desktop =Path("/Users/Erkin/Desktop/")
    eski_joy =desktop/eski_joy/yangi_joy
    yangi_joy =desktop/yangi_joy
    eski_joy.replace(yangi_joy)
    yangi_joy.replace(eski_joy)
fayl2("Angren","Ohangaron")
