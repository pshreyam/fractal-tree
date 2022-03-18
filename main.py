from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


def tree(i):
    if i < 10:
        return
    else:
        # Logic
        pass


def clearScreen():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    gluOrtho2D(-150.0, 150.0, -150.0, 150.0)


def plot_tree():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.55, 0.19, 0.72)
    glPointSize(2.0)
    glBegin(GL_POINTS)
    tree(100)
    glEnd()
    glFlush()


if __name__ == "__main__":
    glutInit()
    glutInitDisplayMode(GLUT_RGB)
    glutCreateWindow("Fractal Tree")
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(50, 50)
    glutDisplayFunc(plot_tree)
    clearScreen()
    glutMainLoop()
