from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


# Angles for rotating the tree for viewing purposes
angle1: float = 0.0
angle2: float = 0.0

# Defining the motion when rotating the tree with the mouse
# for viewing
moving: int = 0
startx: int = 0
starty: int = 0

# Defining the color
r: float = 0.0
g: float = 1.0
b: float = 0.0


def resize(width: int, height: int) -> None:
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-12.0, 12.0, -1.0, 20.0, -15.0, 15.0)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def cylinder(height: float, base: float) -> None:
    qobj = gluNewQuadric()
    glColor3f(r, g, b)
    glPushMatrix()
    glRotatef(-90, 1.0, 0.0, 0.0)
    gluCylinder(qobj, base, base - (0.2 * base), height, 20, 20)
    glPopMatrix()


def tree(height: float, base: float) -> None:
    glPushMatrix()
    cylinder(height, base)
    glTranslatef(0.0, height, 0.0)
    height -= height * 0.2
    base -= base * 0.3

    if height > 1:
        angle = 22.5
        glPushMatrix()
        glRotatef(angle, -1.0, 0.0, 0.0)
        tree(height, base)
        glPopMatrix()
        glPushMatrix()
        glRotatef(angle, 0.5, 0.0, 0.866)
        tree(height, base)
        glPopMatrix()
        glPushMatrix()
        glRotatef(angle, 0.5, 0.0, -0.866)
        tree(height, base)
        glPopMatrix()
    glPopMatrix()


def display() -> None:
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    glRotatef(angle1, 0, 1, 0)
    glRotatef(angle2, 0, 1, 0)

    tree(4.0, 0.1)
    glutSwapBuffers()
    glFlush()


def mouse(btn: int, state: int, x: int, y: int) -> None:
    global moving, startx, starty
    if btn == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        moving = 1
        startx = x
        starty = y
    if btn == GLUT_LEFT_BUTTON and state == GLUT_UP:
        moving = 0


def motion(x: int, y: int) -> None:
    global angle1, angle2, startx, starty
    if moving:
        angle1 = angle1 + (x - startx)
        angle2 = angle2 + (y - starty)
        startx = x
        starty = y
        glutPostRedisplay()


def clearScreen() -> None:
    glClearColor(0.0, 0.0, 0.0, 1.0)


if __name__ == "__main__":
    glutInit()
    glutInitDisplayMode(GLUT_RGB | GLUT_DOUBLE | GLUT_DEPTH)
    glutCreateWindow("3D Y-shaped Fractal Tree")
    glutInitWindowSize(1280, 960)
    glutInitWindowPosition(10, 10)
    glutDisplayFunc(display)
    glutReshapeFunc(resize)
    glutMouseFunc(mouse)
    glutMotionFunc(motion)
    clearScreen()
    glutMainLoop()
