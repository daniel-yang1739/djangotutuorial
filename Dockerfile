FROM python:3.13.3-bullseye
WORKDIR /djangotutorial
RUN pip install django==5.2
CMD ["bash"]
