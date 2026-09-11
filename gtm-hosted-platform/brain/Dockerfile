# Build from the PROJECT ROOT (unchanged, so the existing Render build settings still work):
#   docker build -f gtm-hosted-platform/brain/Dockerfile -t intradiem-gtm-brain .
#
# The engine folders are NO LONGER copied in. Baking the CSVs into the image was the
# stale-data root cause: the data froze at build time and the only way to refresh what
# sellers saw was to redeploy, so it served July data into September. The brain now fetches
# the published gtm_state.json at runtime (GTM_STATE_URL), so a refresh is a file publish.
# 2026-09-05.
FROM python:3.11-slim
WORKDIR /app
COPY gtm-hosted-platform/brain/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY gtm-hosted-platform/brain /app/gtm-hosted-platform/brain
WORKDIR /app/gtm-hosted-platform/brain
EXPOSE 8000
# Required at run time:
#   GTM_STATE_URL   published snapshot, e.g. https://gtm-brain-state.pages.dev/gtm_state.json
#   GTM_API_KEYS    "slack:KEY1,claude:KEY2"
# Optional: GTM_STATE_TTL_SECONDS (300), GTM_STATE_MAX_AGE_HOURS (36),
#           GTM_STATE_HARD_MAX_AGE_HOURS (168)
# /healthz reports snapshot age and returns ok:false once the snapshot is not fresh.
CMD ["sh", "-c", "uvicorn app:app --host 0.0.0.0 --port ${PORT:-8000}"]
