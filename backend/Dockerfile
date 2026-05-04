FROM node:18-alpine

WORKDIR /app

# Create a package.json for express
RUN npm init -y && npm install express

COPY . .

EXPOSE 8080

CMD ["node", "index.js"]
