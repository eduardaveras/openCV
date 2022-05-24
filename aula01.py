import cv2 

img = cv2.imread('Assets/gato_cabecinha.jpg', 0)
#ajustando o tamanho
img_resized = cv2.resize(img, (0, 0), fx=0.5, fy=0.5) 
# fx e fy são as funções que devem multiplicar para ajustar o tamanho da imagem

#rotacionando a imagem
img_rotating = cv2.rotate(img, cv2.cv2.ROTATE_90_CLOCKWISE)

#salvando as alterações
cv2.imwrite('gato_cinza.jpg', img_rotating)

cv2.imshow('Image',img_rotating) #mostrando a imagem
cv2.waitKey(0) #quando tem 0 eu espero p sempre uma tecla ser apertada, quando tem 10 por exemplo espero por 10s 
cv2.destroyAllWindows() #fechando a imagem
