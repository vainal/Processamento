from oct2py import octave
import oct2py
import os
from PIL import Image
from pathlib import Path

def salvaResutados(file, count, avds, ims, i):
    auxW = "avds do tomate " + str(i) + " face número " + str(count) + ":\n"
    file.write(auxW)
    auxW = "avd1: " + str(avds[(i-1)*3 + count - 1][0]) + "\n"
    file.write(auxW)
    auxW = "avd2: " + str(avds[(i-1)*3 + count - 1][1]) + "\n"
    file.write(auxW)
    auxW = "avd3: " + str(avds[(i-1)*3 + count - 1][2]) + "\n"
    file.write(auxW)
    auxW = "avd4: " + str(avds[(i-1)*3 + count - 1][3]) + "\n"
    file.write(auxW)

    file.write("\n")

    auxW = "ims do tomate " + str(i) + " face número " + str(count) + ":\n"
    file.write(auxW)
    auxW = "im1: " + str(ims[(i-1)*3 + count - 1][0]) + "\n"
    file.write(auxW)
    auxW = "im2: " + str(ims[(i-1)*3 + count - 1][1]) + "\n"
    file.write(auxW)

    file.write("\n\n")


    return


def main():
    
    path = Path("Dia 2 - 240518 - Estagio 4")
    numTomates = 20
    nomeTxt = "resultados-Dia-2-240518-Estágio-4" #Nome do arquivo txt cujos resultados serão salvos
    nomeTxt += ".txt"

    #inicia a sessão do octave e carrega a biblioteca bsltl 
    oc = oct2py.Oct2Py()
    oc.eval("pkg install -forge bsltl")
    oc.eval("pkg load bsltl")

    avds = []
    ims = []
    #inicia o processamento de todos os tomates
    with open(nomeTxt, "w") as file:
        numTomates += 1
        for i in range(1, numTomates):
            #Pasta do tomate, formatada aqui como "tomate@", sendo @ o seu número
            pastaAtual = path / ("tomate" + str(i))

            #contador para a face atual
            count = 1
            #itera pelas filmagens feitas (no caso 3)
            for pasta in os.listdir(pastaAtual):

                print("Estamos processando o tomate ", i, " face ", count)

                #diretorio onde se encontram as bmps
                imagesdirAux = pastaAtual / pasta / "pastaBMP"
                IMAGESDIR = str(imagesdirAux.resolve())
                oc.push("IMAGESDIR", IMAGESDIR)
                oc.eval("DATA = datapack(IMAGESDIR, '', 1, 128, 'bmp')", verbose=False)

                #Calcula o indice da metade da imagem em DATA
                oc.eval("[nRows, nCols, nFrames] = size(DATA)")
                oc.eval("thspCol = floor(nCols/2)")
                oc.eval("thspRow = floor(nRows/2)")

                oc.eval("THSP = thsp(DATA,1,thspRow)")
                oc.eval("COM = coom(THSP)")

                oc.eval("[AVD1, AVD2, AVD3, AVD4] = avd(COM,2,3,4)")
                oc.eval("[IM1, IM2] = inertiamoment(COM, 2)")

                #salvar as variaveis no ambiente python
                aux1 = ["AVD1", "AVD2", "AVD3", "AVD4"]
                [avd1, avd2, avd3, avd4] = oc.pull(aux1)
                aux2 = ["IM1", "IM2"]
                [im1, im2] = oc.pull(aux2)
                avds.append([avd1, avd2, avd3, avd4])
                ims.append([im1, im2])

                salvaResutados(file, count, avds, ims, i)
                #salva os resultados em um arquivo

                count+= 1

    return

if __name__ == '__main__':
    main()
