class Education:
    def __init__(self):
        self.degree_name: str = ''
        self.graduated: bool = False
        self.graduation_date: str = ''
        self.school_name: str = ''
        self.school_abbreviation: str = ''
        self.city: str = ''
        self.state_full: str = ''
        self.state_abbreviated: str = ''
        self.overall_GPA: float = 0.0
        self.major_GPA: float = 0.0

    def __str__(self):
        pass


class Project:
    def __init__(self):
        self.types: list = []
        self.programs: list = []
        self.title: str = ''
        self.authors: list = []
        self.start_date: str = ''
        self.end_date: str = ''
        self.mentors: list = []
        self.publications: list = []
        self.presentations: list = []

    def __str__(self):
        pass


class Publication:
    def __init__(self):
        self.title: str = ''
        self.authors: list = []
        self.status: str = ''
        self.journal: str = ''
        self.date: str = ''

    def __str__(self):
        pass


class Presentation:
    def __init__(self):
        self.type: str = ''
        self.group: bool = False
        self.presenters: list = []
        self.asynchronous: bool = False
        self.conference_name: str = ''
        self.start_date: str = ''
        self.end_date: str = ''
        self.location: str = ''

    def __str__(self):
        pass
