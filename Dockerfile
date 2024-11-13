FROM pytorch/pytorch:2.3.0-cuda12.1-cudnn8-devel

COPY . /workspace

WORKDIR /workspace

RUN echo "Acquire::Check-Valid-Until \"false\";\nAcquire::Check-Date \"false\";" | cat > /etc/apt/apt.conf.d/10no--check-valid-until

RUN apt-get update && apt-get install -y apt-transport-https
RUN apt-get install git -y
RUN apt-get install -y libsm6 libxext6 libxrender-dev libxrender1 libfontconfig1 ffmpeg

RUN pip install --no-cache-dir -r requirements.txt

WORKDIR ./conditional_INNs/colorization_cINN
RUN python setup.py build_ext --inplace

WORKDIR /workspace

EXPOSE 8888

CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root"]