class RubiksCube:
    def __init__(self):
        # Représentation du cube avec chaque face : U, D, L, R, F, B
        self.cube = {
            'U': ['U'] * 9,  # Haut
            'D': ['D'] * 9,  # Bas
            'L': ['L'] * 9,  # Gauche
            'R': ['R'] * 9,  # Droite
            'F': ['F'] * 9,  # Avant
            'B': ['B'] * 9   # Arrière
        }

    def rotate_face_clockwise(self, face):
        # Effectuer une rotation de 90° dans le sens des aiguilles d'une montre sur une face
        self.cube[face] = [self.cube[face][6], self.cube[face][3], self.cube[face][0],
                           self.cube[face][7], self.cube[face][4], self.cube[face][1],
                           self.cube[face][8], self.cube[face][5], self.cube[face][2]]

    def rotate_face_counterclockwise(self, face):
        # Effectuer une rotation de 90° dans le sens inverse des aiguilles d'une montre sur une face
        self.cube[face] = [self.cube[face][2], self.cube[face][5], self.cube[face][8],
                           self.cube[face][1], self.cube[face][4], self.cube[face][7],
                           self.cube[face][0], self.cube[face][3], self.cube[face][6]]

    def move_U(self):
        self.rotate_face_clockwise('U')

    def move_D(self):
        self.rotate_face_clockwise('D')

    def move_R(self):
        self.rotate_face_clockwise('R')

    def move_L(self):
        self.rotate_face_clockwise('L')

    def move_F(self):
        self.rotate_face_clockwise('F')

    def move_B(self):
        self.rotate_face_clockwise('B')

    def move_U_prime(self):
        self.rotate_face_counterclockwise('U')

    def move_F_prime(self):
        self.rotate_face_counterclockwise('F')
    def move_R_prime(self):
        self.rotate_face_counterclockwise('R')

    # Méthodes supplémentaires pour appliquer des mouvements aux arêtes pour la croix
    def solve_cross(self):
        """
        Résoudre la croix de la première couche.
        """
        # Exemple pour résoudre la croix (admettons que la face "D" est la première couche)
        # Placer les arêtes de la première couche pour former la croix
        # Algorithmes de base peuvent être appliqués ici en fonction de l'état du cube.

        # Supposons que les arêtes sont mal orientées, nous pouvons utiliser un algorithme
        # pour orienter les arêtes sans perturber la première couche
        self.move_R_prime()
    self.move_D_prime()
    self.move_R()
    self.move_D()

        print("Croix résolue!")
        self.print_cube()

    def print_cube(self):
        for face in ['U', 'F', 'R', 'B', 'L', 'D']:
            print(f"{face}: {self.cube[face]}")

# Création d'un cube
cube = RubiksCube()

# Résolution de la croix
cube.solve_cross()
