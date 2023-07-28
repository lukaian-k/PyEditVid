# PyEditVid

PyEditVid é uma ferramenta de edição de vídeo em Python, permitindo cortar, adicionar texto e mesclar até três vídeos verticalmente.

## Tabela de Conteúdos

- [PyEditVid](#pyeditvid)
  - [Tabela de Conteúdos](#tabela-de-conteúdos)
  - [Visão Geral](#visão-geral)
    - [Recursos Principais:](#recursos-principais)
  - [Demonstração](#demonstração)
  - [Pré-requisitos](#pré-requisitos)
  - [Instalação](#instalação)
  - [Licença](#licença)

## Visão Geral

O PyEditVid é uma ferramenta de edição de vídeo simples, porém eficiente, desenvolvida em Python, projetada para atender às necessidades básicas de edição de conteúdo audiovisual. Com funcionalidades intuitivas, o PyEditVid oferece um conjunto de recursos diretos e práticos para realizar cortes de vídeo, adicionar legendas e unir diferentes clipes em um único vídeo, proporcionando uma solução descomplicada para edição de vídeos.

### Recursos Principais:
1. Corte de Vídeo: O PyEditVid corta o vídeo em trechos, oferecendo uma forma simples de repartir o vídeo em pedaços.

2. Adição de Legendas: O PyEditVid possibilita a inserção de legendas ao vídeo.

3. Combinação de Clipes: A ferramenta permite unir até três vídeos, empilhando-os verticalmente, proporcionando uma solução prática para criar montagens de conteúdo.

## Demonstração

<!-- [Inserir links para uma demonstração ao vivo, capturas de tela ou vídeos que mostram o projeto em ação.] -->

## Pré-requisitos

Antes de executar o PyEditVid, certifique-se de que seu ambiente de desenvolvimento atenda aos seguintes requisitos:

- **Python 3.x**: O PyEditVid é desenvolvido em Python e requer a versão 3.x do interpretador Python instalado em seu sistema. Se você ainda não possui o Python instalado, faça o download e instale a versão mais recente em [python.org](https://www.python.org/).

- **Bibliotecas Python**: O projeto utiliza algumas bibliotecas específicas para a edição de vídeo. Para instalar as dependências necessárias, você pode usar o arquivo `requirements.txt`. Execute o seguinte comando no terminal para instalar as bibliotecas requeridas:
    ```
    pip install -r requirements.txt
    ```

As bibliotecas listadas no `requirements.txt` são:
  - tkinter: Biblioteca gráfica utilizada para a interface de usuário.
  - moviepy: Biblioteca para edição de vídeos em Python.

Certifique-se de estar conectado à internet durante o processo de instalação, pois o pip irá baixar as bibliotecas da internet.

## Instalação

Siga as etapas abaixo para instalar o PyEditVid em seu ambiente de desenvolvimento:

1. **Python 3.x**: Certifique-se de ter o Python 3.x instalado em seu sistema. Se você não possui o Python instalado, faça o download da versão mais recente em [python.org](https://www.python.org/) e siga as instruções de instalação apropriadas para o seu sistema operacional.

2. **Bibliotecas Necessárias**: O PyEditVid requer a instalação de algumas bibliotecas Python para funcionar corretamente. Para instalar as dependências, abra um terminal ou prompt de comando e navegue até o diretório raiz do projeto (onde se encontra o arquivo `requirements.txt`). Em seguida, execute o seguinte comando para instalar as bibliotecas requeridas:
    ```
    pip install -r requirements.txt
    ```

3. **Clonando o Repositório**: Agora, você precisa obter o código-fonte do PyEditVid. Abra o terminal ou prompt de comando e execute o seguinte comando para clonar o repositório do PyEditVid:
    ```
    git clone https://github.com/lukaian-k/PyEditVid
    ```

4. **Acessando o Diretório do Projeto**: Navegue para o diretório recém-clonado:
    ```
    cd pyeditvid
    ```


5. **Executando o PyEditVid**: Agora, tudo está configurado e você pode executar o PyEditVid. No terminal ou prompt de comando, digite o seguinte comando:
    ```
    cd src
    ```
    ```
    python main.py
    ```

Siga essas etapas e o PyEditVid estará pronto para uso em seu ambiente de desenvolvimento.

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE), tornando-o livre para uso e distribuição, desde que respeitadas as condições estabelecidas na licença.
