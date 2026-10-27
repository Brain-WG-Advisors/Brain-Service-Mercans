# Consulta ao Держстат — 1-ПВ (місячна / квартальна), 3 pontos abertos (SR-414 / SR-415)

> Rascunho para o usuário (ou a Altium) enviar. Nada foi enviado.

## Onde conseguir a resposta

| O quê | Link | Para quê |
|---|---|---|
| Кабінет респондента (precisa do КЕП da Altium) | https://statzvit.ukrstat.gov.ua | **Caminho mais rápido:** abrir um rascunho do 1-ПВ (місячна) da Altium e ver o que o portal preenche sozinho em OBL, RAY, КВЕД e NOMER (o formulário diz que o КАТОТТГ e o КВЕД "визначається автоматично" e a lista técnica diz que OBL/RAY vêm "з картки підприємства"). Responde os pontos 1 e 2 para a Altium. |
| Contato oficial do Держстат para desenvolvedores de software de e-reporting | coez@ukrstat.gov.ua · (044) 201-67-07 (página oficial https://ukrstat.gov.ua/elektr_zvit/po.htm, modificada em 07.10.2025) | Pontos 1, 2 e 3 (formato XML e diretórios). |
| Página oficial "Інформація для розробників" | https://ukrstat.gov.ua/elektr_zvit/po.htm | Conferir se há diretório SPR_SSCU novo. |
| Diretório de órgãos estatísticos publicado (2016) | https://www.ukrstat.gov.ua/elektr_zvit/po_doc/spr_sscu_2016.ZIP | Ponto 3 (é o único publicado). |
| ГУС у м. Києві (órgão ao qual a Altium entrega) | http://www.kyiv.ukrstat.gov.ua | Consulta metodológica local (pontos 1 e 2). |

Observação: esses sites não abrem a partir desta máquina (nem pelo Chrome); devem abrir de uma rede ucraniana ou da Altium.

## Texto da consulta (ucraniano)

> Шановні колеги,
>
> просимо роз'яснити заповнення електронних звітів за формами № 1-ПВ (місячна), шаблон S0301016, та № 1-ПВ (квартальна), шаблон S0301121, для юридичної особи без відокремлених структурних підрозділів (номер структурного підрозділу = 1):
>
> 1. Чи потрібно заповнювати елемент KVED (S0301016) / N2 (S0301121) — «Код виду економічної діяльності за КВЕД структурного підрозділу», якщо номер структурного підрозділу (NOMER) = 1? Контроль 3 шаблону S0301016 (контроль 4 шаблону S0301121) вимагає його заповнення без умови, а контроль 2 (контроль 3) пов'язує поля структурного підрозділу з номером > 1.
> 2. Як визначається тризначний код RAY («Код району відповідно до КАТОТТГ») для м. Київ (місто зі спеціальним статусом, код КАТОТТГ UA80000000000093317)?
> 3. Чи чинний довідник органів державної статистики SPR_SSCU.XML у редакції 2016 року (spr_sscu_2016.ZIP) для заповнення елементів C_REG і C_RAJ заголовка (Формат 3.1, таблиця 1)? Якщо ні, просимо надати чинну редакцію.
>
> Дякуємо.

## Tradução (para conferência)

1. É preciso preencher o KVED (S0301016) / N2 (S0301121), "código КВЕД da subdivisão", quando NOMER = 1? O controle 3 (mensal) / 4 (trimestral) exige sem condição; o controle 2 / 3 liga os campos da subdivisão a NOMER > 1.
2. Como se determina o código RAY de 3 dígitos para Kyiv (cidade com status especial, КАТОТТГ UA80000000000093317)?
3. O diretório SPR_SSCU.XML de 2016 continua vigente para C_REG e C_RAJ (Format 3.1, tabela 1)? Se não, qual é o vigente?
