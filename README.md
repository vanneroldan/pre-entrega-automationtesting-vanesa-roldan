# Pre Entrega Automatización QA

## Objetivo

Automatizar pruebas sobre SauceDemo utilizando Selenium WebDriver y Pytest.

## Tecnologías

- Python
- Selenium WebDriver
- Pytest
- Pytest HTML
- Git
- GitHub

## Estructura del Proyecto

```text
pre-entrega-automationtesting-vanesa-roldan
│
├── tests
│   └── test_saucedemo.py
│
├── utils
│   ├── __init__.py
│   └── browser.py
│
├── reports
│   └── reporte.html
│
├── conftest.py
├── README.md
└── requirements.txt
```

## Instalación

1. Clonar el repositorio:

```bash
git clone URL_DEL_REPOSITORIO
```

2. Crear entorno virtual:

```bash
python -m venv venv
```

3. Activar entorno virtual:

```bash
venv\Scripts\activate
```

4. Instalar dependencias:

```bash
pip install -r requirements.txt
```

## Ejecución de Pruebas

```bash
pytest tests -v
```

## Generación de Reporte HTML

```bash
pytest tests -v --html=reports/reporte.html
```

## Casos de Prueba Automatizados

### Login Exitoso
- Navega a SauceDemo.
- Ingresa credenciales válidas.
- Valida acceso al inventario.

### Verificación de Catálogo
- Valida el título "Products".
- Verifica productos visibles.
- Comprueba menú y filtros.
- Obtiene nombre y precio del primer producto.

### Carrito de Compras
- Agrega un producto al carrito.
- Verifica el contador.
- Accede al carrito.
- Valida la presencia del producto agregado.

## Resultados

- ✅ Login automatizado
- ✅ Catálogo validado
- ✅ Carrito validado
- ✅ Reporte HTML generado