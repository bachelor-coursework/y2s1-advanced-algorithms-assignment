from Q2.classes.Person import Person
from Q2.classes.Gender import Gender
from Q2.classes.ProfilePrivacy import ProfilePrivacy

_people = [
    Person("Alice Tan", Gender.FEMALE, "Loves baby products and morning walks.", ProfilePrivacy.PUBLIC),
    Person("Benjamin Lee", Gender.MALE, "Father of two, enjoys DIY projects.", ProfilePrivacy.PRIVATE),
    Person("Carmen Lim", Gender.FEMALE, "Coffee lover and part-time baker.", ProfilePrivacy.PRIVATE),
    Person("Daniel Ong", Gender.MALE, "Gadget geek and weekend cyclist.", ProfilePrivacy.PUBLIC),
    Person("Emily Wong", Gender.FEMALE, "Dog mom who loves cozy cafes.", ProfilePrivacy.PUBLIC),
    Person("Felix Tan", Gender.MALE, "Fitness enthusiast and tech reviewer.", ProfilePrivacy.PUBLIC),
    Person("Grace Lau", Gender.FEMALE, "Bookworm who enjoys quiet afternoons.", ProfilePrivacy.PRIVATE),
    Person("Henry Chua", Gender.MALE, "Aspiring chef who experiments at home.", ProfilePrivacy.PUBLIC),
    Person("Isabelle Lim", Gender.FEMALE, "Music teacher and cat lover.", ProfilePrivacy.PRIVATE),
    Person("Jack Low", Gender.MALE, "Traveler and food photographer.", ProfilePrivacy.PRIVATE),
]

people = {person.id: person for person in _people}
