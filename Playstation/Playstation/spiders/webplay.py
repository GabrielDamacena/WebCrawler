import scrapy
from Playstation.items import PlaystationItem

class WebplaySpider(scrapy.Spider):
    name = "webplay"
    allowed_domains = ["playstation.com"]
    start_urls = ["https://store.playstation.com/pt-br/category/dc464929-edee-48a5-bcd3-1e6f5250ae80/1"]

    def start_requests(self):
        # Adicionando um cabeçalho User-Agent
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
        }
        for url in self.start_urls:
            yield scrapy.Request(url, headers=headers, callback=self.parse)

    def parse(self, response):
        if response.status != 200:
            self.log(f'Erro ao acessar a página: {response.status}')
            return
        
        # Log da URL visitada
        self.log(f'URL visitada: {response.url}')

        # Mantendo rastreamento de jogos e preços únicos
        jogos_precos = {}
        jogos_unicos = set()  # Conjunto para rastrear jogos únicos

        # Exemplo: extraindo títulos de jogos ou conteúdos da página
        titles = response.xpath('//span[@class="psw-t-body psw-c-t-1 psw-t-truncate-2 psw-m-b-2"]/text()').getall()
        prices = response.xpath('//span[@class="psw-m-r-3"]/text()').getall()

        for title, price in zip(titles, prices):
            title = title.strip()
            price = price.strip()
            
            # Verificando se o título já foi processado
            if title not in jogos_unicos:
                jogos_unicos.add(title)  # Adiciona o título ao conjunto para evitar repetição
                jogos_precos[title] = price
                self.log(f'Título encontrado: {title}')  # Log do título encontrado
                yield {'jogo': title, 'preco': price}  # Usando um dicionário para gerar itens

        # Se houver uma próxima página, seguir o link
        next_page = response.xpath('//a[@class="pagination-next"]/@href').get()
        if next_page:
            yield response.follow(next_page, self.parse)
