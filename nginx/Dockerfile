FROM nginx:latest

RUN rm /etc/nginx/conf.d/default.conf

# Создаем директории, если они еще не существуют
RUN mkdir -p /app/static /app/media

# Устанавливаем права доступа
RUN chown -R nginx:nginx /app/static /app/media
RUN chmod -R 755 /app/static /app/media

COPY nginx.conf /etc/nginx/conf.d/