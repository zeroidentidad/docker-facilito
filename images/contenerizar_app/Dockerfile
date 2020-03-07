FROM node

WORKDIR /app

COPY package.json .

RUN npm install

COPY index.js .

ENTRYPOINT ["node"]

CMD ["index.js"]