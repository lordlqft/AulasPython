import os
import pygame

def load_isaac_images():
    base_path = os.path.join(os.getcwd(), "Jogos", "Assets", "Isaac_Images")

    directions = {
        "down": ["IsaacWalkDown1.png", "IsaacWalkDown2.png", "IsaacIdleDown.png"],
        "up": ["IsaacWalkForward1.png", "IsaacWalkForward2.png", "IsaacIdleForward.png"],
        "left": ["IsaacWalkLeft1.png", "IsaacWalkLeft2.png", "IsaacIdleLeft.png"],
        "right": ["IsaacWalkRight1.png", "IsaacWalkRight2.png", "IsaacIdleRight.png"]
    }

    images = {}

    for direction, files in directions.items():
        frames = []
        for file in files:
            full_path = os.path.join(base_path, file)
            if not os.path.exists(full_path):
                raise FileNotFoundError(f"Imagem não encontrada: {full_path}")
            img = pygame.image.load(full_path).convert_alpha()
            frames.append(img)
        images[direction] = frames

    return images
