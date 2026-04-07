# Auditoría de Vulnerabilidades - StockGuard

## Resumen
Esta auditoría identifica vulnerabilidades críticas en el código heredado de StockGuard, un sistema de gestión de existencias en Python. Se han detectado 3 vulnerabilidades principales relacionadas con validación de entradas, manejo de errores y ausencia de pruebas. Las correcciones propuestas incluyen validaciones, manejo de excepciones y un suite de tests completo.

## Vulnerabilidades Identificadas

### 1. Falta de Validación de Entradas (qty y price)
**Descripción**: Las funciones `add_item()` y `update_price()` no validan que `qty` sea mayor que 0 ni que `price` sea mayor que 0. Esto permite introducir valores negativos o cero, lo que puede llevar a inconsistencias en el inventario (e.g., stock negativo) o cálculos erróneos del valor total.

**Riesgo**: 
- Stock negativo puede causar pérdidas financieras o errores en reportes.
- Precios absurdos (negativos o cero) distorsionan el valor total del inventario.
- Posible explotación maliciosa para manipular datos.

**Propuesta de Corrección**:
- Implementar funciones de validación en `validator.py`: `validate_qty(qty)` y `validate_price(price)`.
- Lanzar excepciones `ValueError` si los valores no son positivos.
- Integrar estas validaciones en `add_item()` y `update_price()`.

### 2. Ausencia de Manejo de Archivo JSON Corrupto
**Descripción**: La función `load_inventory()` usa `json.load(f)` sin capturar excepciones. Si el archivo `inventory.json` está corrupto (e.g., sintaxis JSON inválida), el programa lanzará una `json.JSONDecodeError`, causando un crash.

**Riesgo**:
- El sistema se vuelve inestable ante archivos dañados (e.g., por edición manual o fallos de disco).
- Pérdida de funcionalidad sin recuperación automática.
- Posible denegación de servicio si un atacante corrompe el archivo.

**Propuesta de Corrección**:
- Envolver `json.load(f)` en un bloque `try-except` en `storage.py`.
- Si ocurre una excepción, registrar el error y devolver una lista vacía o un valor por defecto.
- Opcionalmente, crear un backup del archivo corrupto antes de resetear.

### 3. Ausencia Total de Tests y Documentación
**Descripción**: No existen pruebas unitarias ni documentación (docstrings, README). Esto dificulta el mantenimiento, debugging y asegura la calidad del código.

**Riesgo**:
- Errores no detectados en futuras modificaciones.
- Dificultad para nuevos desarrolladores en entender el código.
- Falta de confianza en la funcionalidad.

**Propuesta de Corrección**:
- Crear tests en `tests/` usando pytest: `test_validator.py`, `test_storage.py`, `test_models.py`.
- Agregar docstrings a todas las funciones.
- Documentar en `README.md` con instalación, uso y sección IA.
- Implementar CI/CD con GitHub Actions para ejecutar tests y linting automáticamente.

## Conclusiones
Las vulnerabilidades son críticas y deben corregirse antes de desplegar el sistema. La implementación de validaciones, manejo de errores y tests mejorará la robustez y seguridad. Se recomienda seguir el plan de commits para una corrección incremental.