FROM prefecthq/prefect:3-python3.12

COPY remove_ads.py /tmp

RUN python /tmp/remove_ads.py
