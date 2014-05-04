import pygame

class My_Button:
   def __init__(self, text):
      self.text = text
      self.is_hover = False
      self.default_color = (200,250,100)
      self.hover_color = (255,255,255)
      self.font_color = (0,0,0)
      self.obj = None
      
   def label(self):
      '''button label font'''
      font = pygame.font.Font(None, 20)
      return font.render(self.text, 1, self.font_color)
      
   def color(self):
      
      if self.is_hover:
         return self.hover_color
      else:
         return self.default_color
         
   def draw(self, screen, mouse, rectcoord, labelcoord):
      '''create rect obj, draw, and change color based on input'''
      self.obj  = pygame.draw.rect(screen, self.color(), rectcoord)
      screen.blit(self.label(), labelcoord)
      
    
      self.check_hover(mouse)
      
   def check_hover(self, mouse):
      '''adjust is_hover value based on mouse over button - to change hover color'''
      if self.obj.collidepoint(mouse):
         self.is_hover = True 
      else:
         self.is_hover = False
         
   def onClick(self):
        