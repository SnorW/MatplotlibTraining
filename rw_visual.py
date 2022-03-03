import matplotlib.pyplot as plt

from random_walk import RandomWalk

colors = ['r', 'b', 'g', 'w', 'y', 'g']
walks = range(1, 7)
sim = ('s', 'sim')
nao = ('nao', 'não', 'n')


while True:
    plt.style.use('classic')

    rw = RandomWalk()
    rw.fill_walk()

    fig, axs = plt.subplots()

    point_numbers = range(rw.num_points)
    axs.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none'
                , s=2)
    axs.scatter(rw.x_values[-1], rw.y_values[-1], c='r', s=20)
    axs.scatter(rw.x_values[0], rw.y_values[0], c='g', s=20)

    axs.get_xaxis().set_visible(False)
    axs.get_yaxis().set_visible(False)

    plt.show()
    keep_running = input('Deseja executar novamente?')
    if keep_running in nao:
        break