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

        # A person can have an unlimited number of followers.
        # A person can only follow one person.
        # A person can change who they follow.
        # A person may not follow her/himself.

        if follower == followee:
            # Don't allow follower to follow himself.
            return False

        # Unset current_followee score: current_followee score = current_followee score - (follower + follower score)
        if follower.current_followee:
            follower.current_followee.add_to_score(-(1 + follower.score))
            self.people[follower.current_followee.name] = follower.current_followee
    
        # Adjust followee current_followee score: followee.current_followee score = followee.current_followee score + follower + follower score
        if followee.current_followee:
            followee.current_followee.add_to_score(1 + follower.score)
            self.people[followee.current_followee.name] = followee.current_followee

        # Set followee score: followee score = followee score + follower + follower score
        followee.add_to_score(1 + follower.score)
        self.people[followee_name] = followee

        # Finally, set follower's current_followee to followee
        follower.set_current_followee(followee)
        self.people[follower_name] = follower

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
        self.current_followee = None
        self.followers = []
        self.score = 0

    def set_current_followee(self, followee):
        self.current_followee = followee

    def add_follower(self, follower):
        self.followers.append(follower)

    def add_to_score(self, score):
        self.score += score
