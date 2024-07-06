FROM pytorch/pytorch:2.3.0-cuda12.1-cudnn8-devel

COPY . data

WORKDIR data

RUN pip install --no-cache-dir -r requirements.txt

WORKDIR ./conditional_INNs/colorization_cINN
RUN python setup.py build_ext --inplace

WORKDIR ./data

EXPOSE 8888

CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root"]