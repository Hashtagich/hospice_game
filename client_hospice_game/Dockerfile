# Используем образ с Node.js
FROM node:16

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файл с зависимостями
COPY package.json package-lock.json ./

# Устанавливаем зависимости
RUN npm install

# Копируем все файлы
COPY . .

# Собираем приложение
RUN npm run build

# Устанавливаем команду, которая будет выполняться при запуске контейнера
CMD ["npm", "start"]
