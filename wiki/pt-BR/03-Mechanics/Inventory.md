<!-- wiki-i18n source: 5874d77ba7ccf380 -->
<!-- wiki-i18n title: Inventário -->
# Inventário e equipamento {#inventory-equipment}

O hangar permite que você gerencie suas naves e seu equipamento. Equipar bem os itens é a chave para sobreviver e dominar. Você pode fazer isso na estação e, em voo, de dentro de uma zona segura: veja [O hangar em voo](/wiki/03-Mechanics/Hangar.md).

## Slots de equipamento e eficiência dos atributos {#equipment-slots-stat-efficiencies}

Ao contrário dos jogos espaciais tradicionais, o SpaceCorps tem slots de equipamento em faixas dinâmicas, que ajustam a eficácia dos módulos encaixados.

- **Slots de laser**: para armas ofensivas (lasers). Eles sempre operam com **100% do dano e do alcance**.
- **Slots de gerador**: slots compartilhados para escudos, motores e núcleos adaptativos. Eles se dividem em três faixas de eficiência, e a faixa decide quanto dos atributos básicos de um item conta. No hangar, cada faixa tem um (i) ao lado do nome que a explica:
  - **Slots de núcleo**: os itens colocados aqui recebem **100%** dos atributos básicos. Toda nave os tem: coloque aqui os seus melhores escudos e motores.
  - **Slots de suporte**: os itens colocados aqui recebem **75%** dos atributos básicos (por exemplo, 75% da velocidade ou da capacidade do escudo). Toda nave os tem.
  - **Slots auxiliares**: os itens colocados aqui recebem **50%** dos atributos básicos. Só algumas naves os têm (a Paragon tem 2, a Ironclad 3 e a Wraith 4; a Protos, a Kitefin e a Ostirion não têm nenhum). Eles servem melhor para escudos e motores extras, mais fracos, enquanto os seus mais fortes vão nos slots de núcleo.
  - **Slots de drone**: um escudo em um dos seus drones conta como um em um slot de núcleo, **100%** dos atributos dele (veja [Mecânica dos drones](/wiki/03-Mechanics/Drones.md)).
  - **Slots não atribuídos/legados**: os itens colocados aqui não contribuem para os atributos.
  - **O empilhamento também perde força**: escudos e motores são ordenados do mais forte ao mais fraco, e a parcela da faixa é então multiplicada pela da posição deles: do 1º ao 4º contam por inteiro, o 5º, o 6º e o 7º contam 85%, 70% e 55%, e do 8º em diante contam 50% nos escudos e 25% nos motores. Veja [Escudos](/wiki/03-Mechanics/Shields.md) e [Velocidade](/wiki/03-Mechanics/Speed.md).
- **Slots extras**: para itens utilitários especializados, como os drones de reparo.

## Ordem do inventário {#inventory-order}

O inventário lista seus itens na mesma ordem da Loja, seja qual for a ordem em que você os comprou, criou ou encontrou. As categorias que combinam ficam juntas: lasers, amplificadores de laser e munição de laser; escudos e células de escudo; motores e propulsores; núcleos adaptativos; extras (drones de reparo); drones; e, por fim, recursos. Dentro de uma categoria vem primeiro o mais barato (créditos antes de Thulium) e depois o que não tem preço: o equipamento “só por criação” e os itens de saque, da raridade mais fraca para a mais forte (lasers de uma mesma raridade, do dano mais fraco para o mais forte). A munição de laser vai de x1 a x4 e, depois, vem a Siphon Battery. Os foguetes seguem o tipo (alvo único antes de explosão em área, guiado antes de reto) e depois o grau, então o foguete Épico, que custa Thulium, vem por último no seu tipo. As cópias de um mesmo item seguem o grau de encantamento. Acima da grade, um botão por categoria usa a mesma ordem, cada um com o número de itens que a busca encontra nela. Cada botão liga ou desliga sozinho, então você pode ocultar a munição e os drones de reparo enquanto trabalha com lasers, escudos e motores: clique em um botão para mostrar ou ocultar a categoria dele, use Shift+clique (ou clique duplo) para deixar ligada só essa categoria e clique nele de novo para trazer o resto de volta. **Todas** mostra todas as categorias e **Nenhuma** oculta todas, para você ligar só as que quiser. Um botão riscado está desligado; um botão com uma marca de seleção está ligado. A busca funciona nas categorias que estão ligadas, e a sua escolha fica guardada junto com o seu piloto. Se tudo estiver oculto, a grade avisa e oferece **Mostrar todas as categorias**.

## Equipar item em item (subslots) {#item-to-item-equipping-sub-sockets-}

Alguns itens principais podem “equipar” itens de apoio secundários (o chamado subslot) para ampliar seus parâmetros. Para usar um subslot, arraste o item de apoio diretamente sobre o item principal no inventário do seu hangar.

### Tabela de compatibilidade {#compatibility-table}

| Item principal | Itens aceitos no subslot | Efeito resultante |
| :--- | :--- | :--- |
| **Laser** | Amplificador de laser (amp.) | Aumenta o dano base e os atributos de acerto crítico |
| **Escudo** | Célula de escudo | Aumenta a capacidade do escudo e a taxa de recarga |
| **Motor** | Propulsor | Aumenta a velocidade do motor e os multiplicadores |
| **Gerador híbrido** | Célula de escudo OU propulsor | Aumenta a capacidade do escudo, a taxa de recarga ou a velocidade |
| **Drone** | Laser ou escudo, em cada um dos seus slots (um Master Drone tem dois) | Um laser soma o dano dele à sua rajada; um escudo conta como um em um slot de núcleo (100% dos atributos dele) |

---

## Gerenciamento de munição {#ammo-management}

A munição de laser é um recurso consumível.
- A munição se acumula em pilhas no seu inventário.
- Você pode trocar a munição de laser ativa pela barra de atalhos do HUD.
- Munição de melhor qualidade dá multiplicadores de dano (por exemplo, Standard Battery x1, Advanced Plasma x2, Ultra Core x3, Experimental Fusion Core x4). A Siphon Battery causa dano x1 apenas aos escudos e o entrega ao seu.
