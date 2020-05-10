# meals-python ![emoji? yes](https://img.shields.io/badge/emoji%3F-%F0%9F%91%8D-brightgreen) ![Tests](https://github.com/EmojiMeals/meals-python/workflows/Tests/badge.svg?branch=master)

Find what you can cook with your emojis

## get started

install the package:

```console
pip install emoji-meals
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

# Provide ingredients in any order 💯💯IQ 🧠💥
mealify("🍰", "🌚") #=> "🥮"

# Use more than two items!
mealify("🍞","🍅","🧀") #=> "🍕"

# Provde a single argument!
mealify("🍞🍅🧀") #=> "🍕"

# Group your ingredients however you want!
mealify("🍞🍅", "🧀") #=> "🍕"

# After all this eating, I need a drink
mealify("🍶","🍾","🍷","🍸","🍶","🍹","🍺","🍻","🥂","🍾","🥃") #=> "🤮"
```

## Can I donate to the project?
[Yes, here](https://www.buymeacoffee.com/emoji)

## License

This project is licensed under the [MIT License](https://github.com/EmojiMeals/meals-go/blob/master/LICENSE).
