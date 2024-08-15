FROM registry.access.redhat.com/ubi9/ubi-minimal

RUN microdnf update -y && \
    microdnf install -y python3 python3-pip && \
    microdnf clean all

USER 1001

WORKDIR /app
RUN python3 -m venv /app/.venv
ENV PATH="/app/.venv/bin:${PATH}"

COPY ./requirements.txt .

RUN python3 -m pip install -r /app/requirements.txt

COPY main.py .

# Configure the container to be run as an executable
ENTRYPOINT ["python3", "/app/main.py"]
