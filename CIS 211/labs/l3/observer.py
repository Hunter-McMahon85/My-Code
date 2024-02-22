class UOMember:
    def __init__(self, name: str):
        """
        initiator function for the uo member class
        :param name: the persons name
        """
        self.name = name

    def receive_notification(self, message: str):
        """
        indicates that the UO user has been sent a message
        :param message: message to be sent to the UO member
        :return: void
        """
        print(f"UOMember {self.name} received message: {message}")


class Police:
    def __init__(self):
        """
        initiator function for da police
        """
        self.member_registry = []

    def register_observer(self, observer: object):
        """
        adds uo members to the member registry
        :param observer: an instance of the UOmember class we add to the registry
        :return: void
        """
        self.member_registry.append(observer)

    def send_message(self, message: str, who=[UOMember]):
        """
        sends out a message to community members
        :param who: makes so that members of certian status only get a message (students, staff, faculty)
        :param message: message sent to the community
        :return: void
        """
        for i in self.member_registry:
            for n in who:
                if isinstance(i, n):
                    i.receive_notification(message)


# success:
"""
if __name__ == '__main__':
    police = Police()

    uo_member1 = UOMember('John')
    police.register_observer(uo_member1)
    uo_member2 = UOMember('Mary')
    police.register_observer(uo_member2)

    police.send_message('Police alert!')
"""


class Student(UOMember):
    def receive_notification(self, message: str):
        """
        indicates that the UO user has been sent a message
        :param message: message to be sent to the UO member
        :return: void
        """
        print(f"Student {self.name} received message: {message}")


class Faculty(UOMember):
    def receive_notification(self, message: str):
        """
        indicates that the UO user has been sent a message
        :param message: message to be sent to the UO member
        :return: void
        """
        print(f"Faculty {self.name} received message: {message}")


class Staff(UOMember):
    def receive_notification(self, message: str):
        """
        indicates that the UO user has been sent a message
        :param message: message to be sent to the UO member
        :return: void
        """
        print(f"Staff {self.name} received message: {message}")


# given code to run the file:

if __name__ == '__main__':
    police = Police()

    police.register_observer(Student('John'))
    police.register_observer(Faculty('Mary'))
    police.register_observer(Staff('Bob'))

    print("Notifying all:")
    police.send_message('Police alert 1!')

    print("Notifying just students:")
    police.send_message('Police alert 2!', [Student])

    print("Notifying faculty and staff:")
    police.send_message('Police alert 3!', [Faculty, Staff])
# success
