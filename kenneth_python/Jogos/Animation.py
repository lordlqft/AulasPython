def animar_isaac(isaac_images, direcao, ultima_direcao, movendo, frame):
    frames = isaac_images[ultima_direcao if movendo else "down"]
    animacao = [frames[0], frames[2], frames[1], frames[2]]

    if movendo:
        frame += 0.15
        if frame >= len(animacao):
            frame = 0
        imagem = animacao[int(frame)]
    else:
        imagem = isaac_images["down"][2]

    return imagem, frame
