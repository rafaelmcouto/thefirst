FROM nginx

HEALTHCHECK --interval=30s --timeout=3s \
CMD curl -f http://localhost || exit 1
