class Rectangle:

  def __init__ (self, width, height):
    self.width = width
    self.height = height
    
  def set_width(self, width):
    self.width = width

  def set_height(self, height):
    self.height = height

  def get_area(self):
    return (self.width * self.height)

  def get_perimeter(self):
    return (2 * self.width + 2 * self.height)
  
  def get_diagonal(self):
    return ((self.width ** 2 + self.height ** 2) ** .5)

  def get_picture(self):
    if self.width >= 50 or self.height >= 50:
      return "Too big for picture."
    pic = '*' * self.width + '\n'
    pic = pic * self.height
    return pic
      
      
  def get_amount_inside(self, ins):
    return self.get_area() // ins.get_area()

  def __str__(self):
    w = f"(width={self.width}"
    h = f"height={self.height}"
    output = "Rectangle" + w + ", " + h +")"
    return output
    

class Square(Rectangle):
  def __init__ (self, side):
    super().__init__(side, side)

  def set_side(self, side):
    self.width = side
    self.height = side

  def __str__(self):
    return f'Square(side={self.width})'
  
        
    