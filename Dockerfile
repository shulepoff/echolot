FROM python:buster
RUN groupadd -r gunicorn && useradd -r -g gunicorn gunicorn
RUN pip install gunicorn==20.0.4
WORKDIR /
COPY foobar.py /
COPY shosser.db /
COPY run.sh /
EXPOSE 8000 
USER gunicorn
CMD ["/run.sh"]
