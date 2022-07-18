FROM python:3.9-alpine

RUN mkdir /service
COPY ./ /service

WORKDIR /service

RUN pip install -r requirements.txt
RUN python -m grpc_tools.protoc -I ./protos --python_out=. \
           --grpc_python_out=. ./protos/permission.proto

EXPOSE 50051
ENTRYPOINT [ "python", "permission.py" ]