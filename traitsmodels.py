from traits.api import *
from traitsui.api import *

class BasicInfo(HasTraits):
    character_type = Enum('PC', 'INPC', 'NPC',)
    name = String()
    random_name = Button()
    gender = Enum('male', 'female')
    age = Range(15, 60)
    random_age = Button()

class Quirks(HasTraits):
    quirks = List(editor=CheckListEditor(values=['pious', 'dark', 'cheerful', 'bloody'], cols=1))

    view = View(
        Item('quirks', style='custom')
    )

class Disorders(HasTraits):
    disorders = List(editor=CheckListEditor(values=['pious', 'dark', 'cheerful', 'bloody'], cols=1))


class Personality(HasTraits):
    prime_motivation = Enum('vengeange', 'love')
    most_valued_person = Enum('self', 'parent')
    most_valued_posession = Enum('book', 'recording')
    how_feels_about_most_people = Enum('i hate almost everyone', 'I value no-one')
    inmode = Enum('secretive', 'paranoid')
    exmode = Enum('cheerful', 'fluffy')
    quirks = Instance(Quirks, ())
    disorders = Instance(Disorders, ())

    view = View(
        Item('prime_motivation'),
        Item('most_valued_person'),
        Item('most_valued_posession'),
        Item('how_feels_about_most_people'),
        Item('inmode'),
        Item('exmode'),
        Item('quirks'),
        Item('disorders')
    )


class Stats(HasTraits):
    intelligence = Range(1, 10)
    reflexes = Range(1, 10)
    technique = Range(1, 10)
    dexterity = Range(1, 10)
    strength = Range(1, 10)
    constitution = Range(1, 10)
    presense = Range(1, 10)
    body = Range(1, 10)
    move = Range(1, 10)
    willpower = Range(1, 10)

    luck = Int()
    humanity = Int()
    recovery = Int()
    endurance = Int()
    run = Int()
    sprint = Int()
    swim = Int()
    leap = Int()
    hits = Int()
    stun = Int()
    stun_defense = Int()
    resistance = Int()

    view = View(
        HGroup(
            Group(
                Item('intelligence'),
                Item('reflexes'),
                Item('technique'),
                Item('dexterity'),
                Item('presense'),
                Item('willpower'),
                Item('strength'),
                Item('constitution'),
                Item('move'),
                Item('body')
            ),
            Group(
                Item('luck'),
                Item('humanity'),
                Item('endurance'),
                Item('recovery'),
                Item('run'),
                Item('sprint'),
                Item('swim'),
                Item('leap'),
                Item('hits'),
                Item('stun'),

            ),
            Group(
                Item('stun_defense'),
                Item('resistance')
            )
        )
    )

    def calculate_luck(self):
        self.luck = (self.intelligence + self.reflexes) / 2

    def calculate_humanity(self):
        self.humanity = self.willpower * 10

    def calculate_resistance(self):
        self.resistance = self.willpower * 3

    def calculate_move_base(self):
        self.run = self.move * 2
        self.sprint = self.move * 3
        self.leap = self.move
        self.swim = self.move

    def calculate_endurance(self):
        self.endurance = self.constitution * 2

    def calculate_recovery(self):
        self.recovery = (self.strength + self.constitution) / 2

    def calculate_body_based(self):
        self.hits = self.body * 5
        self.stun = self.body * 5

    def _intelligence_changed(self):
        self.calculate_luck()

    def _reflexes_changed(self):
        self.calculate_luck()

    def _willpower_changed(self):
        self.calculate_humanity()
        self.calculate_resistance()

    def _body_changed(self):
        self.calculate_body_based()

    def _constitution_changed(self):
        self.calculate_endurance()
        self.calculate_recovery()

    def _strength_changed(self):
        self.calculate_recovery()

    def _move_changed(self):
        self.calculate_move_base()

class CharacterSheet(HasTraits):
    basic_info = Instance(BasicInfo, ())
    stats = Instance(Stats, ())
    personality = Instance(Personality, ())

    traits_view = View(
        Group(
            Item('basic_info', style='custom'),
            Item('stats', style='custom')
        ),
        Item('personality', style='custom')

    )

if __name__ == '__main__':
    sheet = CharacterSheet()
    sheet.configure_traits()
