from Q2.classes.Gender import Gender
from Q2.classes.ProfilePrivacy import ProfilePrivacy


class Person:
    _current_id = 1

    def __init__(self, name: str, gender: Gender, biography: str, privacy: ProfilePrivacy):
        self.id = f"{Person._current_id:04}"
        self.name = name
        self.gender = gender
        self.biography = biography
        self.privacy = privacy

        Person._current_id += 1

    def __str__(self):
        return f"""
Id: {self.id}
Name: {self.name}
Gender: {self.gender.name}
Biography: {self.biography}
Privacy: {self.privacy.name}
"""
