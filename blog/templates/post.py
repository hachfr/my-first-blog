class Post    
  def __init__(self, content):
    self.content = content 
    self.published = False 

  def publish(self):
    if not self.published:
        self.published = True
        print("Post published successfully")
    else:
        print("Post is already published")


#Beispielverwendung:
my_post = Post("Mein erster Beitrag")
my_post.publish() #Veröffenntliche den Beitrag

  
   