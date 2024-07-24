# Base image
FROM node:18

# Set working directory
WORKDIR /app

# Install dependencies
COPY package.json package-lock.json ./
RUN npm install

# Copy application code
COPY . .

# Build the application
RUN npm run build

# Start the application
CMD ["npm", "start"]
