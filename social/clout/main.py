class Clout(object):
    """
    Clout measures the "social" score for a set of people, based on the number
    weight of the followers of the person. That is, a person's score is
    the sum of its followers' scores, where each point is a follower.
    """
    def __init__(self):
        self.people = {}

    def get_person_by_name(self, name):
        """
        Get person from set of people by name string.
        :param string: name:
        :return obj: person:
        """
        if name:
            if name in self.people:
                person = self.people[name]
            else:
                person = Person(name=name)
                self.people[name] = person
        else:
            return None

        return person

    def follow(self, follower_name, followee_name):
        """
        Add the followee to the list of followers for the follower person and
        adjust his score.
        :param follower:
        :param followee:
        :return bool:
        """
        follower = self.get_person_by_name(follower_name)
        followee = self.get_person_by_name(followee_name)

        if follower in followee.followers:
            # Follower is already following followee.
            return False
        elif follower == followee:
            # Don't allow follower to follow himself.
            return False
        else:
            followee.add_follower(follower)

        # Add the follower's score plus 1 for him as a follower, i.e. you
        # accumulate his followers.
        followee.add_to_score(follower.score + 1)

        # Reset followee to reflect new score.
        self.people[followee_name] = followee

        return True

    def clout(self, person=None):
        """
        If person provided, print the clout of the person. Otherwise print the
        clout of all the people.
        :return string:
        """
        # TODO: Separate out the string printing from the functionality.
        clout = ""
        person = self.get_person_by_name(person)

        if person:
            clout = "{0} has {1} follower(s).\n".format(person.name, person.score)
        else:
            for name, person in self.people.iteritems():
                clout += "{0} has {1} follower(s).\n".format(person.name, person.score)

        return clout


class Person(object):
    # TODO: Add docstrings
    # TODO: Add value checking

    def __init__(self, *args, **kwargs):
        self.name = kwargs.get('name')
        self.followers = []
        self.score = 0

    def add_follower(self, follower):
        self.followers.append(follower)

    def add_to_score(self, score):
        self.score += score
