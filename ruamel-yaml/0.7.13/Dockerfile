FROM python:3.9.5 as pyinstaller
WORKDIR /home/yaml
COPY values_yaml.py ./
RUN pip3 install \
    pyinstaller \
    ruamel.yaml==0.16.12 \
    -i https://mirrors.aliyun.com/pypi/simple/
RUN pyinstaller --noconfirm --clean values_yaml.py

FROM busybox
COPY --from=pyinstaller /home/yaml/dist/values_yaml /usr/lib/yaml
