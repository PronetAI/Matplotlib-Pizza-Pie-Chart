toppings=["cheese","tomato","basil","onion","garlic"]
portions=[45,63,91,222,565]
colours=["r","b","c","g","m"]
plt.pie(portions,
        labels=toppings,
        colors=colours,
        shadow=True,
        explode=[0,1,0,0,0.5],
        autopct = "%1.2f%%")
plt.show()
