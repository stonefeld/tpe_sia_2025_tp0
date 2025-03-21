<h1 align="center">Sistemas de Inteligencia Artificial</h1>
<h3 align="center">TP0: Introducción al Análisis de Datos</h3>
<h4 align="center">Primer cuatrimestre 2025</h4>

# Requisitos

* Python ([versión 3.12.9](https://www.python.org/downloads/release/python-3129/))
* [UV](https://docs.astral.sh/uv/getting-started/installation/)

# Instalando las dependencias

```bash
# Si python 3.12.9 no esta instalado se puede instalar haciendo
uv python install 3.12.9

# Para crear y activar el entorno virtual
uv venv
source .venv/bin/activate  # En Unix
.venv\Scripts\activate     # En Windows

# Para instalar las dependencias
uv sync
```

# Corriendo el proyecto

El proyecto fue probado en primera instancia con archivos dentro de la carpeta
`scripts/` pero luego fue pasado a un _Notebook_ de _Jupyter_ llamado
`analisis_notebook.ipynb`. Para poder abrirlo correr lo siguiente.

```bash
# Para abrir el notebook de jupyter
jupyter notebook
```
