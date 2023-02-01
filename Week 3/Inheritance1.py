# This is the generic class with the two attributes title and content 
class BlogPost:
    def __init__(self, title, content):
        self.title = title
        self.content = content
    
    # First method that publishes the title of the post 
    def publish(self):
        print("Publishing post with title: ", self.title)
    
    # Second method that edits the title and content of the post 
    def edit(self, new_title, new_content):
        self.title = new_title
        self.content = new_content

# This class is a subclass of the BlogPost class and it counts the number of words and prints it out
class TextPost(BlogPost):
    def __init__(self, title, content, word_count= None, letter_count= None):
        super().__init__(title, content)
        self.word_count = word_count
        self.letter_count = letter_count
        
    def count_words(self):
        if self.word_count is None:
            words = self.title + " " + self.content
            word_count = 0
            for word in words.split():
                word_count += 1
            self.word_count = word_count
        print("Word count of title and content is : ", self.word_count )

    def count_letters(self):
        if self.letter_count is None:
            letters = self.title + self.content
            letter_count = 0
            for letter in letters:
                letter_count += 1
            self.letter_count = letter_count
        print("Letter count for title and content is: ", self.letter_count)

#This class also a subclass from the BlogPost class and is used when users post an image post 
class ImagePost(BlogPost):
    def __init__(self, title, content, image_url, image_caption):
        super().__init__(title, content)
        self.image_url = image_url
        self.image_caption = image_caption
        
    def set_image(self, new_url, new_caption):
        self.image_url = new_url
        self.image_caption = new_caption

#This class also a subclass from the BlogPost class and is used when users post an video post         
class VideoPost(BlogPost):
    def __init__(self, title, content, video_url, video_length):
        super().__init__(title, content)
        self.video_url = video_url
        self.video_length = video_length
        
    def set_video(self, new_url, new_length):
        self.video_url = new_url
        self.video_length = new_length



# testing method to see if it works 
print("\n Text Post\n")

# create a text post
text_post = TextPost("This is a test text post", "The content of this post is to see if this code works.")
text_post.publish()
text_post.count_words()
text_post.count_letters()

print("\n Image Post\n")

# create an image post
image_post = ImagePost("This is a test Image Post", "The Content of the image post is to see if it works.", "https://www.sorenkaplan.com/wp-content/uploads/2017/07/Testing.jpg", "Test Image")
image_post.publish()
print("Image URL: ", image_post.image_url)
image_post.set_image("https://www.etestware.com/wp-content/uploads/2020/08/shutterstock_515285995-1200x580.jpg", "New Example Image")

print("\n Video Post\n")

# create a video post
video_post = VideoPost("My First Video Post", "The Content of the Video post is to see if it works.", "https://www.youtube.com/watch?v=JkmCb565fKg", 130)
video_post.publish()
print("Video URL: ", video_post.video_url)
video_post.set_video("https://www.youtube.com/watch?v=ae6P4OT41K8", 110)