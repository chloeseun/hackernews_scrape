from bs4 import BeautifulSoup
html_doc = """
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <meta http-equiv="X-UA-Compatible" content="ie=edge" />
    <title>My Web</title>
  </head>
  <body>
    <div id="section_1">
      <h3 data-hello="hi">Hi</h3>
      <!-- <img src="" alt=""> -->
      <p>Lorem, ipsum dolor sit amet consectetur adipisicing elit. Rem adipisci inventore doloribus nesciunt molestiae consectetur? Quasi, quas. In maxime at quasi saepe sit ex nulla, excepturi fugit eos, facere eaque!</p>
    </div>

    <div id="section_2">
      <ul class="items">
         <li class="item"><a href="#">Item1</a></li>
         <li class="item"><a href="#">Item2</a></li>
         <li class="item"><a href="#">Item3</a></li>
         <li class="item"><a href="#">Item4</a></li>
         <li class="item"><a href="#">Item5</a></li>
      </ul>
    </div>
  </body>
</html>
"""

soup = BeautifulSoup(html_doc, 'html.parser')

# Direct
# print(soup.body)
# print(soup.head)

# find()
# el = soup.find('div')
# el = soup.find(id='section_1')
# el = soup.find(class_='items')

# findAll() // returns a list
# el = soup.findAll('div')[1]

# select() // returns a list
# el = soup.select('#section_2')
# el = soup.select('#section_2')[0]

# get_text()
# el = soup.find(class_='item').get_text()

# for item in soup.select('.item'):
#    print(item.get_text())

# Navigation
# el = soup.body.contents[1].contents[1].find_next_sibling()
# el = soup.find(id='section_2').find_previous_sibling()
# el = soup.find(class_='item').find_parent()
el = soup.find('h3').find_next_sibling('p')


print(el)
