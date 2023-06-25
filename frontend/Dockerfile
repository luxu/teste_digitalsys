FROM node:18
WORKDIR app
COPY * /app/
# Install vue first and then quasar
RUN npm install
RUN npm rebuild node-sass
RUN npm install -g quasar-cli
EXPOSE 8080
RUN npm run dev
