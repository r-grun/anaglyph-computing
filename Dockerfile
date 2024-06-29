FROM pytorch/pytorch

COPY . data

WORKDIR data

#RUN pip install --no-cache-dir -r requirements.txt

#CMD ["python", "<meinpythonfile>.py"]