FROM ermiry/pycerver:latest

WORKDIR /home/status

COPY service .
COPY start.sh .

CMD ["/bin/bash", "start.sh"]
