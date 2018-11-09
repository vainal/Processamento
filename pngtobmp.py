from PIL import Image
import os
from pathlib import Path

def getCenter(img):
    flag = 0
    #pega o pixel de menor e maior valor da imagem
    [min, max] = img.getextrema()
    for x in range(img.size[0]):
        if(flag == 0):
            for y in range(img.size[1]):
                if(img.getpixel((x,y)) == max):
                    xInicial = x
                    yInicial = y
                    flag = 1
        else:
            break

    return [xInicial, yInicial]



def main():
    pastasTomates = Path("Dia 2 - 240518 - Estagio 4")
    append = "pastaBMP"
    #for para iterar nas 20 pastas dos tomates
    i = 1
    for pasta in os.listdir(pastasTomates):
        path = pastasTomates / pasta
        #loopa cada uma das pastas contidas em path
        for file in os.listdir(path):
            #pega o caminho para cada uma das 3 pastas contidas na pasta do tomate
            folderPath = path / file
            print ("folderPath:  ", folderPath)
            #cria a pasta que conterá as imagens bpm
            if not os.path.exists(folderPath / append):
                os.makedirs(folderPath / append)
            count = 1
            #para cada imagem convertemos ela para bpm e salvamos na pasta que
            #contem as imagens convertidas
            flag = 0 #só precisamos pegar o primeiro pixel mais claro da primeira imagem
            for image in os.listdir(folderPath):
                if(image.endswith(".png")):
                    #print( "Join:  ", os.path.join(folderPath, image))
                    imagem = os.path.join(folderPath, image)
                    img = Image.open(imagem)
                    img = img.convert('L')

                    #se é a primeira imagem, devemos pegar as coordenadas do x e y mais claros
                    if(flag == 0):
                        [xInicial, yInicial] = getCenter(img)
                        flag = 1

                    #cortamos as imagens a fim de obtermos apenas a parte do tomate
                    img2 = img.crop((xInicial - 60, yInicial -40, xInicial + 60, yInicial + 50))
                    output = str(count) + ".bmp"


                    img2.save(folderPath / append / output)
                    #print ("Local Save:   ", folderPath + append + output)
                    count += 1

        i += 1




if __name__ == "__main__":
    main()
