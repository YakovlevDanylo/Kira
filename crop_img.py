from PIL import Image


image_path = "slime.png"



image = Image.open(image_path)

# Параметры спрайтов
sprite_width = 32
sprite_height = 32
num_sprites = 1


for i in range(num_sprites):

    left = 0
    upper = i * sprite_height
    right = sprite_width
    lower = upper + sprite_height


    sprite = image.crop((left, upper, right, lower))


    sprite.save(f"slime{i}.png")
    print(f"Спрайт {i} сохранён")

print("Все спрайты сохранены успешно!")