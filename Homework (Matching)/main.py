
import pygame

pygame.init()
screen = pygame.display.set_mode((1000,800))
SHAPE_FONT = pygame.font.SysFont("arial", 35)

pentagon = pygame.image.load("pentagon.png")
rectangle = pygame.image.load("rectangle.png")
square = pygame.image.load("square.png")
trapezoid = pygame.image.load("trapezoid.png")
triangle = pygame.image.load("triangle.png")

pentagonT = SHAPE_FONT.render("pentagon", 1, (255,255,255))
rectangleT = SHAPE_FONT.render("rectangle", 1, (255,255,255))
squareT = SHAPE_FONT.render("square", 1, (255,255,255))
trapezoidT = SHAPE_FONT.render("trapezoid", 1, (255,255,255))
triangleT = SHAPE_FONT.render("triangle", 1, (255,255,255))

screen.blit(pentagon, (50,50))
screen.blit(rectangle, (50, 200))
screen.blit(square, (50, 350))
screen.blit(trapezoid, (50, 500))
screen.blit(triangle, (50,650))
screen.blit(trapezoidT, (800,100))
screen.blit(rectangleT, (800, 225))
screen.blit(pentagonT, (800, 350))
screen.blit(triangleT, (800, 500))
screen.blit(squareT, (800, 650))

pygame.display.update()

while True:
    event = pygame.event.poll()
    if event.type == pygame.MOUSEBUTTONDOWN:
        mouseP1 = pygame.mouse.get_pos()
        pygame.draw.circle(screen, (0,255,0), mouseP1, 10, 0)
        pygame.display.update()
        
    elif event.type == pygame.MOUSEBUTTONUP:
        mouseP2 = pygame.mouse.get_pos()
        pygame.draw.circle(screen, (0,255,0), mouseP2, 10, 0)
        pygame.draw.line(screen, (0,255,0), (mouseP1), (mouseP2), 2,)
        pygame.display.update()
    
