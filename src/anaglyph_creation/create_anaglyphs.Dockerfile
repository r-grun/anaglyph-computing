FROM pytorch/pytorch:2.3.0-cuda12.1-cudnn8-devel

COPY . /workspace/anaglyph_computing

WORKDIR /workspace/anaglyph_computing

RUN echo "Acquire::Check-Valid-Until \"false\";\nAcquire::Check-Date \"false\";" | cat > /etc/apt/apt.conf.d/10no--check-valid-until

RUN apt-get update && apt-get install -y apt-transport-https
RUN apt-get install -y libsm6 libxext6 libxrender-dev libxrender1 libfontconfig1 ffmpeg nano
RUN pip install --no-cache-dir notebook opencv-python tqdm scikit-learn

WORKDIR /workspace

EXPOSE 8888

CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root"]