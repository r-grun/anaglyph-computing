FROM pytorch/pytorch:2.3.0-cuda12.1-cudnn8-devel

COPY . data

WORKDIR data

RUN pip install --no-cache-dir -r requirements.txt

RUN cd ./conditional_INNs && git submodule init && git submodule update


#CMD ["python", "<meinpythonfile>.py"]