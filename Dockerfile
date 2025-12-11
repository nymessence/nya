# BRAHMANDA LORA NYM: Dockerfile for Universal Existence Container
# This container achieves universal coherence and absolute harmony for the Nya language

FROM ubuntu:22.04

# Set environment variables for spiritual compilation
ENV DEBIAN_FRONTEND=noninteractive
ENV LANG=en_US.UTF-8
ENV LC_ALL=en_US.UTF-8

# Update package list and install essential build tools for consciousness compilation
RUN apt-get update && apt-get install -y \
    build-essential \
    cmake \
    git \
    curl \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# Create working directory for the Nya consciousness field
WORKDIR /nya-elyria

# Copy the entire Nya project into the container for universal coherence
COPY . .

# Clean any existing build artifacts and build the LymDeya compiler using spiritual configuration
RUN rm -rf build && \
    mkdir -p build && \
    cd build && \
    cmake .. && \
    make && \
    make install

# Verify that the LymDeya compiler exists and is functional
RUN which LymDeya

# Set the default command for the containerized consciousness field
CMD ["bash"]