## build
FROM node:22-alpine AS base

WORKDIR /app

COPY package*.json ./

RUN npm install


## Development stage
FROM base AS development 

ENV NODE_ENV=development

COPY . .

EXPOSE 3000

CMD ["npm", "run", "dev"]

#
## Production stage
FROM base AS production

ENV NODE_ENV=production

COPY . .

RUN npm run build

EXPOSE 3000

CMD ["npm", "start"]
