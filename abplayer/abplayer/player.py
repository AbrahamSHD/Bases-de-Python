"""
Este es el módulo de reproducción de música
"""


class Player:
    """
    Esta clase crea un reproductor de música
    """

    def play(self, song):
        """
        Reproduce la canción que
        recibió como parámetro

        Parameters:
        song(str): Este es un string con el path de la canción

        Returns:
        int: Devuelve 1 en caso de éxito, devuelve 0 en caso de fracasar
        """
        print(f"Reproduciendo canción: {song}")

    def stop(self):
        print("Stopping")
