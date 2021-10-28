FROM python:3.6


ADD main.py .

RUN pip install requests 
RUN pip install bs4 
RUN pip install requests_html 
RUN pip install pytest

COPY . /

CMD [ "python", "/main.py" ]
