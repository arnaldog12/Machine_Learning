# Introdução
___
Esse repositório foi criado com a intenção de difundir o ensino de Machine Learning em português. 

Os algoritmos aqui implementados não são otimizados e foram implementados visando o fácil entendimento. __Portanto, não devem ser utilizados para fins de pesquisa ou outros fins além dos especificados.__

Os códigos e explicações, quando tirados de outras fontes, são devidamente referenciados. __Por favor, entre em contato caso você tenha visto algo não referenciado__.

Sinta-se livre para contribuir nesse projeto!

# Instalação
1. Baixe ou clone o repositório.
2. Baixe e instale o [Miniconda](https://conda.io/miniconda.html). (__Windows__: marque a opção de adicionar o conda às variáveis de ambiente (_$PATH_))
3. Abra o terminal e digite o seguinte comando para instalar o ambiente:
    ```sh
    $ conda config --add channels bioconda
    $ conda create -n mpdl python=3.5.3 numpy=1.12.1 pandas=0.20.1 matplotlib=2.0.2 scikit-learn=0.18.1 seaborn=0.7.1 jupyter=1.0.0
    ```

# Uso do ambiente

> __Nota:  É obrigatório seguir as ordens da seção "Instalação" antes de utilizar o ambiente__.

Siga os passos abaixo sempre que quiser executar os códigos desse repositório.
1. Abra o terminal e digite:
    - __Windows__:
    ```sh
    $ activate mpdl
    ```
    - __Linux/Mac__:
    ```sh
    $ source activate mpdl
    ```
2. Execute o Jupyter Notebook:
    ```sh
    $ jupyter notebook
    ```