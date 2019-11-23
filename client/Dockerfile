FROM node:latest

RUN mkdir -p src/app


COPY package.json src/app

WORKDIR /src/app


RUN npm install 

COPY . /src/app

CMD ["npm", "start"]







