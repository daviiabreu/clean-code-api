Ficamos em duvida entre go e python (go tinha os exemplos dos exercício, python temos mais familiaridade, facilidade com FastAPI e coisas do tipo). Optamos por seguir com python pela familiaridade e pelo tempo escasso. A partir disso, usamos a extensão de live shared para permitir que fizéssemos o exercício de forma simultânea, criando as pastas e arquivos em conjunto. Paralelamente estávamos fazendo pesquisas para buscar inspirações e referências de repositórios e artigos explicando sobre clean code em go (que paramos de ver depois de algumas pesquisas) e em python (que resolvemos priorizar). Achamos referências com arquitetura de pastas distintas, com /service e /handler mas sem /domain ou /repository. 

Depois de algumas pesquisas, achamos um arquivo da medium chamado "[Clean Architecture in Python (Without Overengineering](https://medium.com/the-pythonworld/clean-architecture-in-python-without-overengineering-d1088f179de2))", onde ele apresentava uma estruturada de pastas praticamente idêntica ao material presente no exercício (apenas trocou o /handler por /api, o que foi algo que nos deixou confusos inicialmente porque de cara não associamos que eles seriam a mesma coisa).

```python
project/  
│  
├── domain/  
│ └── models.py  
│  
├── services/  
│ └── user_service.py  
│  
├── repositories/  
│ └── user_repository.py  
│  
├── api/  
│ └── routes.py  
│  
└── main.py 
```

No entanto, apesar desse artigo dar um norte em relação ao caminho que nós precisávamos seguir, ele possuía pouco código como referência. Buscamos em outros artigos da [medium](https://medium.com/@bhagyasithumini/how-to-implement-clean-architecture-in-fastapi-a-step-by-step-guide-8b73a75c650b) sobre FastAPI, [repositórios do github](https://dev.to/alwil17/building-a-production-ready-fastapi-boilerplate-with-clean-architecture-5757) e [blogs de dev](https://dev.to/alwil17/building-a-production-ready-fastapi-boilerplate-with-clean-architecture-5757). Por fim, achamos também [esse site](https://oneuptime.com/blog/post/2026-02-03-python-repository-pattern/view) com a estrutura de pastas envolvendo as camadas de service, domain e infrastrucure. Esse site tinha bons códigos de referência e até mesmo exemplos de testes


Uma vez que tínhamos boas referências e um norte claro do que precisava ser feito e como precisava ser feito, partimos para a execução. Acabamos consultando alguns outros sites no meio do processo mas as principais bases de consulta foram as citadas anteriormente. Além disso, depois de criarmos a estrutura de pastas e os arquivos iniciais, percebemos que o Live Shared não ia funcionar tão bem, então commitamos o que tínhamos estruturado em conjunto inicialmente e depois resolvemos seguir trabalhando em paralelo mas não com as mudanças simultâneas do live shared.

O Matheus começou estruturando o domain e o repository, ele conseguiu fazer de forma até que rápida, buscando traduzir o que havia na proposta do desafio da ponderada para o código. Enquanto ele fazia essa estrutura, eu (daniel) estava documentando o que havia sido feito até então.

Depois, com essa primeira camada estruturada, dividimos as responsabilidades dos próximos passos, de modo que eu fiquei com o service, o Davi com o handler e banco de dados e o Matheus foi estudar sobre os testes unitários.

Tive bastante dificuldade em traduzir as regras de negócio para código, consultei alguns dos sites que tinha buscado de referência no início da atividade, aos poucos fui tendo mais clareza de como fazer o que precisava ser feito. Relendo o enunciado da ponderada me dei conta que o meu código precisava "servir" o handler, que teria as 5 rotas. Então entendi que dentro da minha classe `FigurinhaService` eu iria precisar de 5 funções, uma para cada rota e com as especificidades solicitadas na ponderada. A partir disso, com os exemplos dos sites que encontrei, documentações e pelo entendimento das regras de negócio da atividade, apesar de ter demorado um pouco, consegui desenvolver o que foi solicitado.

Enquanto eu mexia no service, o Davi ficou responsável pelo handler e pela parte de banco de dados. No handler ele montou as 5 rotas que a ponderada pedia (criar, listar, obter por id, atualizar e deletar) usando o `APIRouter` do FastAPI e deixando cada rota basicamente chamando a função correspondente do service, sem colocar regra de negócio ali dentro. Para o banco ele acabou indo de SQLite, que era algo mais simples de subir e que não dependia de configuração externa, criando o schema da tabela de figurinha e uma camada de repositório que conversava de fato com o banco. Como ele estava com essas duas pontas, ficou natural também juntar tudo no `main`, ligando o repositório ao service e o service ao handler para a api rodar de verdade.

Depois que cada um terminou a sua parte, juntamos tudo e fomos rodar a api pela primeira vez. Como era de se esperar, não funcionou de cara e apareceram alguns erros de import e de integração entre as camadas, que a gente foi ajustando aos poucos até a aplicação subir e responder as rotas como o esperado.