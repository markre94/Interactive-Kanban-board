from matplotlib import pyplot as plt
import numpy as np

def calculate(type_of_task, students):
    fig = plt.figure()
    ax = fig.add_axes([0, 0, 1, 1])
    ax.axis('equal')
    type_of_task = ['TODO', 'DOING', 'DONE']
    students = [10,50,90]
    ax.pie(students, labels=type_of_task, autopct='%1.2f%%')
    plt.show()
    plt.savefig("flask_app/templates/figures")
