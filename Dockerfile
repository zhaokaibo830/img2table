FROM continuumio/miniconda3

RUN conda create -n new_env_name python=3.11.9

RUN echo "conda activate new_env_name" >> ~/.bashrc

SHELL ["/bin/bash", "--login", "-c"]

RUN conda activate new_env_name

WORKDIR .

COPY img2table/ ./img2table/

COPY requirements.txt ./

RUN pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt

RUN #pyarmor gen -O code/ ./img2table/*

RUN #rm -rf ./img2table

EXPOSE 8004

WORKDIR ./img2table

#ENTRYPOINT ["python","run.py","-OPENAI_API_KEY","-OPENAI_API_BASE"]
