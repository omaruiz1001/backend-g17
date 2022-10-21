from tabulate import tabulate

tabla = [
    ["cesar mayta", "cesarmayta@gmail.com","2302302302"],
    ["carlos perez","carlosperez@hotmail.com","9239293"]
]

columnas = ["nombre","email0","celular"]

print(tabulate(tabla,headers=columnas,tablefmt="grid"))