---
name: pmx-specs-driven-development
description: Guía para aplicar Specs-Driven Development en un repositorio cuando colaboran personas y agentes de IA. Usa esta skill siempre que el usuario pida crear, organizar, continuar, revisar o cerrar una `spec`; cuando mencione carpetas `docs/specs/`, `Docs/Specs/`, `specs/`, `Specs/`, agrupadores, o archivos como `01.requirements.md`, `02.analysis.md`, `03.plan.md`, `03.plan.rev-NN.md`, `04.exec.phase-NN.md`, `05.summary.md`; o cuando hable de fases de ejecución, plan de implementación, revisión de plan, criterios de aceptación, análisis previo a implementar, o resumen final de una iniciativa documentada como spec. Aplícala también cuando se busque documentar trabajo de implementación de forma estructurada para que múltiples desarrolladores o agentes puedan retomarlo sin perder contexto.
---

# Specs-Driven Development

Esta skill traduce el enfoque **Specs-Driven Development** a una guía operativa. Su propósito es que cualquier persona o agente de IA pueda preparar, ejecutar y cerrar un cambio documentando los artefactos en una carpeta de `spec` con la estructura, los nombres y el flujo correctos.

La unidad principal de trabajo es la `spec`: una carpeta autocontenible que reúne planteamiento, análisis, plan, ejecución y cierre de un cambio o feature concreto.

## Cuándo aplicar esta skill

Actívala cuando el trabajo se beneficia de tratar la especificación como artefacto principal de coordinación. Señales típicas:

- El usuario pide crear una `spec` nueva, retomar una existente o avanzar a la siguiente fase.
- Se menciona crear `01.requirements.md`, `02.analysis.md`, `03.plan.md`, `04.exec.phase-NN.md`, `05.summary.md` o revisiones `03.plan.rev-NN.md`.
- Se discute la ubicación (`docs/specs/` vs `specs/`), agrupadores, o cómo nombrar una spec.
- Se va a documentar la ejecución de una fase o cerrar un ciclo.
- Hay colaboración entre varios agentes o desarrolladores y se quiere reducir pérdida de contexto.

No la apliques para tareas one-shot triviales que no justifican una spec (ediciones puntuales, hotfixes muy locales, exploraciones sin entregable). En esos casos, sugiérelo solo si el usuario explícitamente quiere documentar el cambio bajo este enfoque.

## Principio rector

Una spec debe cubrir **un solo objetivo verificable** y debe poder entenderse, implementarse y verificarse de forma relativamente autónoma. Si una spec empieza a parecer una iniciativa o roadmap, conviértela en un agrupador y descompónla en varias specs más pequeñas.

## Decisión 1 — Elegir la carpeta raíz

Antes de crear nada, decide dónde vivirán las specs en el repositorio:

- **`docs/specs/` o `Docs/Specs/`** — cuando el repositorio es principalmente una aplicación, servicio, librería, plataforma o componente técnico, y `docs/` puede alojar otros documentos (arquitectura, operación, troubleshooting, runbooks, guías de usuario).
- **`specs/` o `Specs/`** — cuando el repositorio es principalmente documental (guía de desarrollo, sitio de documentación, base de conocimiento) y las specs forman parte del flujo editorial principal.

Mantén la misma capitalización que el resto del proyecto: si usa `Docs/` con D mayúscula, usa `Docs/Specs/`; si usa minúsculas, usa `docs/specs/`. Si no hay convención clara, prefiere minúsculas.

Si la raíz ya existe en el repo, **úsala**. No crees una raíz alternativa.

## Decisión 2 — ¿Necesito un agrupador?

Un **agrupador** es una carpeta directamente bajo la raíz que agrupa specs relacionadas. Puede representar un módulo, subdominio, iniciativa, feature-set o área funcional. Su propósito es ordenar specs relacionadas, no introducir una jerarquía rígida.

Crea un agrupador cuando:

- varias specs pertenecen a un mismo aspecto funcional o subdominio, **y**
- la carpeta raíz comienza a perder claridad por volumen.

Empieza con una estructura plana. Introduce agrupadores cuando se justifiquen — no antes. Si solo hay una o dos specs, ponlas directamente bajo la raíz.

## Decisión 3 — ¿Subdividir esta spec?

Divide una spec en varias cuando ocurra **cualquiera** de estas condiciones:

- Requiere aprobaciones separadas.
- Puede entregarse en incrementos con valor independiente.
- Mezcla varios objetivos funcionales o técnicos poco acoplados.
- Su análisis, plan o ejecución dejan de ser entendibles como una sola unidad.

Cuando subdividas, agrupa las specs resultantes bajo un mismo agrupador para preservar la relación.

## Convenciones de nombre

Respeta estas convenciones **literalmente**. Son la única forma en que personas y agentes que retomen la spec puedan reconocer su estado de un vistazo. No inventes nombres alternativos (no `spec.md`, no `tasks.md`, no `decisions.md`, no `README.md` dentro de la spec) — usa solo los seis tipos de documento listados abajo.

| Segmento | Formato | Ejemplo |
| --- | --- | --- |
| Carpeta raíz común | `docs/specs` o `Docs/Specs` | `docs/specs` |
| Carpeta raíz especializada | `specs` o `Specs` | `specs` |
| Agrupador | `<slug>` | `access-control` |
| Spec | `<NNN>-<slug>` | `001-login-hardening` |
| Requerimientos | `01.requirements.md` | `01.requirements.md` |
| Análisis | `02.analysis.md` | `02.analysis.md` |
| Plan inicial | `03.plan.md` | `03.plan.md` |
| Revisión del plan | `03.plan.rev-NN.md` | `03.plan.rev-01.md` |
| Ejecución por fase | `04.exec.phase-NN.md` | `04.exec.phase-01.md` |
| Resumen final | `05.summary.md` | `05.summary.md` |

Reglas:

- El **slug** usa kebab-case y describe brevemente el agrupador o la spec.
- **Toda carpeta de spec lleva prefijo numérico `NNN-` obligatorio** (`001-validacion-credito`, no `validacion-credito`). El prefijo establece orden cronológico y trazabilidad; omitirlo rompe la convención y desordena la lectura.
- La spec se numera **dentro de su agrupador** con ceros a la izquierda (`001`, `002`, …). Si no hay agrupador, se numera dentro de la raíz.
- Las revisiones de plan y las fases de ejecución usan numeración independiente con dos dígitos (`rev-01`, `phase-01`, `phase-02`, …).
- No todas las specs necesitan revisiones de plan ni múltiples fases, pero conserva siempre la convención de nombres para preservar consistencia.
- **No introduzcas archivos adicionales** dentro de la carpeta de la spec (nada de `README.md`, `notes.md`, `tasks.md`, `decisions.md`). Si necesitas registrar algo, encaja en uno de los seis archivos canónicos. Si no encaja en ninguno, probablemente el contenido pertenece a documentación formal del proyecto, no a la spec.

## Estructura típica

Con agrupadores:

```text
📁 docs/specs/
├── 📄 README.md
├── 📁 comercializacion/
│   ├── 📁 001-trazabilidad-pedidos-mayoreo/
│   │   ├── 📄 01.requirements.md
│   │   ├── 📄 02.analysis.md
│   │   ├── 📄 03.plan.md
│   │   ├── 📄 03.plan.rev-01.md
│   │   ├── 📄 04.exec.phase-01.md
│   │   ├── 📄 04.exec.phase-02.md
│   │   └── 📄 05.summary.md
│   └── 📁 002-validacion-credito-cliente-industrial/
│       └── …
└── 📁 cumplimiento/
    └── 📁 001-resguardo-evidencia-firma-electronica/
        └── …
```

Sin agrupadores (estructura plana):

```text
📁 docs/specs/
└── 📁 001-integracion-firma-contrato-comercial/
    ├── 📄 01.requirements.md
    ├── 📄 02.analysis.md
    ├── 📄 03.plan.md
    ├── 📄 04.exec.phase-01.md
    └── 📄 05.summary.md
```

## Tipos de documento — propósito breve

Las plantillas completas viven en `assets/plantillas/`. Cópialas como punto de partida cuando crees cada archivo y adapta el contenido al caso concreto.

- **`01.requirements.md`** — Define **qué** se necesita, **por qué** y bajo qué **criterios de aceptación**. Fija el objetivo antes de discutir implementación. Plantilla: `assets/plantillas/01.requirements.md`.
- **`02.analysis.md`** — Documenta estado actual, restricciones, hallazgos y alternativas. Separa el entendimiento del problema del plan y de la ejecución. Plantilla: `assets/plantillas/02.analysis.md`.
- **`03.plan.md`** — Convierte el análisis en una secuencia ejecutable por fases, con validaciones previstas (idealmente pruebas unitarias, de integración y end-to-end según corresponda). Plantilla: `assets/plantillas/03.plan.md`.
- **`03.plan.rev-NN.md`** — Registra el resultado de revisar el plan (ajustes, interrogantes pendientes, o declaración de que el plan está listo). **No sobrescribe** el plan inicial; lo complementa. Plantilla: `assets/plantillas/03.plan.rev-NN.md`.
- **`04.exec.phase-NN.md`** — Registra la ejecución real de **cada** fase: cambios realizados, evidencias, validaciones y observaciones. Plantilla: `assets/plantillas/04.exec.phase-NN.md`.
- **`05.summary.md`** — Consolida planteamiento, análisis, plan y ejecución al cerrar la spec. Es el punto de entrada rápido para quien necesite entender el resultado sin releer todo. Plantilla: `assets/plantillas/05.summary.md`.

## Flujo de trabajo

1. **Crear la carpeta** de la spec dentro de su agrupador (o directamente bajo la raíz si no aplica agrupar).
2. **Redactar `01.requirements.md`** — objetivo, problema, alcance, criterios de aceptación.
3. **Elaborar `02.analysis.md`** — estado actual, restricciones, alternativas, enfoque propuesto.
4. **Definir `03.plan.md`** — estrategia general, fases concretas, validaciones previstas.
5. **Someter el plan a revisión** y obtener **aprobación explícita** del desarrollador responsable **antes** de ejecutar cualquier fase.
6. Si el plan necesita ajustes, tiene interrogantes pendientes, o se quiere declarar formalmente que está listo para ejecución, registrar el resultado en `03.plan.rev-NN.md` (numerando consecutivamente: `rev-01`, `rev-02`, …).
7. **Ejecutar fase por fase** y documentar **cada una** en su propio `04.exec.phase-NN.md`.
8. Si una fase requiere seguimiento posterior (incidencias, correcciones, ajustes), registrar el detalle en el archivo `04.exec.phase-NN.md` correspondiente o crear una **nueva fase** cuando el seguimiento tenga entidad propia.
9. Al concluir, consolidar en **`05.summary.md`**.
10. Si durante la ejecución cambia el alcance o se toma una decisión relevante, **reflejarlo en la spec** y no dejarlo solo en el historial del chat.

## Reglas críticas

Estas reglas existen para evitar errores recurrentes. Aplícalas con disciplina:

### No ejecutar fases sin aprobación previa, y registrarla por escrito

La existencia del análisis o de un plan detallado **no constituye autorización de ejecución**. Antes de tocar código o ejecutar comandos que materialicen una fase, confirma con el desarrollador responsable. Esta regla protege contra cambios irreversibles tomados a partir de supuestos.

La aprobación **debe quedar registrada en archivo**, no solo en el chat. La forma canónica es crear (o cerrar) un `03.plan.rev-NN.md` con conclusión `Plan listo para ejecución` y, si aplica, transcripción del acuse del responsable. El historial conversacional no es trazabilidad — el archivo sí.

Cuando alguien te pida "ejecuta ya" o "el plan está claro, procede" sin un rastro escrito de aprobación, **detente y pide el acuse explícito**, ofreciendo crear el `03.plan.rev-NN.md` que lo registre. No interpretes la prisa del usuario como autorización.

### Documentar cada fase ejecutada, aun si ya está descrita en el análisis

Cada fase planificada que se ejecute debe tener su propio `04.exec.phase-NN.md`. **No omitas su registro** aunque el contenido haya sido anticipado en `02.analysis.md` o resumido en otro artefacto. El análisis describe **lo que se entendió**; la ejecución registra **lo que efectivamente ocurrió**, con evidencias y validaciones. Son artefactos con propósito distinto.

Esto aplica incluso a fases que parecen "solo" levantamientos, inventarios, verificaciones iniciales u otras actividades ya explicadas en el análisis.

### Las revisiones de plan no sobrescriben el plan inicial

`03.plan.rev-NN.md` se crea como archivo separado para preservar trazabilidad. El `03.plan.md` original se mantiene; las revisiones registran los cambios, interrogantes o conclusiones de la revisión.

### Reflejar cambios de alcance en la spec, no en el chat

Si durante la ejecución cambia el alcance, surge una decisión relevante, o se descubre algo que altera el plan, actualiza la spec (en el archivo apropiado) — no asumas que el historial conversacional servirá de registro.

### Evitar duplicación con documentación formal del proyecto

La carpeta `specs` **no reemplaza** los artefactos formales de análisis, arquitectura, entrega o validación. Su propósito es coordinar implementación y dejar evidencia operativa.

- Usa `specs` para organizar el trabajo de una implementación concreta.
- Si una decisión, requisito, regla, contrato o validación tiene valor **permanente** más allá de esta implementación, documéntala en su capa disciplinaria correspondiente (ADRs, contratos, criterios de aceptación reutilizables, etc.) y **enlázala desde la spec**.
- La spec puede resumir o referenciar, pero no debería convertirse en una segunda taxonomía paralela.

## Cómo trabajar con esta skill

Cuando el usuario pide algo concreto, no asumas; verifica:

1. **Localiza la raíz de specs** en el repo (`docs/specs/`, `Docs/Specs/`, `specs/` o `Specs/`). Si no existe, propón crearla aplicando la Decisión 1.
2. **Identifica si pertenece a un agrupador** existente o si debe vivir en la raíz (Decisión 2).
3. **Asigna el número** (`NNN`) revisando las specs existentes en el mismo nivel — usa el siguiente disponible con tres dígitos.
4. **Crea solo los archivos que correspondan a la fase actual**. No anticipes archivos vacíos. Por ejemplo, no crees `04.exec.phase-01.md` antes de tener `03.plan.md` aprobado.
5. **Copia la plantilla** desde `assets/plantillas/<archivo>` y adáptala al contexto. No inventes una estructura distinta.
6. **Antes de avanzar a ejecución**, asegúrate de tener aprobación explícita registrada (ya sea en chat o, preferentemente, en una revisión `03.plan.rev-NN.md` con conclusión "listo para ejecución").
7. **Al cerrar**, revisa que el `05.summary.md` cubra objetivo original, solución ejecutada, fases completadas, ajustes relevantes, resultado de validación y pendientes.

Cuando dudes entre crear un archivo o anexar contenido a uno existente, prefiere **archivos nuevos** que respeten la convención (`phase-02`, `rev-02`) sobre engrosar el archivo previo — la modularidad facilita revisión.

## Lectura por niveles

Esta estructura permite leer una spec en dos niveles:

- **Lectura rápida** — `05.summary.md` para recuperar contexto general.
- **Lectura detallada** — `01` a `04` para reconstruir planteamiento, análisis, plan y ejecución.

Diseña tu redacción pensando en ambos niveles: el `05.summary.md` debe poder leerse aislado; los archivos `01`–`04` aportan el detalle verificable.

## Referencias

- `references/decisiones-y-flujo.md` — Criterios extendidos para decidir ubicación, agrupadores y subdivisión, junto con el flujo paso a paso con ejemplos de errores comunes.
- `assets/plantillas/` — Plantillas listas para copiar para cada tipo de documento.
