import psutil

#retorna o disco romovível com maior espaço livre

def disco_removivel():
    discosArmaz = {}
    for disco in psutil.disk_partitions():
        if disco[3] == "rw,removable":
            espaco_livre = psutil.disk_usage(disco[0]).free
            discosArmaz[disco[0]] = espaco_livre
    maior = max(discosArmaz, key = discosArmaz.get)
    return maior, discosArmaz[maior]
    
print(disco_removivel())
