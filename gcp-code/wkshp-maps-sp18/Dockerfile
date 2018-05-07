FROM gcr.io/google-appengine/python

RUN apt-get update && apt-get install -y \
  binutils \
  gdal-bin \
  python-gdal
# Create a virtualenv for dependencies. This isolates these packages from
# system-level packages.
RUN virtualenv /env -p python2.7

# Setting these environment variables are the same as running
# source /env/bin/activate.
ENV VIRTUAL_ENV /env
ENV PATH /env/bin:$PATH

# Copy the application's requirements.txt and run pip to install all
# dependencies into the virtualenv.
ADD requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt
# Add the application source code.
ADD . /app

CMD gunicorn -b :$PORT main:app