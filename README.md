
# **Título**: Análisis geoespacial de clientes para optimizar estrategias de ventas y marketing

## Introducción

- **Descripción del Proyecto:** 
 
La empresa dedicada a la comercialización de vestuario (importante mencionar qué tipo de vestuario), busca a través de la tecnología necesaria, recopilar, almacenar y organizar información geográfica de sus clientes, para así lograr establecer sus nichos de mercado, mejorar sus estrategias de marketing y potenciar sus ventas en determinados lugares específicos en la ciudad de Buenos Aires (ARG). 
Teniendo en cuenta las necesidades del cliente, proponemos el proyecto de análisis geoespacial; herramienta a través de la cual se pretende implementar una arquitectura web que permita recopilar información de los clientes directos e indirectos, con la recopilación de esta, se permitirá comprender las características sociodemográficas estableciendo de manera específica la relación entre necesidades vs ubicación. A su vez, esta herramienta busca establecer de manera georeferencial identificación de patrones especiales entre la distribución de los clientes y los puntos de mayores ventas o establecer puntos de clientes potenciales. Este proyecto, además, busca optimizar el almacenamiento de los datos significativos y que se consideren de relevancia para la compañía de acuerdo a sus necesidades para la creación de las estrategias de marketing y permitirá organizar información geográfica, focalizando puntos de ventas y brindando elementos para el análisis de posibles clientes.

El cliente, empresa dedicada a la comercialización de vestuario, busca comprender mejor a sus clientes B2B en la ciudad. Para ello, se propone un proyecto de análisis geoespacial que tiene como objetivos principales:

## Definiciones

- **B2B:** son empresas o entidades que ofrecen productos, servicios o soluciones a otras empresas en lugar de vender directamente a consumidores finales.

## Objetivo:

### Objetivo principal:

Implementar arquitectura web para la ejecución de un análisis geoespacial estableciendo polígonos de datos que permitan a la compañía mejorar sus estrategias de marketing y potenciar sus ventas en determinados lugares específicos en la ciudad de Buenos Aires (ARG).

### Objetivos secundarios: 

- Recopilar información a través de una base de datospara promocionar productos
- Ofrecer eficiencia a la exploración, Preparacion y visualizacin de los datos.
- Organizar información geográfica de los clientes potenciales a través de elementos de georreferenciación 

- **Contexto:**

El proyecto se centrará en mapear la ubicación precisa de los clientes, creando una representación visual detallada de su distribución espacial. Esta información nos permitirá identificar concentraciones de clientes, zonas de potencial crecimiento y áreas que podrían estar subatendidas.

En una etapa anterior, se llevó a cabo una segmentación de mercado utilizando técnicas de machine learning, aprovechando tanto los datos de los clientes como los registros de sus compras. Para este análisis en particular, nos centraremos en la información geoespacial, tomando los resultados de la segmentación previa.

El proyecto de análisis geoespacial incluirá los siguientes pasos:

- Recopilación y preparación de datos: Se recopilarán datos de clientes, ventas y censo de diversas fuentes. Los datos se limpiarán, formatearán y prepararán para el análisis.
- Análisis geoespacial: Se utilizarán técnicas de análisis geoespacial para analizar la distribución espacial de los clientes, las ventas y los datos demográficos. Se identificarán patrones y tendencias en los datos.
- Segmentación del mercado: Se segmentará el mercado en grupos de clientes con características y necesidades similares.
- Desarrollo de estrategias: Se desarrollarán estrategias de ventas y marketing dirigidas a los segmentos de clientes específicos.

Tipo de proyecto: Incremental.

## Datos 

Se utilizarán los siguientes conjuntos de datos

- Información geoespacial (polígonos) del Gran Buenos Aires:
    - Base de datos a utilizar: MongoDB.
    Justificación: El uso será limitado y no se necesitarán funciones avanzadas (intersección, unión y búfer). Inicialmente, se requiere calcular distancias desde el punto de la empresa hasta los clientes. Es necesario que la base de datos pueda escalar horizontalmente, ya que los polígonos pueden aumentar en el futuro. Además, su uso es más sencillo comparado con PostGIS, el cuál está diseñado para consultas más complejas como intersección, unión y búfer. Ademas, Información encriptada del cliente (Edad, Género, posición geográfica (longitud y latitud), grupo asignado)
    1. Mongo es una base de datos especializadas en geospacial para el almacenamiento
    2. Mongo es la ideal para subir archivos JSON dado a la data 
    3. No se usan bases de datos relacionales debido a que la complegidad de usar datos como **longitud y latitud** 

Base de datos **db_javeraian**, Colleccion **poligonos_buenos_aires**
a continuacion los datos del **JSON**
![tipos_datos_mongo.png](doc/img/tipos_datos_mongo.png)

- Información del censo.  
    - Base de datos a utilizar: SQL Postgres.
    Justificación: La información original no tiene un formato definido; sin embargo, todos los barrios tienen la misma información: nombre del barrio, número de hombres, número de mujeres y total por edades desde 0 a 110 años (años legales) y que no cuenta con una alta latencia en transacionalidades por segundo. Por lo tanto, se organiza en formato tabular por barrio y su contenido. Se podría usar MongoDB si se quisiera adicionar información única de cada barrio (número de parques, número de playas, etc.), pero como en este caso no es necesario, se elige usar SQL.
datos se almacenan en la base de datos **jave_database** tabla **census_data** a continuacion los siguientes **columnas**:

![tipos_datos_postgres.png](doc/img/tipos_datos_postgres.png)

- Información de la encuesta de bienestar. 
    - Base de datos a utilizar: SQL.
    Justificación: La información se manejará a nivel de personas individuales en lugar de casas u hogares, lo que nos proporciona una estructura de datos definida y permite el uso de SQL

![alt text](doc/img/tabla_postgis_mongo.PNG)

![alt text](doc/img/tabla_sql_mongo.PNG)

- **Alcance:**  

Se implementara la siguiente arquitectura para la solucion de los objetivos planteados y resolver las necesidades de la empresa dedicada a la comercialización de vestuario

    1. Se realiza lo siguiente
        a. **Login**: Se realiza en el front-end en **HTML5** que es una aplicativos **Web** que interactua con el usuario para ingresar al sistema con credenciales usuario o telefono y su contraseña además interactuar en el Back-end con **Python** para las conexiones de validacion del usario hacia la base de datos **Cassandra** dado a sus nodos podemos consultar por usurio o telefono mejorando la velocidad de respuesta y versatilidad y eficiencia 

        b. **Data Censo: ** Se realiza en el front-end en **HTML5** un aplicativo **Web** que interactua con el usuario para visualizar los insumos de data .csv a consumir por el sistema que interactua con **Python** para realizar los inserts a las bases de datos **Postgres** en sql relacionales

        c. **Data Buenos Aires:** Se realiza en el front-end en **HTML5** un aplicativo **Web** que interactura con el usuario para visualizar los insumos .geojson que interactua con **Python** para realizar los inserts en las base de datos de **MongoDb**
        
        d.**Mapas Analítica:** Se utiliza un front-end **Kepler.gl** y **HTML5** para la visualización de los mapas que interactuan con el usuarion para ver la exploracion y preparacion que realizo el aplicativo para encontrar los analisis con la finalidad de evidenciar estadisticamente datos significaativos de donde mas popular se comercializa vestidos 

        e.**Jupiter:** Se utiliza en la parte de backend para la exploración y preparación de los datos con la finalidad de que sevisualicen los datos de buenos aires y los clientes

        f.**Repositorio:** Se utiliza un controlador de repositorios **Git-Hub** para el control de versiones
        
        g.**Data proveedores:** Se utiliza la data de los provedores como insumos para iniciar con los analisis, exploración y preparación de los datos **.csv** y **.geojson** y es open source y para que no se compromentan nombres se limpian desde el inicio

        h.**Docker:** Se utiliza las contenedores con patron per servises para contenerizar las bases de datos y el aplicativo

![arquitectura.png](doc/img/arquitectura.png)

### Preguntas de negocio 

- Donde se encuentran los mejores clientes
- Los mejores o los peores se encuentran mas cerca o mas lejos
- Los mejores estan asociados a ingresos?


### Resultados esperados 

El proyecto se espera que resulte en los siguientes resultados:

- Una mejor comprensión de la distribución espacial de los clientes y las ventas.
- Una comprensión más profunda de la relación entre la ubicación de los clientes y sus características demográficas.
- Segmentos de mercado bien definidos con características y necesidades similares.
- Estrategias de ventas y marketing más efectivas dirigidas a segmentos específicos del mercado.

## Atributos de Calidad 

- **Escalabilidad:** Estos contenedores son aislados y consistentes, lo que significa que la aplicación se ejecutará de la misma manera en cualquier entorno que soporte Docker.
- **Rendimiento:** ya depende los recursos del servidor o la nuve que utilice en ram y almacenamiento
- **Disponibilidad:** No maneja
- **Seguridad:** Maneja temas de encriptación en password en base de datos utilizando hash
- **Mantenibilidad:** Utiliza un patron MVC modelo vista controlador para la mantebilidad
- **Confiabilidad:** Nivel de confiabilidad y cómo se garantizará.

## Descripción de la Arquitectura 
- **Diagramas de Arquitectura:** Se encuentra con 
- **Componentes:** Descripción de los principales componentes del sistema y sus responsabilidades.
- **Flujo de Datos:** Cómo se mueven los datos a través del sistema. (##### falta definirlo)

### Arquitectura (##### ni idea)
- Componentes
![arquitectura_componetes.png](doc/img/arquitectura_componetes.png)

## Tecnologías Utilizadas
- **Lenguajes de Programación:** Se utilizara Python
- **Frameworks y Librerías:** keplergl, dash
- **Plataformas y Servicios:** (##### ni idea)

## Configuración e Instalación
- **Requisitos Previos:** Python 3.10 (##### revisar el docker compose)
- **Instrucciones de Instalación:** Pasos detallados para instalar y configurar el proyecto.
- **Configuración Inicial:** Configuraciones iniciales que deben ser realizadas antes de ejecutar el proyecto.

### <a id='1'>Local usage of App </a>

1. Download the repository.

```bash
ssh git clone repositorio (add)
```

2. Navigate to the xxx folder.

```bash
cd folder/
```

3. Run the following Docker command:

```bash
docker compose build
```
After

```bash
docker compose up
```

4. Navigate to the "App" folder to run the App application, and execute it with the following instruction.

```bash
ssh python3 app.py
```

5. To access the app, open your preferred browser and enter the following command: (verificar si es 8080)

```bash
http://localhost:8080/
```

## Uso del Proyecto
- **Guía de Usuario:** Instrucciones sobre cómo usar el proyecto.

Al iniciar un mapa con la aplicación Kepler se mostrará una vista similar a la que se muestra en la siguiente imagen.

![alt text](doc/img/guia1.PNG)

1. Viñeta para desplegar funciones relacionadas con los datos.
2. Bones para desplegar funciones relacionadas con el mapa

Al despliegar la viñeta 1 se mostrará una vista similar a la que se muestra en la siguiente imagen.

![alt text](doc/img/guia2.PNG)

1. Botones para capas, filtros y otros.
2. Datos cargados actualmente.
3. Capas de datos cargadas actualmente; puede haber más de una capa a la vez.
4. Botón para crear una nueva capa, disponible solo si se tienen datos cargados previamente.

- **Ejemplos de Uso:** Ejemplos prácticos de cómo interactuar con el sistema.

Al iniciar un mapa, en este ejemplo, los barrios y comunas del Gran Buenos aires, se mostrará una vista similar a la que se muestra en la siguiente imagen.

![alt text](doc/img/guia3.PNG)

1. Mapa
2. Datos y capas cargados actualmente, los cuales se pueden modificar

(##### agregar videos)

En laviñeta de filtros se pueden aplicar filtros a necesidad, se mostrará una vista similar a la que se muestra en la siguiente imagen.(#### modificar imagen)

![alt text](doc/img/guia4.PNG) 

## Pruebas y Validación (##### ni idea)
Estrategia de Pruebas: Cómo se realizarán las pruebas para asegurar la calidad.
Casos de Prueba: Ejemplos de casos de prueba que se utilizarán.
Resultados Esperados: Resultados esperados de las pruebas.
 
## Pruebas y Validación (##### ni idea)
Estrategia de Pruebas: Cómo se realizarán las pruebas para asegurar la calidad.
Casos de Prueba: Ejemplos de casos de prueba que se utilizarán.
Resultados Esperados: Resultados esperados de las pruebas.

## Mantenimiento y Soporte (##### ni idea)
Guía de Mantenimiento: Procedimientos y mejores prácticas para mantener el sistema.
Soporte: Cómo obtener ayuda y soporte para el proyecto.

## Contribuciones (##### ni idea)
Guía de Contribución: Cómo otros pueden contribuir al proyecto.
Políticas de Código: Normas y políticas para contribuir con código al proyecto.

## Licencia (##### ni idea)
Licencia del Proyecto: Detalles sobre la licencia bajo la cual se distribuye el proyecto.








# Instalacion
pip install pymongo pandas flask python-dotenv xlrd openpyxl
python upload_data.py
python app.py

docker-compose up -d --build

usuario:felipe o 3224612380
pass jave2024


usuario: oscar o 3228344230
pass jave2024


# Subir archivos pesados 
git lfs install
git lfs track "*.gl.html"
git lfs push --all origin main
git add .
git commit -m "carga pureba"
git push

# traer a local
git checkout main 
git fetch origin main 
git merge origin/main

# subir
git add . 
git commit -m "cargue1" 
git push