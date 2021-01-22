# Shamir Secret Share Scheme
[![Generic badge](https://img.shields.io/badge/version-3.09.10-<COLOR>.svg)](https://shields.io/)
[![Open Source Love png1](https://badges.frapsoft.com/os/v1/open-source.png?v=103)](https://github.com/ellerbrock/open-source-badges/)
[![Generic badge](https://img.shields.io/badge/contributors-2-blue)](https://shields.io/)  
[![forthebadge made-with-python](https://forthebadge.com/images/badges/made-with-python.svg)](https://www.python.org/)  







# About
An implementation of the Shamir Secrete Share Scheme




# Como empezar
Primero que nada, es necesario mencionar que se encuentra escrito en Python, bajo las versiones superiores o iguales a Python3.8, por ello es recomendable actualizar a la versión de Python más reciente a tu ordenador, de lo contrario podrían ocurrir algunas fallas, y  de igual manera recomendamos ejecutar en ordenadores con Sistema Operativo GNU LINUX en cualquiera de sus versiones. 
Asimismo es necesario instalar algunas bibliotecas extras, no es necesario que te preocupes por instalar de forma correcta cada una de ellas, gracias a un script de auto-instalación


## Requerimientos
* Verifica utilizar una versión superior a Python3.6 :
```
python --version
```
> `Python 3.8+` is adviced  

  Nota, en algunos distros de Linux, lo correras como:  
  ```
  python3 --version
  ```


* Puedes revisar si tienes instalado PyPI así como Python 
  Disponible en el siguiente artículo
  [PyPI](https://www.tecmint.com/install-pip-in-linux/) up.  

* Tener instalado pip "Pip Installs Packages" para instalar las biblotecas necesarias

## Instalación

* Primero que nada deberás instalar todas las bibliotecas que se necesitan para que el progrmama corra, para esto sólo corre el siguiente comando

```
./installer.sh
```

# Uso
* Primero que nada para comprobar que todo este en orden correremos la prubas unitarias, para correrlas ejecutar el siguiente comando
```
bash test.sh
```
* El programa funciona de 2 maneras, para encriptar y para decriptar archivos. 
* Este programa implementa el Shamir Secrete Share Scheme, entonces necesitamos generar un polinomio de grado k-1 y n evaluaciones del polinomio

* Para encriptar un archivo se debe ejecutar el siguiente comando
```
python3 main.py c <archivo> <k> <n>
```
* k son el número minimo de evaluaciones para desencriptar el archivo
* n son el número de evaluaciones que se harán para después repartirlas

* Después de haber encriptado el archivo, el archivo original se borrará y habrá 2 nuevos archivos que tendrán los nombres:
```
archivo.frg 
```
y
```
archivo.aes
```
* El primer archivo es un archivo donde se guardaron las n evaluaciones, para después ser repartidas
* El segundo archivo es el archivo encriptado


* Ahora para descencriptar un archivo se deberá ejecutar el seguiente comando
```
python3 main.py d archivo.frg archivo.aes
```
* archivo.frg no necesariamente debe ser el archivo anteriormente generado, puede ser otro archivo que siga la misma nomenclatura que el archivo.frg originalmente generado, pero para poder descrinptar de buena forma el archivo.aes se necesitan minimo k evaluaciones

* archivo.aes es el archivo que se generó al encriptar el archivo original

* Si el archivo se desencritó de manera correcta el archivo original deberá aparecer de nuevo con su contenido original, si no es asi, es porque se evaluó menos de k evaluaciones o porque las evaluciones no eran las correctas.

## Generar Documentación
* Para generar la documentación sobre el proyecto se debe correr el siguiente comando
```
bash python-docs.sh
```
* Esto creará una carpeta llamada 
```
docs
```
* En la cual se encontrará toda la doc


# Desarrollado por:
#### David Hernández Urióstegui | No. de Cuenta: 420003708   &   Ian Israel García Vázquez | No. de Cuenta: 317097364

[<img src="https://img.shields.io/badge/gmail-D14836?&style=for-the-badge&logo=gmail&logoColor=white"/>](https://mail.google.com/mail/?view=cm&source=mailto&to=iangarcia@ciencias.unam.mx)
[<img src="https://img.shields.io/badge/gmail-D14836?&style=for-the-badge&logo=gmail&logoColor=white"/>](https://mail.google.com/mail/?view=cm&source=mailto&to=Dhdezu@ciencias.unam.mx)





---
![forthebadge biult-with-love](https://forthebadge.com/images/badges/built-with-love.svg) 
[![forthebadge powered-by-electricity](https://forthebadge.com/images/badges/powered-by-electricity.svg)](http://ForTheBadge.com)  

---
[Go up](#Shamir Secret Share Scheme)
