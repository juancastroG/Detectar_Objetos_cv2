# Detector de objetos utilizando CascadeClassifier

##  Descripción general del proyecto:

Este proyecto tiene como objetivo detectar objetos específicos en tiempo real utilizando el algoritmo CascadeClassifier de la biblioteca OpenCV en Python. En este caso, los objetos a detectar son un mouse y una unidad USB. Se proporcionan códigos separados para la detección de cada objeto y un archivo para detectar ambos objetos en un solo código, aunque no es muy eficiente. Para desarrollar este proyecto, se hizo uso de la biblioteca cv2 y el algoritmo CascadeClassifier.

## Algoritmo CascadeClassifier de cv2

CascadeClassifier es un algoritmo de aprendizaje automático utilizado para la detección de objetos en imágenes. Este algoritmo se basa en la técnica de "características en cascada" que se utiliza para detectar objetos específicos. El algoritmo de CascadeClassifier utiliza un conjunto de características Haar para la detección de objetos. Estas características se derivan de las imágenes de entrenamiento que contienen los objetos que se quieren detectar. Una vez que se han extraído las características, se utiliza un clasificador para determinar si el objeto está presente o no en la imagen de prueba.

## Procesos de entrenamiento y test para la clasificación de imágenes

El proceso de entrenamiento para la clasificación de imágenes con el algoritmo CascadeClassifier consiste en lo siguiente:

1- Recopilar imágenes de entrenamiento que contengan los objetos que se quieren detectar.
2- Extracción de características utilizando el algoritmo de Haar.
3- Entrenamiento del clasificador utilizando un conjunto de datos de entrenamiento etiquetados.
4- Pruebas del clasificador utilizando un conjunto de datos de prueba.

## Requisitos

- cv2
- numpy
- imutils

## Uso
Para ejecutar el proyecto, simplemente corra el archivo detectadoFinal.py. La cámara se encenderá y comenzará la detección de objetos.
```bash
python detectadoFinal.py
```

## Autoría:
Este proyecto fue realizado por Juan Carlos Castro Guevara y cuenta con autoría propia.
