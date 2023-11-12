 E1 - **Apresente a query para listar todos os livros publicados após 2014. Ordenar pela coluna cod, em ordem crescente, as linhas. Atenção às colunas esperadas no resultado final: cod, titulo, autor, editora, valor, publicacao, edicao, idioma.**

 select * <br>
 from livro<br>
 where publicacao >= '2015-01-01'<br>
 order by cod<br>

#

 E2 - **Apresente a query para listar os 10 livros mais caros. Ordenar as linhas pela coluna valor, em ordem decrescente.  Atenção às colunas esperadas no resultado final:  titulo, valor.**

 select titulo, valor<br>
 from livro<br>
 order by valor desc<br>
 limit 10<br>

#

 E3 - **Apresente a query para listar as 5 editoras com mais livros na biblioteca. O resultado deve conter apenas as colunas quantidade, nome, estado e cidade.Ordenar as linhas pela coluna que representa a quantidade de livros em ordem decrescente.**

 select editora.nome, endereco.estado, endereco.cidade, count(*) as quantidade<br>
 from livro inner join editora on editora=codEditora<br>
 inner join endereco on endereco=codEndereco<br>
 group by editora.nome, endereco.estado, endereco.cidade<br>
 order by quantidade desc<br>
 limit 5<br>

#

 E4 - **Apresente a query para listar a quantidade de livros publicada por cada autor. Ordenar as linhas pela coluna nome (autor), em ordem crescente. Além desta, apresentar as colunas codautor, nascimento e quantidade (total de livros de sua autoria).**

 select  a.nome, a.codAutor, a.nascimento, coalesce(count (l.cod),0) as quantidade<br>
 from livro l right join autor a on l.autor=a.codAutor<br>
 group by a.codAutor, a.nascimento, a.nome<br>
 order by a.nome<br>

#

 E5 - **Apresente a query para listar o nome dos autores que publicaram livros através de editoras NÃO situadas na região sul do Brasil. Ordene o resultado pela coluna nome, em ordem crescente. Não podem haver nomes repetidos em seu retorno.**

 select distinct a.nome<br>
 from autor a inner join livro l on l.autor=a.codAutor <br>
 inner join editora e on e.codEditora=l.editora <br>
 left join endereco en on en.codEndereco=e.endereco <br>
 where en.estado not in ('RIO GRANDE DO SUL','PARANÁ') <br>
 order by a.nome <br>

#

 E6 - **Apresente a query para listar o autor com maior número de livros publicados. O resultado deve conter apenas as colunas codautor, nome, quantidade_publicacoes.**

 select a.codAutor, a.nome, count(*) as quantidade_publicacoes<br>
 from livro l inner join autor a on l.autor=a.codAutor<br>
 group by a.nome, a.codAutor<br>
 order by quantidade_publicacoes desc<br>
 limit 1<br>

#

 E7 - **Apresente a query para listar o nome dos autores com nenhuma publicação. Apresentá-los em ordem crescente.**

 select a.nome <br>
 from livro l right join autor a on l.autor=a.codAutor <br>
 where l.cod is null <br>
 group by a.nome <br>

# 

 E8 - **Apresente a query para listar o código e o nome do vendedor com maior número de vendas (contagem), e que estas vendas estejam com o status concluída.  As colunas presentes no resultado devem ser, portanto, cdvdd e nmvdd.**

 select v.cdvdd, nmvdd <br>
 from tbvendedor v left join tbvendas ven on v.cdvdd=ven.cdvdd <br>
 where status = 'Concluído' and (select count(qtd) from tbvendas) <br>
 group by v.cdvdd, nmvdd <br>
 order by count(qtd) desc <br>
 limit 1 <br>

#
 
 E9 - **Apresente a query para listar o código e nome do produto mais vendido entre as datas de 2014-02-03 até 2018-02-02, e que estas vendas estejam com o status concluída. As colunas presentes no resultado devem ser cdpro e nmpro.**

 select cdpro, nmpro <br>
 from tbvendas<br>
 where status = 'Concluído' <br>
 and dtven between '2014-02-03' and '2018-02-02' <br>
 group by cdpro, nmpro <br>
 limit 1 <br>

#

 E10 - **A comissão de um vendedor é definida a partir de um percentual sobre o total de vendas (quantidade * valor unitário) por ele realizado. O percentual de comissão de cada vendedor está armazenado na coluna perccomissao, tabela tbvendedor. Com base em tais informações, calcule a comissão de todos os vendedores, considerando todas as vendas armazenadas na base de dados com status concluído. As colunas presentes no resultado devem ser vendedor, valor_total_vendas e comissao. O valor de comissão deve ser apresentado em ordem decrescente arredondado na segunda casa decimal.**

 select tbv.nmvdd as vendedor, sum(vnd.qtd*vnd.vrunt) as valor_total_vendas, <br>
 round(sum((vnd.qtd*vnd.vrunt)*tbv.perccomissao)/100,2) as comissao <br>
 from tbvendedor tbv inner join tbvendas vnd on tbv.cdvdd=vnd.cdvdd <br>
 where vnd.status='Concluído' <br>
 group by tbv.nmvdd <br>
 order by comissao desc <br>

#

 E11 - **Apresente a query para listar o código e nome cliente com maior gasto na loja. As colunas presentes no resultado devem ser cdcli, nmcli e gasto, esta última representando o somatório das vendas (concluídas) atribuídas ao cliente.**

 select distinct cdcli, nmcli, sum(vrunt*qtd) as gasto <br>
 from tbvendas <br>
 where status = 'Concluído' <br>
 group by nmcli <br>
 order by gasto desc <br>
 limit 1 <br>

#

 E12 - **Apresente a query para listar código, nome e data de nascimento dos dependentes do vendedor com menor valor total bruto em vendas (não sendo zero). As colunas presentes no resultado devem ser cddep, nmdep, dtnasc e valor_total_vendas. Observação: Apenas vendas com status concluído.**

 select td.cddep, td.nmdep, td.dtnasc, sum(tvd.qtd*tvd.vrunt) as valor_total_vendas <br>
 from tbvendas tvd inner join tbvendedor tv on tv.cdvdd = tvd.cdvdd <br>
 inner join tbdependente td on tvd.cdvdd = td.cdvdd <br>
 where tvd.status = 'Concluído' <br>
 group by td.cddep <br>
 having valor_total_vendas > 0 <br>
 order by valor_total_vendas <br>
 limit 1 <br>

#

 E13 - **Apresente a query para listar os 10 produtos menos vendidos pelos canais de E-Commerce ou Matriz (Considerar apenas vendas concluídas). As colunas presentes no resultado devem ser cdpro, nmcanalvendas, nmpro e quantidade_vendas.**

 select cdpro, nmcanalvendas, nmpro, sum(qtd) as quantidade_vendas <br>
 from tbvendas <br>
 where nmcanalvendas in ('Matriz','Ecommerce') and status = 'Concluído' <br>
 group by nmcanalvendas, nmpro <br>
 order by quantidade_vendas <br>
 limit 10 <br>

#

 E14 - **Apresente a query para listar o gasto médio por estado da federação. As colunas presentes no resultado devem ser estado e gastomedio. Considere apresentar a coluna gastomedio arredondada na segunda casa decimal e ordenado de forma decrescente. Observação: Apenas vendas com status concluído.**

 select estado, round(avg(qtd*vrunt),2) as gastomedio <br>
 from tbvendas <br>
 where status = 'Concluído' <br>
 group by estado <br>
 order by gastomedio desc <br>

#

 E15 - **Apresente a query para listar os códigos das vendas identificadas como deletadas. Apresente o resultado em ordem crescente.**

 select cdven <br>
 from tbvendas <br> 
 where deletado > 0 <br>

#

 E16 - **Apresente a query para listar a quantidade média vendida de cada produto agrupado por estado da federação. As colunas presentes no resultado devem ser estado e nmprod e quantidade_media. Considere arredondar o valor da coluna quantidade_media na quarta casa decimal. Ordene os resultados pelo estado (1º) e nome do produto (2º). Obs: Somente vendas concluídas.**

 select estado, nmpro, round(avg(qtd),4) as quantidade_media <br>
 from tbvendas <br> 
 where status = 'Concluído' <br>
 group by estado,nmpro <br>
 order by estado, nmpro <br>