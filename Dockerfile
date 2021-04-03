# # Pull base Ubuntu 20.04 image
# FROM ubuntu:20.04
# Pull debian-based python image
FROM python:3.9.0-slim-buster

LABEL maintainer="hi@tobias.fyi"

# Initial envirovars
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set up source directories
ENV HOME=/home/src
RUN mkdir -p ${HOME}
# Set working directory
WORKDIR ${HOME}

# Create the app user
RUN addgroup --system savvy && \
    adduser --system --no-create-home --group savvy

# Install psycopg2 dependencies
RUN apt-get update && \
    apt-get upgrade -y gcc libpq-dev && \
    apt-get install netcat -y && \
    apt-get clean
# Install Python dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt ${HOME}
RUN pip install -r ${HOME}/requirements.txt

# Copy project
COPY . ${HOME}

# Copy entrypoint script
COPY ./entrypoint.sh ${HOME}
RUN chmod +x ${HOME}/entrypoint.sh

# chown all files to the app user
RUN chown -R savvy:savvy $HOME && chmod -R 755 $HOME

# Change to non-root user
USER savvy

# Expose port 8000 (if needed)
# EXPOSE 8000
ENTRYPOINT [ "/home/src/entrypoint.sh" ]

