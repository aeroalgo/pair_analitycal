import matplotlib.pyplot as plt


def get_chart(list_data: list):
    for data in list_data:
        plt.figure(figsize=(7, 7))
        plt.plot(data)
        plt.grid()
        plt.show()
    return
