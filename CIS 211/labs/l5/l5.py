from typing import List, Set, Dict, Optional


class Student:
    def __init__(self, name: str, interests: List[str]):
        self.name = name
        self.interests = interests
        self.freetimes = {8, 9, 10, 11, 12, 13, 14, 15, 16}
        self.meetings: List[int] = []

    def schedule_meeting(self, time: int):
        if time in self.freetimes:
            self.freetimes.remove(time)
            self.meetings.append(time)


class Club:
    def __init__(self, name: str):
        self.name = name
        self.members: List[Student] = []
        self.meeting_time: Optional[int] = None

    def join(self, student: Student):
        self.members.append(student)

    def find_common_time(self):
        # free_times = [self.members[i].freetimes for i in self.members]
        free_times = []
        for i in self.members:
            free_times.append(self.members[i].freetimes)
        common_times = []
        for i in free_times:
            for j in i:
                for x in free_times:
                    if j in x:
                        common_times.append(j)
                    else:
                        common_times.remove(j)
                        break
        if len(common_times) == 0:
            return 0
        else:
            return common_times[0]

    def __str__(self) -> str:
        member_names = [member.name for member in self.members]
        return f"{self.name} ({', '.join(member_names)})"


class ASUO:
    def __init__(self):
        self.students: List[Student] = []
        self.clubs: List[Club] = []

    def enroll(self, student: Student):
        self.students.append(student)

    def form_clubs(self):
        clubs_to_form: Dict[str, Club] = {}
        for i in self.students:
            for j in i.interests:
                if j not in clubs_to_form:
                    clubs_to_form[j] = Club(j)
        for key in clubs_to_form:
            if clubs_to_form[key] not in self.clubs:
                self.clubs.append(clubs_to_form[key])

    def schedule_clubs(self):
        for i in self.clubs:
            i.find_common_time()

    def print_club_schedule(self):
        for club in self.clubs:
            if club.meeting_time is not None:
                print(f"{club} meets at {club.meeting_time}")


asuo = ASUO()
asuo.enroll(Student("Marty", ["badminton", "robotics"]))
asuo.enroll(Student("Kim", ["backgammon"]))
asuo.enroll(Student("Tara", ["robotics", "horticulture", "chess"]))
asuo.enroll(Student("George", ["chess", "badminton"]))

asuo.form_clubs()
asuo.schedule_clubs()
asuo.print_club_schedule()
