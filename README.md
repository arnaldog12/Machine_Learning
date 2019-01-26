# Introdução
Esse repositório foi criado com a intenção de difundir o ensino de Machine Learning em português.

# Algoritmos Implementados

| Classificação | Regressão | Clusterização | Redução de <br>Dimensionalidade |
|:----------------:|:--------------:|:-------------:|:-------------------------------:|
| 🌿 Adaboost | 📈 Linear | 🔠 K-Means | 🌹 PCA |
| 🌳 Decision Trees | 🔱 Multivariada |  | 🌻 LDA |
|  🏠🏠 K-NN | 📊 Polinomial |  |  |
| 🥴 Naive Bayes |  |  |  |
| 🧠 Redes Neurais |  |  |  |

E ainda temos um notebook só com métodos de **Seleção de Atributos**:

| Métodos de Filtragem (Filter Methods) | Métodos de Empacotamento (Wrapper Methods) | Métodos Embarcados (Embedded Methods) |
|:-------------------------------------:|:------------------------------------------:|:-------------------------------------:|
| 📈 📉 Correlação de Pearson | 🏆 Stability Selection | 📈 Regressão Linear |
| 📝 :left_right_arrow:📝 Mutual Information | 🔁 Eliminação Recursiva | 1️⃣ Regularização L1 (Lasso) |
| 💯 Maximal Information Coefficient | ⭐️ Boruta | 2️⃣ Regularização L2 (Ridge) |
|  |  | ⬇️ 💩 Mean Decrease Impurity |
|  |  | ⬇️ 🎯 Mean Decrease Accuracy |


# Instalação
1. Baixe ou clone o repositório.
2. Baixe e instale o [Miniconda](https://conda.io/miniconda.html). (__Windows__: marque a opção de adicionar o conda às variáveis de ambiente (_$PATH_))
3. Abra o terminal e digite os seguintes comandos para instalar o ambiente:
    ```sh
    $ conda config --add channels bioconda
    $ conda create -n ml python=3.5.3 numpy=1.12.1 pandas=0.20.1 matplotlib=2.0.2 scikit-learn=0.18.1 seaborn=0.7.1 jupyter=1.0.0
    ```

#### Uso do ambiente

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
