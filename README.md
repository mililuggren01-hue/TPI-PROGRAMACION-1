# 🌍 Sistema de Gestión de Datos de Países en Python

Este proyecto es el **Trabajo Práctico Integrador (TPI)** para la materia **Programación 1** de la *Tecnicatura Universitaria en Programación a Distancia* de la **Universidad Tecnológica Nacional (UTN)**[cite: 246, 247].

Consiste en una aplicación de consola desarrollada en Python 3.x orientada a la gestión, filtrado, ordenamiento y análisis estadístico de un dataset de países almacenado en formato CSV[cite: 262].

## 👥 Integrantes del Equipo
***Luggren María de los Milagros** - Desarrollo de Lógica, Filtros y Documentación[cite: 249].


---

## 🛠️ Características y Funcionalidades del Sistema

1.**Persistencia CSV:** Carga inteligente al iniciar y guardado automático al realizar altas o modificaciones utilizando rutas absolutas (`os.path`)[cite: 296, 299].
2. **Gestión de Países (ABM):** Agregar nuevos registros (evitando campos vacíos) y actualización de valores de población y superficie[cite: 298, 300].
3.  **Búsquedas:** Localización exacta o por coincidencia parcial de caracteres en el nombre del país.
4.  **Filtros Avanzados:** Filtrado por continente o mediante rangos numéricos acotados (superficie/población).
5. **Algoritmo de Ordenamiento Propio:** Implementación manual del método **Bubble Sort** (Ordenamiento de Burbuja) para organizar los datos por Nombre, Población o Superficie de manera ascendente y descendente sin usar funciones nativas como `sorted()`[cite: 285, 286].
6. **Módulo Estadístico:** Reportes del país con mayor/menor población, promedios generales y cantidad de países por región continental[cite: 288, 300].

---

## 🚀 Instrucciones de Uso

### Requisitos Previos
* Tener instalado **Python 3.x**.
* Asegurarse de que el archivo `paises.csv` esté ubicado en la misma carpeta que el ejecutable `TPI_paises.py`[cite: 296].

### Ejecución
Para iniciar la aplicación, ejecutá la terminal en el directorio del proyecto y corré:
```bash
python TPI_paises.py
