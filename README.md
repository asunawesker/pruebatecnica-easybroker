# Pruebatecnica Easybroker

## Prerrequisitos

Instalar python, ejemplo de instalación para python en Ubuntu
```
sudo apt install python3.8
```

## Instalaciones previas

```
python -m venv env  || virtualenv -p python3 env
pip install -r requirements.txt
```

## Iniciar proyecto 

Entrar por medio de la terminal a la carpeta `pruebatecnica`, posteriormente ejecutar

```
source myvenv/bin/activate
python3 manage.py runserver
```

## Correr Test

Entrar por medio de la terminal a la carpeta `pruebatecnica`, posteriormente ejecutar

```
python3 manage.py test
```

## Capturas
![alt text](https://github.com/asunawesker/pruebatecnica-easybroker/blob/main/easybroker_images/easy1.png)

![alt text](https://github.com/asunawesker/pruebatecnica-easybroker/blob/main/easybroker_images/easy2.png)

![alt text](https://github.com/asunawesker/pruebatecnica-easybroker/blob/main/easybroker_images/easy3.png)

## Comentarios finales

El desarrollo en backend con django de la aplicación resultó mucho más sencillo que hacerlo con algún framework frontend. La forma en que se desarrolladon los test fue mucho más sencilla y práctica y al no haber problemas con los CORS la aplicación está lista para producción. 

La aplicación cumple con todos los requerimientos mandados para la prueba técnica, considero que se puede mejorar en código en la parte de views en properties y se podría hacer menos dependiente el código en esa parte, aún así no considero que haya un acoplamiento fuerte pero sin duda es mejorable.

El testing se centró principalmente en los servicios implementados para obtener la información de properties, property y contact request.

Para realizar las interfaces se utilizó bootstrap.
