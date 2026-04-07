# StockGuard

![CI](https://github.com/yioqse/StockGuard/actions/workflows/ci.yml/badge.svg?branch=main)

## Descripción

StockGuard es un sistema de inventario simple desarrollado en Python que permite gestionar ítems con validación de cantidad y precio, almacenamiento en JSON y pruebas automatizadas. Incluye modelos de datos, funciones de validación, almacenamiento persistente y un pipeline de CI/CD con GitHub Actions.

## Instalación

1. Clona el repositorio:
   ```bash
   git clone https://github.com/yioqse/StockGuard.git
   cd StockGuard
   ```

2. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

## Cómo ejecutar tests

Para ejecutar las pruebas unitarias con pytest:

```bash
python -m pytest tests/ -v
```

O para una salida más concisa:

```bash
python -m pytest tests/ -q
```

## Uso de IA

Este proyecto fue desarrollado con asistencia de IA (GitHub Copilot) para acelerar el proceso de codificación y pruebas. La IA generó:

- **Tests unitarios**: Archivos `test_models.py`, `test_validator.py` y `test_storage.py` con casos de prueba completos, incluyendo mocks para simular archivos y errores.
- **Pipeline CI**: Archivo `.github/workflows/ci.yml` con configuración para linting y pruebas en GitHub Actions.
- **Docstrings**: Documentación en formato Google para todas las funciones públicas, inicialmente en inglés y luego traducidas al español.

Modificaciones realizadas por el desarrollador:

- Traducción de docstrings y comentarios al español.
- Instalación de python ver 13 y pytest para ejecucion de los tests
- Ajustes menores en el formato de los tests para cumplir con flake8.
- Actualización del README con secciones detalladas.

## Captura del CLI

Ejemplo de salida de los tests ejecutados localmente:

```
........................                                                 [100%]
24 passed in 0.05s
```

Esto indica que todas las 24 pruebas pasaron exitosamente.
