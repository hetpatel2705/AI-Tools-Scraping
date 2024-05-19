import scrapy

class ToolsSpider(scrapy.Spider):
    name = "tools"
    allowed_domains = ["futuretools.io"]
    start_urls = ["https://futuretools.io"]

    def parse(self, response):
        tool_detail = []

        # Selecting the cards using the appropriate CSS selector
        cards = response.css("div.tool-item-columns-new")
        
        # Iterating through each card and extracting the required information
        for tool in cards:
            tool_info = {
                'tool_link': tool.css('a.tool-item-link-block---new::attr(href)').get(),
                'image_src': tool.css('.tool-item-image---new::attr(src)').get(),
                'tool_name': tool.css('.tool-item-link---new::text').get(),
                'description': tool.css('.tool-item-description-box---new::text').get(),
                'category': tool.css('.text-block-53::text').get(),
            }
            tool_detail.append(tool_info)

        # Printing the extracted tool details to the console
        for detail in tool_detail:
            self.log(detail)

        # Save the extracted details to a file
        with open('file.txt', 'a') as f:
            for detail in tool_detail:
                f.write(f"{detail}\n")

        # Identify and follow the "Next" page link
        next_page = response.css('a.next::attr(href)').get()
        if next_page:
            yield response.follow(next_page, self.parse)
        
        # Print the number of AI tools to the console
        print(f"Number of AI tools: {len(tool_detail)}")
