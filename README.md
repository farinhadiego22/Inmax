Inmax - Fase 1 🧠📊
Inmax es un sistema web diseñado para la creación y monitoreo de campañas publicitarias, enfocado en captar y analizar interacciones de usuarios dentro de la red social Inmax. Esta es la primera fase del proyecto, centrada en levantar un entorno funcional con backend, base de datos y preparación para frontend.

🚀 Tecnologías utilizadas
FastAPI – Backend de alto rendimiento (Python).
MongoDB – Base de datos NoSQL para almacenamiento flexible.
Vue.js – Framework progresivo para el frontend (fase siguiente).
Docker y Docker Compose – Orquestación de servicios para facilitar el despliegue local y futuro en nube.
📂 Estructura del proyecto
Inmax/
├── Inmax-api/      # Código fuente del backend (FastAPI)
├── Inmax-bd/       # Configuración y scripts relacionados a MongoDB
├── docker-compose.yml
└── README.md
⚙️ Cómo levantar el entorno
Clona este repositorio:

git clone https://github.com/farinhadiego22/inmax.git
cd inmax
Levanta los servicios con Docker:

docker compose up --build
Accede a FastAPI en:
👉 http://localhost:8000/docs

Puedes verificar la base de datos MongoDB usando Mongo Compass o Mongo Express (si lo incluyes).

📌 Estado actual
✅ Backend funcional con FastAPI
✅ Conexión a MongoDB estable
✅ Endpoints estructurados para login, campañas y avisadores
🕐 Frontend en desarrollo (Vue.js, siguiente fase)
📄 Próximas tareas
Implementar frontend en Vue.js (Figma ya entregado por la empresa).
Añadir dashboards de monitoreo de interacciones.
Cálculo de métricas clave (CTR, ROI, conversión).
Seguridad y autenticación avanzada (Keycloak, JWT).
🧠 Contexto
Este sistema nace como una propuesta de mejora para la red Inmax de Aloxentric, como parte de un proyecto universitario con proyección a desarrollo real. Su objetivo es optimizar el proceso de publicación, seguimiento y análisis de campañas publicitarias dentro de la red.

🧑‍💻 Equipo
👨‍💻 Jorge Morris – Jefe de Proyecto
💡 + Integrantes (agrega los nombres)
📜 Licencia
MIT © 2025
