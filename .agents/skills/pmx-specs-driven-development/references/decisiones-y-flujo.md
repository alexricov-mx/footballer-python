# Decisiones y flujo extendido

Esta referencia amplía las decisiones y el flujo descritos en `SKILL.md`. Consúltala cuando una situación no esté cubierta por las reglas básicas o cuando necesites entender el porqué detrás de una convención.

## Por qué tratar la spec como artefacto principal

En entornos donde colaboran personas y agentes de IA, la conversación no debe sustituir a la documentación. La spec:

- explicita el problema y el resultado esperado antes de cambiar código;
- documenta supuestos, restricciones y decisiones para reducir ambigüedad;
- divide el trabajo en fases verificables que pueden revisarse y retomarse sin depender del contexto completo del chat;
- conserva evidencia de lo ejecutado para auditar cambios, reproducir resultados y corregir desviaciones.

Esto reduce pérdida de contexto, evita que decisiones importantes queden enterradas en el historial conversacional y facilita retomar una spec sin reconstruir todo desde cero.

## Ubicación de specs — criterios extendidos

### `docs/specs/` (o `Docs/Specs/`)

Usar cuando:

- El repositorio es **una aplicación, servicio, librería, plataforma o componente técnico**.
- La carpeta `docs/` puede alojar **otros tipos de documentos** además de specs: arquitectura, operación, troubleshooting, runbooks, guías de usuario, ADRs, etc.
- Quieres mantener las specs separadas pero dentro del paraguas documental del repo.

### `specs/` (o `Specs/`)

Usar cuando:

- El repositorio es **principalmente documental**: una guía de desarrollo, un sitio de documentación, una base de conocimiento, un manual.
- Las specs forman parte del flujo editorial principal y no necesitan quedar anidadas dentro de otra carpeta documental.
- Anidarlas bajo `docs/specs/` produciría una estructura redundante.

### Mantener la elección

Una vez elegida la raíz, conserva la misma estructura interna (agrupadores, specs y documentos numerados). No mezcles `docs/specs/` y `specs/` en el mismo repositorio.

## Agrupadores — cuándo introducir uno

Empieza con una estructura **plana** (specs directamente bajo la raíz). Introduce agrupadores solo cuando:

- Varias specs comparten un mismo aspecto funcional (módulo, subdominio, iniciativa, área).
- La cantidad de specs en la raíz dificulta la navegación.
- Quieres que el agrupador sirva como contexto compartido (por ejemplo, "todas las specs de `comercializacion/` se evalúan con el mismo equipo").

No introduzcas agrupadores anticipadamente "por si acaso". Es más fácil mover una spec a un agrupador cuando se justifique que deshacer una jerarquía prematura.

## Subdivisión — más detalle

Las cuatro condiciones para dividir una spec en varias se resumen en SKILL.md. Aquí ejemplos típicos:

- **Aprobaciones separadas**: la spec mezcla cambios que requieren validación legal con cambios técnicos que pasan por revisión normal. Separa para que cada flujo de aprobación avance a su ritmo.
- **Entregas incrementales**: la spec abarca un cambio de schema, una migración de datos y una nueva UI. Cada paso tiene valor por sí solo y puede liberarse de forma independiente.
- **Objetivos poco acoplados**: una spec habla de "modernizar el módulo de pagos" e incluye refactor interno + cambio en gateway externo + reportes nuevos. Son objetivos distintos.
- **Complejidad de lectura**: cuando la sola lectura del `02.analysis.md` deja a quien lo lee sin un modelo mental claro al final.

Regla práctica: si una spec empieza a parecer una **iniciativa o roadmap**, conviértela en un agrupador y descompónla.

## Numeración

- Los números (`NNN`) son **dentro de un mismo nivel**. Una spec `001` puede existir en `comercializacion/` y otra `001` en `cumplimiento/`; no compiten porque viven en agrupadores distintos.
- Usa **tres dígitos** para specs (`001`, `010`, `100`).
- Usa **dos dígitos** para revisiones y fases (`rev-01`, `phase-01`).
- No reutilices números aun si una spec se cancela o archiva. La continuidad numérica es trazabilidad histórica.

## Flujo paso a paso — con qué cuidado

### 1. Crear la carpeta

Verifica primero si existe la raíz (`docs/specs/`, `Docs/Specs/`, `specs/` o `Specs/`). Si no existe, propón crearla aplicando la decisión de ubicación. No crees archivos sueltos fuera de la raíz.

### 2. Redactar `01.requirements.md`

Objetivo principal: dejar claro **qué** se necesita y **cómo se sabrá que está resuelto**. Si los criterios de aceptación no son verificables (por ejemplo, "mejorar el sistema"), reformúlalos.

### 3. Elaborar `02.analysis.md`

Aunque el análisis describa trabajo que coincidirá con una o más fases del plan, ese contenido **no sustituye** la documentación de ejecución. La fase, cuando se ejecute, debe registrarse en su propio `04.exec.phase-NN.md`.

### 4. Definir `03.plan.md`

Cada fase debe poder ejecutarse y validarse. Si una fase no tiene validaciones claras, refínala. Las validaciones deberían incluir, según aplique:

- pruebas unitarias para lógica nueva o alterada;
- pruebas de integración para puntos de contacto entre componentes;
- pruebas end-to-end para flujos críticos del usuario.

No todas las fases requieren los tres niveles, pero el plan debe ser explícito sobre qué evidencia se espera.

### 5. Someter el plan a revisión

**Antes de ejecutar nada**, obtén aprobación explícita del desarrollador responsable. Esto es una salvaguarda fundamental: el análisis y el plan **no autorizan** la ejecución por sí mismos.

Si la aprobación ocurre en chat, considera transcribirla a una revisión `03.plan.rev-NN.md` con conclusión "listo para ejecución" para tener trazabilidad fuera del historial conversacional.

### 6. Registrar revisiones cuando aplique

Una revisión puede producir uno de tres resultados:

- **Ajustes relevantes al plan** (fases modificadas, agregadas, eliminadas o reordenadas).
- **Interrogantes o definiciones pendientes** en formato accionable, con su respuesta o decisión una vez resuelta.
- **Conclusión de que el plan está listo** para solicitar aprobación y pasar a ejecución.

Crea una revisión cuando ocurra cualquiera de los tres. No es necesario crear una revisión "por crear".

### 7. Ejecutar fase por fase

Cada fase ejecutada **debe** tener su propio `04.exec.phase-NN.md`, aun cuando ya esté descrita en `02.analysis.md`. El análisis describe la comprensión previa; la ejecución registra el hecho:

- qué se cambió realmente,
- qué comandos y validaciones se corrieron,
- qué evidencias quedaron,
- qué desviaciones aparecieron respecto al plan.

Cuando corras pruebas, incluye una **muestra representativa** de la salida para evidenciar la lógica ejercitada.

### 8. Seguimiento posterior a una fase

Si una fase requiere correcciones o ajustes:

- Si el seguimiento es menor y conceptualmente parte de la misma fase, regístralo en el mismo `04.exec.phase-NN.md`.
- Si el trabajo de seguimiento tiene entidad propia (otra ronda de cambios, nuevo alcance), crea una **fase adicional**.

### 9. Cerrar con `05.summary.md`

El resumen debe permitir entender el resultado **sin leer todo el historial**. Cubre:

- objetivo original (síntesis),
- solución ejecutada (resumen),
- fases completadas (relación breve),
- ajustes relevantes al plan,
- resultado de validación (con muestra de salida cuando aplique),
- pendientes o siguientes pasos.

### 10. Cambios de alcance durante ejecución

Si emerge una decisión que altera el plan, **actualiza la spec** en el archivo apropiado:

- Cambio en el alcance funcional → reflejar en `01.requirements.md` (con nota de cuándo y por qué cambió) o en una nueva revisión.
- Cambio técnico relevante → reflejar en `02.analysis.md` o en una revisión del plan.
- Decisión tomada al vuelo durante una fase → registrar en el `04.exec.phase-NN.md` correspondiente.

No dejes la decisión solo en el chat: la spec debe ser autocontenible.

## Errores comunes a evitar

- **Saltarse el análisis** porque "el plan está claro". El análisis fija supuestos que el plan después usa implícitamente.
- **Mezclar análisis y plan** en el mismo archivo. Pierdes la separación entre comprensión del problema y secuencia ejecutable.
- **Sobrescribir el plan original** en lugar de crear una revisión. Pierdes trazabilidad de cómo evolucionó el enfoque.
- **Ejecutar sin aprobación** porque "el plan estaba bien razonado". El razonamiento no es autorización.
- **No documentar una fase** porque "ya lo dijimos en el análisis". El análisis no registra ejecución real.
- **Crear `05.summary.md` antes de cerrar** la spec. El resumen consolida; no anticipes el cierre.
- **Duplicar contenido extenso** entre `specs` y la documentación formal del proyecto. Resume y enlaza; no copies.

## Relación con la documentación formal del proyecto

La carpeta `specs` cumple una función operativa. La documentación formal del proyecto (típicamente organizada por disciplina: estrategia, análisis, arquitectura, entrega, validación) preserva conocimiento estable y duradero.

Reglas prácticas:

- Usa `specs` para organizar el trabajo de una implementación concreta.
- Usa la documentación formal para conocimiento con valor más allá de una implementación.
- Cuando una decisión, regla, contrato o validación tenga **valor permanente**, documéntala en su capa disciplinaria correspondiente (ADR, contrato, criterio de aceptación reutilizable) y **enláza desde la spec**.
- Evita duplicar contenido extenso entre ambos espacios. La spec puede resumir o referenciar, pero no debería convertirse en una segunda taxonomía paralela.

Relación típica entre artefactos:

- `01.requirements.md` resume y referencia necesidades, requisitos o casos de uso de la capa de análisis formal.
- `02.analysis.md` se apoya en artefactos de análisis y arquitectura para justificar el enfoque.
- `03.plan.md` traduce ese contexto a una secuencia ejecutable.
- `04.exec.phase-NN.md` y `05.summary.md` registran evidencia operativa y transferencia de contexto; normalmente no sustituyen documentación formal.
- Si emerge una decisión técnica duradera durante la implementación, promuévela a un ADR u otro artefacto formal y enlázalo desde la spec.
- Si la validación requiere más formalidad o reutilización, registra criterios, escenarios o casos de prueba en la capa de validación y referencia desde la spec.
