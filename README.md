# Dockerfile
FROM n8nio/n8n:latest

# Copiar workflows exportados al contenedor
# Ajusta la ruta si tus JSON están en otra carpeta
COPY Flujo/workflows/ /workflows/

# (Opcional) Copiar credenciales NO recomendado (mejor por UI/Secrets)
# COPY Flujo/credentials/ /credentials/
