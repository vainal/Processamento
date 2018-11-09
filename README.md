# Processamento
Requerimentos:
-Python3
-Octave 

Dependências python:
Para instalar as dependencias em python basta utilizar o comando “pip3 install -r requirements.txt”  (linux)
-scipy
-numpy
-pillow
-oct2py


Método de uso:
Mantenha os scripts na mesma pasta onde está a pasta destino dos tomates a serem processados
Altere a variável “path” no início da main em ambos os scripts para o nome da pasta
Em processamento.py, altere a variável “numTomates” caso o número seja diferente de 20 (usado por padrão no script)
Também em processamento.py, altere a variável “nomeTxt” para o nome desejado do documento txt com os resultados
Cada pasta dos tomates deve estar nomeada como “tomateX”, sendo x o número do tomate a ser processado.
Rode primeiro o script pngtobmp.py para obter as imagens convertidas em bmp e cortadas
Após isto rode o script processamento.py para obter o resultado dos processamentos em um txt.

O método usado depende de dois scripts, um chamado “pngtobmp.py” e o outro “processamento.py”. O primeiro script converte os tomates de png para bmp, além de realizar o corte em volta da região central, onde o biospeckle bateu mais diretamente. Ele salvará as imagens convertidas em uma pasta chamada “pastaBMP”, uma dentro de cada face do tomate.
	O segundo script faz o processamento em si. Usamos uma biblioteca chamada oct2py, que cria uma sessão de octave e realiza o processamento nela. Usamos a biblioteca Bio-Speckle Laser Tool Library para realizar o processament das imagens em si. Pode-se encontrar esta biblioteca em http://www.nongnu.org/bsltl/
