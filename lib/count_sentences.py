class MyString:
    def __init__(self, value=""):
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if not isinstance(new_value, str):
            print("The value must be a string.")
        else:
            self._value = new_value

    def is_sentence(self):
        return self.value.endswith(".")

    def is_question(self):
        return self.value.endswith("?")

    def is_exclamation(self):
        return self.value.endswith("!")

    def count_sentences(self):
        # Replace ending marks with periods
        cleaned = (
            self.value
            .replace("?", ".")
            .replace("!", ".")
        )

        # Split and filter empty chunks
        parts = cleaned.split(".")
        sentences = [p for p in parts if p.strip()]

        return len(sentences)