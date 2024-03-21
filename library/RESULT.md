Tecnologias Utilizadas:

Backend (Django e Django Rest Framework):
Django: Utilizei o Django como framework principal do backend, fornecendo uma estrutura sólida para o desenvolvimento de aplicativos web.
Django Rest Framework (DRF): Implementei o DRF para criar uma API RESTful que permite a comunicação entre o frontend e o backend.
SQLite: Utilizei o SQLite como banco de dados leve e eficiente para armazenar os dados da aplicação, proporcionando um desempenho rápido e confiável.

Frontend (Vue.js 2):
Vue.js 2: Escolhi o Vue.js pela sua capacidade de criar interfaces de usuário dinâmicas e responsivas, garantindo uma experiência de usuário agradável. E pela praticidade do mesmo. 
Bootstrap: Utilizei o Bootstrap para facilitar o desenvolvimento do layout e dos componentes da interface do usuário, garantindo uma aparência moderna e consistente em todos os dispositivos.

Integração:
JavaScript e Python: Integramos de forma eficiente o frontend e o backend usando JavaScript no frontend (Vue.js) e Python no backend (Django). Essa integração perfeita permite uma comunicação eficiente entre os dois ambientes, garantindo uma experiência de usuário consistente e sem interrupções.
Recursos Principais da Aplicação:

Gerenciamento de Viagens: Os usuários podem facilmente adicionar, editar e excluir viagens, proporcionando uma maneira conveniente de organizar seu trabalho diário.
API RESTful: Utilizamos o Django Rest Framework para criar uma API RESTful poderosa, permitindo a comunicação eficiente entre o frontend e o backend.

A aplicação consiste em quatro telas:
Login, Registro, Listagem de viagens, Formulário para manutenção/cadastro de viagens. 

A partir do login podemos acessar a tela de registro para o cadastro de um novo usuário.
E logados temos acesso a listagem com um filtro de buscas. A partir da listagem podemos acessar o formulário de manutenção, bastando apenas clicar sobre a linha da viagem a qual queremos atualizar.
E caso queiramos acrescentar uma nova viagem há uma barra de navegação no topo com o acesso direto ao formulário em branco. 