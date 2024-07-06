FROM pytorch/pytorch:2.3.0-cuda12.1-cudnn8-devel

COPY . data

WORKDIR data

RUN apt-get update -y
RUN apt-get install -y libsm6 libxext6
RUN apt-get install -y libxrender-dev
RUN apt-get install -y libxrender1 libfontconfig1

RUN pip install --no-cache-dir -r requirements.txt

WORKDIR ./conditional_INNs/colorization_cINN
RUN python setup.py build_ext --inplace

WORKDIR /workspace/data

EXPOSE 8888

CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root"]