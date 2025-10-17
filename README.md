CHAED

Este proyecto es una página web desarrollada con Django. Su objetivo principal es dar a conocer los servicios de la cafeteria.
## Características


## Tecnologías Utilizadas
* **Python** 
* **Django** 
* **HTML5**
* **CSS3** 
* **JavaScript**
* **PostgresSQL**

  
## Configuración y Ejecución

Sigue estos pasos para poner en marcha el proyecto en tu entorno local:

### Prerrequisitos

Asegúrate de tener instalado:
* [Python 3](https://www.python.org/downloads/)
* [pip](https://pip.pypa.io/en/stable/installation/) (gestor de paquetes de Python)

### Instalación
1.  **Clona el repositorio**
2.  **Crea y activa el entorno virtual**:
    ```bash
    python3 -m venv venv
    # En Windows
    venv\Scripts\activate
    # En macOS/Linux
    source venv/bin/activate
    ```

3.  **Instala las dependencias**:
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configura la base de datos**:
    ```bash
    python manage.py migrate
    ```

5.  **Ejecuta el servidor de desarrollo**:
    ```bash
    python3 manage.py runserver
    ```

Ahora la aplicación debería estar funcionando en [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

## Uso

Una vez que la aplicación esté en funcionamiento:
1.  Navega a la URL principal.


## Contribución

¡Las contribuciones son bienvenidas! Si quieres mejorar este proyecto, por favor:
1.  Haz un "fork" del repositorio.
2.  Crea una nueva rama (`git checkout -b feature/nueva-funcionalidad`).
3.  Realiza tus cambios y haz "commit" (`git commit -m 'feat: Añadir nueva funcionalidad X'`).
4.  Haz "push" a tu rama (`git push origin feature/nueva-funcionalidad`).
5.  Abre un "pull request".

## Licencia
Ninguna
