import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="emoji_meals", # Replace with your own username
    version="0.0.1",
    author="Sam Wheating",
    author_email="SamWheating@gmail.com",
    description="Find what you can cook with your emojis 👨‍🍳",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/EmojiMeals/meals-python",
    packages=['emoji_meals'],
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)