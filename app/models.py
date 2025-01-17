class Sources:
    '''
    Source class that defines source objects
    '''
    def __init__(self,id,name,description,url,category,language,country):
        self.id = id
        self.name = name
        self.description = description
        self.url = url
        self.category = category
        self.language = language
        self.country = country

class Top_Headlines :
  '''
  Source class to define Top_headlines Objects
  '''
  def __init__(self, author, title, description, url, urlToImage, publishedAt, content) :
    self.author = author
    self.title = title
    self.description = description
    self.url = url
    self.urlToImage = urlToImage
    self.publishedAt = publishedAt
    self.content = content

class Everything :
  '''
  Source class to define Everything Objects
  '''
  def __init__(self, author, title, description, url, urlToImage, publishedAt, content) :
    self.author = author
    self.title = title
    self.description = description
    self.url = url
    self.urlToImage = urlToImage
    self.publishedAt = publishedAt
    self.content = content
