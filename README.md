# meals-python ![emoji? yes](https://img.shields.io/badge/emoji%3F-%F0%9F%91%8D-brightgreen)
Find what you can cook with your emojis

## get started

install the package:

```console
pip install emoji-meal
```

then start using it:

```console
from emoji-meals import mealify
mealify("🍞","🍅","🧀")

>>> 🍕
```

## Usage 

```python
mealify("🌚","🍰") #=> "🥮"

# it is not order dependent 💯💯IQ 🧠💥
mealify("🍰", "🌚") #=> "🥮"

# Use more than two items!
mealify("🍞","🍅","🧀") #=> "🍕"

# After all this eating, I need a drink
mealify("🍶","🍾","🍷","🍸","🍶","🍹","🍺","🍻","🥂","🍾","🥃") #=> "🤮"
```

## Can I donate to the project?
[Yes, here](https://www.buymeacoffee.com/emoji)

## License

This project is licensed under the [MIT License](https://github.com/EmojiMeals/meals-go/blob/master/LICENSE).
