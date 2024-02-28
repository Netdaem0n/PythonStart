# kolvo_tovara - кол-во товара
# price_t -цена тетрадки
# price_o - цена обложки
# totall - стоимость покупки

kolvo_tovara = int(input())
price_t = int(input())
price_o = int(input())
totall = (kolvo_tovara * price_t) + (kolvo_tovara * price_o)
print('стоимость покупки =', totall)
