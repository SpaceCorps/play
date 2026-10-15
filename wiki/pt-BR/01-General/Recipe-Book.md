<!-- wiki-i18n source: 6ff3251582e96a39 -->
<!-- wiki-i18n title: Livro de receitas -->
# Livro de receitas e builds {#recipe-book-and-builds}

<!-- wiki-search: recipe; recipes; recipe book; bill; steps; chart; craft tree; what do i need; build; builds; loadout; preset; presets; import; export; json; my builds; share a build; receita; receitas; custo; etapas; diagrama; criar; equipamento; predefinição; predefinições; importar; exportar; meus builds; compartilhar um build -->

O **Livro de receitas** responde a “o que isto exige?” para qualquer item do jogo: um diagrama do que o compõe, as etapas em ordem, o custo completo e de onde vem cada matéria-prima. **Builds** faz o mesmo para uma nave inteira: importe o equipamento do seu hangar ou o build de um amigo, comece por uma das 15 predefinições ou crie o seu, e veja suas estatísticas e seu custo completo, passo a passo. Os dois ficam na **Biblioteca** da estação, abaixo da Wiki.

O Livro de receitas não guarda uma lista de preços própria: ele calcula seus números na hora em que você olha, a partir das receitas, dos preços, das tecnologias e das tabelas de drop que a Loja, a [Montagem](/wiki/06-Items/Overview.md#upgrading-modules) e a [Pesquisa](/wiki/03-Mechanics/Research.md) usam, e por isso acompanha o jogo quando um preço ou uma receita muda. É por isso que esta página não cita nenhum preço nem estatística: abra o item ou o build.

![The Builds page: the presets from early to late, and a build with its lasers, generators, extras and drones laid out in slots](../../img/wiki-img/shots/builds.jpg)
![The Bill tab: what the item takes in Credits, Thulium and raw items, with what you have and what is missing](../../img/wiki-img/shots/recipe-book-bill.jpg)
![An item in the Recipe Book: its ways to get it, the switches for the bill and the chart of what it takes down to the raw items](../../img/wiki-img/shots/recipe-book-chart.jpg)

## Abrir {#open-it}

Abra o menu da estação e escolha **Biblioteca › Livro de receitas** ou **Biblioteca › Builds**. O Livro de receitas lembra o último item que você viu, seus filtros e seu zoom, somente neste computador; seus builds não fazem parte disso ([Salvos na sua conta](#saved-on-your-account)). Quando o jogo é mais novo que o servidor com o qual ele fala, a página avisa e mostra menos: o Livro de receitas continua calculando tudo o que se compra, se cria ou se melhora, mas não sabe dizer onde o mundo dá um item (ele só escreve “Obter”), e Builds nomeia as partes que precisam do servidor mais novo: as predefinições, Meus builds e as estatísticas.

## Encontrar um item {#find-an-item}

A lista grande à esquerda tem todos os itens do jogo, agrupados por tipo e, dentro de um tipo, na ordem própria do jogo: o nível mais fraco primeiro. A EMP Charge, o único consumível, também está nela.

- **Busca.** Comece a digitar em qualquer lugar da página e o texto vai para o campo de busca. A lista vira uma lista só, ordenada pelo quanto o nome combina (o nome inteiro, o começo dele, o começo de uma palavra, qualquer parte, depois o tipo). Maiúsculas e acentos não importam, e o nome antigo de um item renomeado encontra o item. `Esc` limpa a busca.
- **Tipo.** O menu suspenso acima da lista a reduz a um tipo e diz quantos itens cada tipo tem. A chave ao lado ordena de A a Z dentro de cada tipo.
- **Linhas.** Uma linha mostra a imagem, o nome, o tipo e a raridade do item, um pequeno símbolo do caminho pelo qual você normalmente o obteria (feito na Montagem, vendido na Loja, cai ou é encontrado, prensado, ou produzido no buraco negro) e um visto quando você o tem.
- **Teclas.** As setas, Page Up, Page Down, Home e End percorrem a lista, e `Enter` passa para o diagrama. `Alt+Left` e `Alt+Right` voltam e avançam pelos itens que você abriu.

## O diagrama {#the-chart}

Clique em um item e o lado direito o mostra. No alto ficam a imagem, o nome, a raridade e o tipo dele, e um chip para cada **caminho** de obtê-lo: **Criar** (na Montagem, com seu tempo e seu custo), **Comprar** (na Loja, com seu preço), **Prensar** (a partir de minério, na Forja do Skylab), **Drop** (o mundo dá: alienígenas, rochas, recompensas) e **Produzir** ([Dark Matter](/wiki/03-Mechanics/Dark-Matter.md), a partir de N.I.K.E.s disparados no buraco negro). O chip preenchido é o caminho que o diagrama e o custo seguem; clique em outro chip para seguir aquele. Se você não pesquisou o que permite criar o item, uma linha diz qual tecnologia é necessária e quanto tempo ela leva, com um botão que abre a Pesquisa.

O **Diagrama** desenha o item como uma árvore da esquerda para a direita: o item à esquerda, o que o compõe à direita dele, até as matérias-primas.

- Cada caixa mostra o item, quantos você precisa e um símbolo de como ele é obtido (o do chip desse caminho, acima; passe o mouse sobre a caixa para ver as palavras, assim a cor nunca é o único sinal). Um cadeado diz que a tecnologia dele ainda não foi pesquisada, e um visto verde com um número diz quantos você tem.
- Uma caixa com ramos tem uma pequena alça que os recolhe; os ramos profundos de uma árvore grande começam recolhidos. **Expandir tudo**, **Recolher tudo**, **Ajustar** e os botões de zoom ficam acima do diagrama.
- Clique em uma caixa para ler a ficha dela sob o diagrama: o item, os caminhos para obtê-lo (clique em outro chip para seguir esse caminho), o que o caminho pede (as rodadas, o tempo e o custo de uma criação, ou o preço na Loja), quantos você tem e, em uma caixa bloqueada, a tecnologia de que ela precisa. Um clique duplo, ou `Enter`, abre esse item no Livro de receitas. As setas passam de caixa em caixa, `Space` recolhe ou abre um ramo e `0` ajusta o diagrama. Role para se mover; `Ctrl` e a roda do mouse dão zoom.
- Um item que só se compra ou se encontra é uma caixa única que diz “Nada para criar: compra-se ou encontra-se. Veja Fontes.”

Em uma janela larga o diagrama ocupa a esquerda e os outros painéis ficam em uma coluna à direita dele; em uma estreita, as abas **Diagrama**, **Etapas**, **Custo**, **Fontes** e **Usado em** mostram um painel de cada vez.

## Etapas e custo {#steps-and-the-bill}

Sob o cabeçalho, três controles decidem o que é contado: **Quantos** exemplares você quer, **Contar o que tenho** (ligado: o que você já tem é descontado) e **Incluir o que está equipado** (desligado: uma peça equipada em uma nave não é contada, porque melhorar consome uma peça e uma equipada deixaria o seu slot).

- **Etapas** é o diagrama como uma lista numerada, na ordem em que se faz, em grupos: Pesquisar, Obter, Comprar, Prensar e criar, e Do seu estoque. A pesquisa vem primeiro porque a Montagem não cria nada antes que a tecnologia seja pesquisada. Cada etapa diz o que e quantos, quanto custa e quanto tempo leva, e uma etapa Obter pode mostrar onde obter. **Copiar etapas** copia a lista como texto.
- **Custo** soma tudo: seus Credits e seu Thulium frente ao que você tem, cada matéria-prima com o que **Precisa**, o que **Tem** e o que **Falta**, o Dark Matter que a pesquisa consome, o tempo de criar e prensar, o tempo de pesquisar (uma tecnologia por vez) e um **Valor**. O Valor é um jeito de comparar dois caminhos para obter um item, com o Thulium e as coisas que você precisa encontrar contados em Credits: não é um preço. **Copiar custo** copia o custo como uma tabela que você pode colar em um chat ou em uma nota.

## Fontes e Usado em {#sources-and-used-in}

- **Fontes** diz onde o mundo dá o item e cada matéria-prima de que o plano precisa, por tipo: alienígenas, asteroides e rochas, enxames, o Dormant Swamp, guardiões do clã, [Davidski](/wiki/03-Mechanics/Davidski.md), expedições do Skylab, a escavadeira gigante, produção do Skylab, missões, Convidar amigos e o pacote inicial. Uma linha nomeia quem dá e onde, a chance e quantos. “Também em” lista o [Leilão](/wiki/03-Mechanics/Auction.md), o estoque do Davidski e outros pilotos. Uma chance é uma chance, não um ritmo por hora: quanto tempo leva uma destruição depende de você.
- **Usado em** lista os itens que são criados com este. Clique em um para abri-lo.

## Adicionar ao build {#add-to-build}

Um item que fica em um slot ou que se leva consigo tem um botão **Adicionar ao build**: naves, blindagens de casco, lasers, amplificadores, escudos, células, motores, propulsores, Adaptive Cores, extras, drones, formações, munição, foguetes e a EMP Charge. Ele coloca o item no build que você está editando em **Builds**, no primeiro lugar onde cabe (se não houver nenhum, um build novo chamado “Novo build” é criado), e uma mensagem diz para onde ele foi ou por que não coube (“Escolha uma nave primeiro.”). Adicionar uma nave a um build que já tem uma pede que você clique de novo para substituí-la. A EMP Charge é levada, não equipada: ela vai para os foguetes do build.

## Builds

Um **build** é o equipamento de uma nave, escrito com nomes de itens para que signifique o mesmo em todo servidor: a nave, os lasers com seus amplificadores, os escudos, motores e Adaptive Cores com suas células e propulsores, os extras, as peças dos slots de habilidade, as blindagens de casco, os drones com o que levam, uma formação, e a munição e os foguetes a levar. Ele também tem um nome, uma nota, uma fase (Início, Meio ou Fim) e um tipo.

A lista à esquerda tem as **Predefinições** por fase, **Meus builds**, **Novo build** e **Importar**; em uma janela estreita é uma fileira de abas. Escolha um build e você vê o painel dele, as estatísticas e o custo.

### Importar {#import}

**Importar** abre uma folha com três portas:

- **Colar**: cole o texto de um build ou aperte **Colar da área de transferência**.
- **De um arquivo**: os arquivos de build da pasta `exports` da pasta de dados do jogo (`.spacecorps2027` na sua pasta pessoal), a mesma pasta em que **Salvar em arquivo** grava.
- **Do meu hangar**: escolha uma das suas naves e uma configuração, e o jogo lê o que está equipado: lasers e amplificadores, geradores com suas células e propulsores, extras, peças de habilidade, blindagens de casco, drones com o que levam e o nível da sua Extra Slots CPU. Ele também oferece a formação, a munição e os foguetes da sua barra de atalhos; marque os que você quiser.

Você vê o que entra antes de qualquer coisa ser salva, e o jogo diz exatamente o que não conseguiu importar: um item que não existe neste jogo, uma peça que não vai no seu lugar, mais peças do que a nave tem slots, um build feito por um jogo mais novo. **Importado sem alterações** significa que tudo entrou. Depois, **Salvar em Meus builds**, **Abrir no editor**, ou feche a folha. Seus níveis da [Forja](/wiki/06-Items/Forge.md), os bônus da Forja, os níveis dos drones, os boosters, o P.E.T., a aparência da sua nave e a outra configuração do [Hangar](/wiki/03-Mechanics/Hangar.md) não fazem parte de um build (importe a outra configuração como um segundo build).

### As 15 predefinições {#the-15-presets}

Quinze builds estão prontos para usar: três fases do jogo, **Início**, **Meio** e **Fim**, com cinco tipos em cada uma. **Farm** consegue mais destruições pelo que custa, **Defesa** tem o maior escudo e a regeneração mais rápida, **Ataque** o maior dano e a maior penetração, **Situacional** escolhe seus combates com camuflagem, saltos e velocidade, e **Tanque** tem o casco e o escudo mais altos juntos. Uma predefinição não pode ser alterada: **Editar uma cópia** a abre como um rascunho seu, e **Adicionar a Meus builds** a guarda como está. Cada linha mostra o Valor em poucos caracteres, calculado a partir das receitas enquanto você olha; abra uma predefinição para ver suas estatísticas e seu custo.

### Editar {#edit}

Um build é desenhado como um hangar: lasers, geradores, extras, habilidades, blindagens e drones, depois o nível da Extra Slots CPU, uma formação e a munição e os foguetes a levar. Clique em um slot vazio e uma lista mostra só o que cabe nele, com o preço ou o caminho para obtê-lo; clique em uma peça para **Substituir**, **Adicionar um módulo** ou **Remover**. Um drone leva um laser ou um núcleo de escudo. Se você troca a nave, as peças que ainda cabem ficam, e o resto aparece na lista como removido. Dê ao build um nome, uma fase, um tipo e uma nota, e depois **Salvar**, **Salvar como cópia**, **Excluir** ou **Fechar** (Fechar pergunta antes quando há alterações não salvas).

### Estatísticas {#stats}

Sob o painel fica a ficha de estatísticas do hangar: pontos de vida, dano, alcance, chance crítica, escudos e sua recarga, absorção, velocidade, bônus de escudo e de velocidade, penetração e, em uma nave com slots de blindagem, o casco que as blindagens dela somam. A ficha não tem linhas para habilidades: as peças dos slots de habilidade ficam no painel. O servidor calcula os números com o mesmo código do seu hangar, para um build que não está equipado em nenhuma nave. Duas chaves definem o **Nível da Forja** e o **Nível dos drones** que os números supõem. Uma formação age em voo, então aparece como texto e não entra nos números, e os boosters e os seus próprios níveis da Forja também não.

### Custo {#cost}

O custo tem quatro blocos:

- **Totais**: Credits, Thulium, Dark Matter, cada matéria-prima com Precisa, Tem e Falta, os tempos e o Valor. **Você ainda precisa de** é o que sobra depois de descontar o que você tem.
- **Para onde vai o dinheiro**: cada peça, a mais cara primeiro.
- **Passos**: pesquisar, obter, comprar, prensar e criar, em ordem, para o build inteiro. Clique em um passo Obter para ver onde o mundo o dá, ou abra o item no Livro de receitas.
- **Antes de começar**: o que não é uma peça, como os níveis da Extra Slots CPU, a pesquisa dos slots de blindagem, os drones que você ainda precisa comprar e o nível do Núcleo do Skylab que a Forja exige.

Três chaves: **Descontar o que tenho** (ligada), **Incluir o que está equipado** (desligada) e **Incluir munição e foguetes** (desligada: eles se gastam o tempo todo, então não são o preço do build).

## Salvos na sua conta {#saved-on-your-account}

**Meus builds são salvos na sua conta**, no servidor e não neste computador, para que sigam você a qualquer computador. Você pode guardar até 50; a lista mostra quantos você tem e, quando está cheia, a página pede que você exclua um para salvar outro. Um build está salvo quando o servidor diz que está: a página mostra **Salvando...** enquanto espera, e se o servidor recusa ou não pode ser alcançado, ela diz por quê e o build continua sem salvar, com suas alterações ainda no editor. Um build salvo é só nomes de itens, alguns rótulos e o nome e a nota que você digitou, e nenhum outro piloto pode vê-lo. Para dar um a um amigo, exporte-o.

## Compartilhar e exportar {#share-and-export}

**Exportar** em um build abre uma folha com o build como texto (JSON). **Copie-o** para colar em um chat, ou use **Salvar em arquivo**, que grava `spacecorps-build-<name>.json` na pasta `exports` e nunca sobrescreve um arquivo mais antigo. Um amigo cola o texto em **Importar › Colar**, ou põe o arquivo na própria pasta `exports` e o escolhe em **De um arquivo**. O texto contém os nomes dos itens do equipamento, a nave e o nome e a nota do build, e nada da sua conta.

## Dicas {#tips}

1. **Olhe antes de farmar.** Abra um item no Livro de receitas e leia as Fontes e as Etapas dele antes de passar um dia em um drop que não é o que você precisa.
2. **Conte do zero.** Desligue **Contar o que tenho** (em Builds: **Descontar o que tenho**) para ver o que um item ou um build custa do zero; deixe ligado para ver o que você ainda precisa.
3. **Comece por uma predefinição.** **Editar uma cópia**, troque uma peça, e as estatísticas e o custo acompanham.
4. **Leia também as árvores.** As [Árvores de itens](/wiki/06-Items/Item-Trees.md) mostram cada tipo de item lado a lado, e o Livro de receitas calcula o preço de qualquer um deles para você.
