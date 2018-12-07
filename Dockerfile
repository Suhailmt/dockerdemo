# Use Alpine Linux based Python 3.6 as our base
FROM python:3.6-alpine

# Where our app will live
WORKDIR /apps/demo

# Install pre-req libaries
RUN pip install flask

# Copy app contents
COPY server.py .
COPY templates ./templates
COPY static ./static

# Any environmental variables app uses
ENV PICTURE_OF car

# Network port
EXPOSE 8000

# Run the app!
ENTRYPOINT [ "python", "server.py" ]