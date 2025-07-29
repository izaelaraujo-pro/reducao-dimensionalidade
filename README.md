# ESTUDO SOBRE REDUÇÃO DE DIMENSIONALIDADE COM PYTHON ✴
O Objetivo Gral desse código é processar e segmentar uma imagens em tons de cinza, aplicando técnicas básicas de visão computacional para destacar o bjetos ou regiões de interesse,e visualizar o efeito de cada etapa de maneira organizada.

## Em Resumo:
1. Recebe uma imagem enviada do computador.
2. Converte para tons de cinza, simplificando o processamento.
3. Aplica um desfoque (blur) para reduzir ruídos.
4. Aplica duas limiarizações (thresholding):
  - Uma normal (realça áreas claras).
  - Uma invertida (realça áreas escuras).
5. Cria uma máscara para destacar certas regiões da imagem original.
6. Monta uma grade de visualização com imagens lado a lado.
7. Exibe o resultado final no Google Colab.

---

No início do código, estou importante as bibliotecas NumPy e OpenCV.

1. **NumPy**: É uma biblioteca fundamental para computação numérica em Python.
O alias np é uma convenção comum para facilitar a chamada de métodos da biblioteca (ex: np.array() ao invés de numpy.array()).

    - Essa biblioteca é amplamente utilizada para lidar com matrizes e operações vetorias, que são essenciais em processamento de imagens (como manipulação de pixels, máscaras, kernels de convulação etc).
    - Imagens são, na prática, arrays multidimensionais (ex: largura x altura x canais de cor).

2. **OpenCV (Open Source Computer Vision Library)**: Essa biblioteca é uma das mais populares para visão computacional e processamento de imagens.

    - Ela permite realizar operações como:
      - Carregar e exibir imagens/vídeos.
      - Detectar objetos e rostos.
      - Aplicar filtros, bordas, segmentações.
      - Operações morfológicas, transformações geométricas, etc.
    - Trabalha muito bem com NumPy, já que converte as imagens diretamente em arrays.

  ---

<pre>
from google.colab import files
uploaded = files.upload()
</pre>
Aqui estou importando uma bibiloteca do Colab para fazer upload da imagem a ser analisada.

<pre>
import os 
print(os.listdir('.'))
</pre>

Aqui estou conferindo se foi feito o upload correto da imagem.

---

<pre>
img = cv2.imread('exemplo.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

suave = cv2.GaussianBlur(img, (7,7), 0) # aplica blur
(T, bin) = cv2.threshold(suave, 160, 255, cv2.THRESH_BINARY)
(T, binI) = cv2.threshold(suave, 160, 255, cv2.THRESH_BINARY_INV)

resultado = np.vstack([
    np.hstack([suave, bin]),
    np.hstack([binI, cv2.bitwise_and(img, img, mask = binI)])
])
</pre>

1. Na primeira linha, utilizei a função cv2.imread().
Ela carrega uma imagem que eu dei o nome de 'exemplo.jpg' no diretório atual e a converte para uma matriz NumPy (altura x largura x 3 canais de cor).
O resultado é atribuído a variável img.

    - Por que? Essa imagem será o ponto de partida para todos os processamentos seguintes.


---


2. Na segunda linha, utilizei a função **vc2.cvtColor(img, cv2.COLOR_BGR2GRAY)**.
Ela converte a imagem de BGR (formato padrão do OpenCV) para tons de cinza.
    - **cv2.COLOR_BGR2GRAY** é um código que indica o tipo de conversão.

    - Por que? Operações como desfoque, limiarização (threshold), bordas e segmentação geralmente são feitas com imagens em tons de cinza, pois simplificam o processamento (1 canal ao invés de 3).



---

3. Na terceira linha, atribui a função cv2.GaussianBlur(img, (7,7), 0) a variável suave.
Essa função aplica um desfoque gaussiano à imagem em tons de cinza.
(7,7) é o tamanho do kernel (janela de filtro), e o 0 é o desvio padrão (calculado automaticamente).

    - Por que? O desfoque ajuda a reduzir ruídos e pequenas variações locais de intensidade, melhorando a eficácia da limirização que vem a seguir.

---

4. Na quarta linha, apliquei a função cv2.threshold(suave, 160, 255, cv2.THRESH_BINARY) na tupla (T, bin).
Essa função aplica uma limiarização binária: todos os pixels com valor acima de 160 viram 255 (branco), os demais viram 0 (preto).

    - Por que? Útil para separar objetos calros sobre fundo escuro.

---

5. Na quinta linha, mesma coisa da anterior, só que com inversão de resultado.

    - Por que? Útil para obter o complemento da imagem anterior. Frequentemente usado quando você quer destacar o fundo ao invés do objeto, ou preparar uma máscara inversa.

---

6. Nas últimas linhas, utilizei a função np.vstack em forma aninhada, onde as de dentro une imagens horizontalmente, e as de fora une imagens verticalmente.

    - A função cv2.biwise_and(img, img, mask=binI) aplica a máscara binI sobre a imagem original em tons de cinza, "recortando" apenas as áreas onde a máscara é branca (255).

    - Por que? Essa visualização é excelente para compara os efeitos das etapas do processamento. Permite analisar o efeito do desfoque, o resultado da miliarização direta e invertida e como a máscara pode ser usada para isolar partes da imagem original.
  
---

<pre>
  from google.colab.patches import cv2_imshow
  cv2_imshow(resultado)
</pre>

<p align="center">
  <img width="621" height="932" alt="image" src="https://github.com/user-attachments/assets/267e38b8-c873-41e6-9fc3-9abbe08114a0" />
</p>


Aqui estou exibindo os resultados no Google Colab.
