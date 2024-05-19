import scrapy

class AitoolsSpider(scrapy.Spider):
    name = "aitools"
    allowed_domains = ["futuretools.io"]
    start_urls = ["https://futuretools.io"]

    def parse(self, response):
        tool_detail = []
        number_of_tools = 0
        cards = response.css("div.tool-item-columns-new")
        
        for tool in cards:
            tool_info = {
                'tool_link': tool.css('a.tool-item-link-block---new::attr(href)').get(),
                'image_src': tool.css('.tool-item-image---new::attr(src)').get(),
                'tool_name': tool.css('.tool-item-link---new::text').get(),
                'description': tool.css('.tool-item-description-box---new::text').get(),
                'category': tool.css('.text-block-53::text').get(),
            }
            tool_detail.append(tool_info)
            number_of_tools += 1

        for detail in tool_detail:
            self.log(detail)

        next_page = response.css('a.next::attr(href)').get()
        if next_page:
            yield response.follow(next_page, self.parse)
        print(f"Number of ai tools: {len(tool_detail)}")
