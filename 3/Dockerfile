FROM ubuntu:latest

RUN apt-get update && apt-get install -y wget python3 python3-pip 

COPY 1.py /tmp/extract_path_value.py
COPY 1.sh /tmp/search_path.sh
COPY data.txt /tmp/data.txt
RUN chmod +x /tmp/search_path.sh

WORKDIR /tmp

RUN echo "#!/bin/bash\n./tmp/search_path.sh /tmp/data.txt \$1 \n/usr/bin/python3 /tmp/extract_path_value.py /tmp/data.txt \$1 " > /tmp/run_all.sh 
RUN chmod +x /tmp/run_all.sh

ENTRYPOINT ["/tmp/run_all.sh"]
CMD ["file"]
