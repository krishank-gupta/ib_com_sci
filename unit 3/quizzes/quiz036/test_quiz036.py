import pytest
from quiz036 import Person, Student

def test_Person():
    person = Person(name="John Doe", age=16)
    assert person.get_name() == 'John Doe'
    assert person.get_age() == 16

def test_Student():
    student = Student(name="John Doe2", age=16, grade='78%')
    assert student.get_name() == 'John Doe2'
    assert student.get_grade() == '78%'

def test_exceptions():
    with pytest.raises(TypeError):
        student = Student(name=24, age=16, grade='78')
        student = Student(name='John Doe3', age="16", grade='78')
