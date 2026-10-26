# Plantilla de diseño — Encuesta de satisfacción (hito 1)

**Equipo:** ___ · **Integrantes:** Jordan Sangucho, Josue Palma, Aidan Carrasco, Joel Champutiz, Emily Dias· **Fecha:** 25/10/2026
**Repositorio (fork):** https://github.com/josuepalma23/Lab3-Proyecto-EstII
**Enfoque del equipo (aprobado en clase):** Satisfacción y expectativas

Completa cada sección. Usa commits por sección; la historia del repositorio se revisa.

> **Formato del entregable:** exporta esta plantilla completada a PDF, con el enlace de tu fork en la carátula, y guarda el PDF en `informes/` del fork. Entrega el PDF y el enlace del fork en el aula virtual.

## 1. Objetivo de la encuesta

Estimar el porcentaje de personas satisfechas en el intervalo de 18 a 29 años en una escala del 1 al 5 con respecto a RetailAndina e identificar los beneficios que el encuestado espera sobre el programa de fidelización, con el objetivo de ser enviados a la gerencia para la posterior toma de decisiones.

## 2. Población objetivo

- **Población:** Personas de 18 a 29 años, residentes de la ciudad de Quito que compran en tiendas de consumo masivo de manera frecuente.
- **Límites y justificación:** 
  - Edad 18-29: Es el enfoque seleccionado, además de ser 18 años la edad mínima requerida para dar consentimiento informado y decidir compras por cuenta propia.
  - Residentes en la ciudad de Quito, para facilitar la recolección de información en la etapa de la encuesta.
  - Personas que compran de manera frecuente y al menos una vez al mes en tiendas de consumo masivo, garantiza que el encuestado tenga experiencia suficiente para opinar sobre el tema.
  - Las personas menores de 18 años y mayores de 29 años quedarán fuera de la encuesta, así como personas que no compran en tiendas de consumo masivo.

## 3. Método de muestreo

*Elige aleatorio simple, estratificado o conveniencia y justifica. Meta: 15–30 respuestas reales (3–6 por integrante); opcional: relleno simulado hasta 60–100 filas marcadas con la columna `origen`.*

- Método:
- Tamaño y justificación:
- Cómo se seleccionarán los participantes:
- **Equivalente en código (Python o R):** la línea que implementa tu método sobre un CSV de clientes (aleatorio simple, estratificado o conveniencia) con el resultado de una corrida con semilla, y una frase sobre por qué tu método (y no la conveniencia) justifica el hito.

## 4. Cuestionario (5–10 preguntas)

*Preguntas neutras, específicas, una idea por pregunta, opciones exhaustivas y excluyentes.*

| # | Pregunta | Tipo de variable | Dtype al cargar | Opciones / escala |
|---|---|---|---|---|
| 1 | | | | |
| 2 | | | | |
| ... | | | | |

*Nota: la columna "tipo de variable" usa la clasificación del cap. 3 (numérica continua/discreta, categórica binaria/ordinal). "Dtype al cargar" es cómo crees que llegará la columna en `df.dtypes`/`str()` (`int64`, `float64`, `str`/`object` según la versión de pandas). Pista: el dtype es una pista, no la clasificación — una ordinal puede llegar como `int`.*

## 5. Análisis de sesgos

*Identifica 2 problemas potenciales de esta encuesta y su mitigación.*

| Sesgo potencial | Mitigación |
|---|---|
| 1. | |
| 2. | |

## 6. Confidencialidad (RA3)

- Datos personales que se piden y por qué:
- Plan de anonimización (qué se quita o codifica antes de compartir):

## 7. Verificación con herramientas (Python/R)

*Escribe `scripts/verificacion_encuesta.py` (o `.R`): debe cargar `plantillas/encuesta_respuestas.csv` y reportar los tipos de cada columna, los datos faltantes por columna y la distribución de `satisfaccion_general` y `recomendaria`. Incluye la salida y responde:*

- ¿Coinciden los tipos con tu predicción de la sección 4?
- ¿Cuántos datos faltantes hay por columna?

*Ejecuta el script sobre el CSV final (separa con un filtro de la columna `origen` las filas reales de las simuladas): ¿qué resultado delataría un sesgo de **no respuesta** y cuál un sesgo de **respuesta**? Escribe tu interpretación usando solo las respuestas reales.*
