ENV PYTHONUNBUFFERED=1
# I deeply hope this actually does what I want it to.
RUN apt-get update && apt-get upgrade -y && \
  apt-get install python3-pip -y && \
  pip3 install pandas && \
  pip3 install matplotlib && \
  pip3 install sklearn && \
  pip3 install ordinal_encoders && \
  pip3 install -i https://test.pypi.org/simple/ lambdata-witterone && \
  python3 -c "import lambdata_witterone; print(lambdata_witterone.TEST)"
