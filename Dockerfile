FROM pytorch/pytorch:2.3.0-cuda12.1-cudnn8-devel

COPY . data

WORKDIR data

RUN pip install --no-cache-dir -r requirements.txt

CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root"]
#CMD ["python", "<meinpythonfile>.py"]