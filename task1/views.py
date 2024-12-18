from django.shortcuts import render
from .models import Buyer, Game

def create_data(request):
    # Создаем покупателей
    buyer1 = Buyer.objects.create(name="ilya", balance=1500.05, age=24)
    buyer2 = Buyer.objects.create(name="Terminator2000", balance=42.15, age=52)
    buyer3 = Buyer.objects.create(name="Ubivator432", balance=0.5, age=16)  # Младше 18

    # Создаем игры
    game1 = Game.objects.create(title="Cyberpunk2077", cost=31.00, size=6.2, description="Game of the year 1", age_limited=True)
    game2 = Game.objects.create(title="Mario", cost=5.00, size=0.5, description="Old Game", age_limited=False)
    game3 = Game.objects.create(title="Hitman", cost=12.00, size=3.6, description="Who kills Mark 21", age_limited=True)

    return render(request, 'success.html')

def assign_games_to_buyers(request):
    # Получаем покупателей и игры
    buyer1 = Buyer.objects.get(name="ilya")
    buyer2 = Buyer.objects.get(name="Terminator2000")
    buyer3 = Buyer.objects.get(name="Ubivator432")

    game1 = Game.objects.get(title="Cyberpunk2077")
    game2 = Game.objects.get(title="Mario")
    game3 = Game.objects.get(title="Hitman")

    # Связываем покупателей с играми
    # Buyer1 (ilya) получает все игры
    game1.buyer.set([buyer1, buyer2])
    game2.buyer.set([buyer1, buyer2, buyer3])
    game3.buyer.set([buyer1, buyer2])

    # Buyer3 (Ubivator432) не получает игры с ограничением возраста
    game1.buyer.remove(buyer3)
    game3.buyer.remove(buyer3)

    return render(request, 'success.html')