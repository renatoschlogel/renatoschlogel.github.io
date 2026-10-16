# Renato Welinton Schlogel — currículo público

Website bilíngue para apresentação profissional, preparado para GitHub Pages.

- Inglês: <https://renatoschlogel.github.io/>
- Português: <https://renatoschlogel.github.io/pt-br/>

## Conteúdo e manutenção

O conteúdo público dos dois idiomas fica em `content/resume.json`. Depois de editar, gere as páginas:

```bash
python3 scripts/build.py
```

Versione também os HTMLs gerados. O GitHub Pages serve os arquivos estáticos; Python é necessário apenas para regenerar o conteúdo localmente, sem dependências externas.

```text
content/resume.json   conteúdo profissional e traduções
scripts/build.py     gerador com a biblioteca padrão do Python
index.html           página em inglês
pt-br/index.html     página em português
assets/style.css     layout responsivo e estilos de impressão
assets/site.js       botão de impressão
assets/favicon.svg   ícone do site
sitemap.xml          URLs e alternativas de idioma
robots.txt           referência ao sitemap
.nojekyll            publicação estática sem processamento Jekyll
```

## Visualizar localmente

```bash
python3 -m http.server 8000
```

Abra <http://localhost:8000/> ou <http://localhost:8000/pt-br/>. Navegação, conteúdo e idiomas funcionam sem JavaScript; JavaScript habilita o botão de impressão.

## Publicar no GitHub Pages

1. Revise as páginas e faça commit/push dos arquivos para `main`.
2. No GitHub, abra **Settings → Pages**.
3. Em **Build and deployment**, selecione **Deploy from a branch**.
4. Escolha a branch **main** e a pasta **/ (root)**; salve.
5. Aguarde o processamento do GitHub Pages e acesse o endereço do site.

O projeto não exige instalação de pacotes, um framework ou workflow de build personalizado. O endereço final depende de o GitHub Pages estar habilitado para este repositório.

## Impressão e PDF

Na página do idioma desejado, use **Imprimir / salvar PDF** ou a impressão do navegador. Os estilos de impressão removem navegação e elementos decorativos e usam uma coluna com texto selecionável. Para exportar, selecione A4, escala 100% e desative os cabeçalhos/rodapés automáticos do navegador.

A paginação pode variar conforme navegador e configurações. Confira o PDF antes de enviar a recrutadores; o botão abre a impressão, não baixa um PDF previamente gerado.

## Critérios editoriais

- Posicionamento geral: engenharia backend Java/Spring Boot, liderança técnica e conhecimento de negócio financeiro e de saúde.
- Experiências em ordem cronológica inversa, decisões técnicas e resultados verificáveis.
- Go e .NET como experiências complementares; Progress no histórico profissional.
- IA generativa e agentes de codificação descritos sem marcas de ferramentas.
- Mensageria descrita como atuação em avaliação e especificação. Kafka aparece como avaliação de desenho; implementação futura não é apresentada como entrega concluída.
- Contatos públicos: e-mail profissional, LinkedIn e GitHub; localização limitada a Brasil e fuso horário.
- HTML semântico, navegação por teclado, links de idioma explícitos, metadados de busca e layout responsivo. Fontes do sistema e nenhuma dependência de serviços externos para carregar o conteúdo.

## Referências da pesquisa

- [Harvard Extension School — currículos concisos, específicos e baseados em evidências](https://careerservices.fas.harvard.edu/resources/hes-create-impactful-resumes-and-cover-letters/)
- [Google Search Central — versões de idioma em URLs próprias e navegação explícita](https://developers.google.com/search/docs/specialty/international/managing-multi-regional-sites)
- [W3C WAI — idioma principal da página](https://www.w3.org/WAI/WCAG21/Understanding/language-of-page)
- [GitHub Docs — criação e publicação de um GitHub Pages](https://docs.github.com/en/pages/getting-started-with-github-pages/creating-a-github-pages-site)

Não há um padrão internacional único de currículo: o formato deve ser adaptado ao mercado e à oportunidade. Esta página é uma apresentação geral; candidaturas para vagas específicas continuam exigindo seleção de experiências e ênfase próprias.
