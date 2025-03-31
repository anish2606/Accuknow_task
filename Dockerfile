# Use Alpine Linux as base image
FROM alpine:latest  

# Install required dependencies including cowsay
RUN apk update && apk add --no-cache \
    fortune \
    netcat-openbsd \
    curl \
    git \
    perl \
    perl-utils \
    make \
    gcc \
    musl-dev \
    perl-dev 

# Clone and install cowsay manually
RUN git clone https://github.com/schacon/cowsay.git && \
    cd cowsay && \
    chmod +x install.sh && \
    ./install.sh && \
    mv cowsay /usr/bin/cowsay && \
    chmod +x /usr/bin/cowsay

# Set working directory
WORKDIR /app  

# Copy the script into the container
COPY wisecow.sh /app/wisecow.sh  

# Make the script executable
RUN chmod +x /app/wisecow.sh  

# Expose the port Wisecow uses (4499)
EXPOSE 4499  

# Run the script when the container starts
CMD ["/app/wisecow.sh"]
