FROM python
WORKDIR /src
RUN pip install flask
COPY . .
EXPOSE 3000
CMD python server.py
