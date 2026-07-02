# Build from the PROJECT ROOT so the engine folders are in context:
#   docker build -f gtm-hosted-platform/brain/Dockerfile -t intradiem-gtm-brain .
FROM python:3.11-slim
WORKDIR /app
COPY gtm-hosted-platform/brain/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
# The brain imports these at runtime (it adds them to sys.path).
COPY tam-outbound-engine /app/tam-outbound-engine
COPY intradiem-signal-engine /app/intradiem-signal-engine
COPY impact /app/impact
COPY gtm-hosted-platform/brain /app/gtm-hosted-platform/brain
WORKDIR /app/gtm-hosted-platform/brain
EXPOSE 8000
# Set GTM_API_KEYS at run time, e.g. -e GTM_API_KEYS="slack:KEY1,claude:KEY2"
# Bind to the host's PORT (Render sets it); fall back to 8000 locally.
CMD ["sh", "-c", "uvicorn app:app --host 0.0.0.0 --port ${PORT:-8000}"]
