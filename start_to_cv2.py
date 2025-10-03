import cv2

# Ouvrir la caméra par défaut
camera = cv2.VideoCapture(0)

# Lire la première image
ret, image = camera.read()

# Boucle pour afficher la vidéo en direct
i =0
while i<100:
    i +=1
    # Lire une nouvelle image
    ret, image = camera.read()

    # Afficher l'image
    cv2.imshow("Caméra", image)

    # Attendre que l'utilisateur appuie sur une touche
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Libérer la caméra
camera.release()

# Fermer toutes les fenêtres
cv2.destroyAllWindows()
